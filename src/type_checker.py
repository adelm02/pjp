from generated.PLCParser import PLCParser
from generated.PLCVisitor import PLCVisitor

from .symbol_table import SymbolTable
from .types import PLCType, can_implicitly_convert


_NUMERIC = {PLCType.INT, PLCType.FLOAT}


class PLCTypeChecker(PLCVisitor):
    """Walks the parse tree, annotates every expression node with its type
    (`ctx.plc_type`), and collects every type error so that we can report
    them all (per the spec). Also fills the symbol table that the code
    generator will consume."""

    def __init__(self):
        self.symbols = SymbolTable()
        self.errors: list[str] = []
        # Per-AssignExpr flag: true when the right-hand side needs an
        # int -> float conversion. The code generator reads this so it knows
        # whether to emit `itof`.
        self.needs_itof: dict[int, bool] = {}

    # --- helpers ---------------------------------------------------------

    def _err(self, ctx, msg: str):
        tok = ctx.start
        self.errors.append(f"[type] line {tok.line}:{tok.column} {msg}")

    def _annotate(self, ctx, t: PLCType) -> PLCType:
        ctx.plc_type = t
        return t

    # --- statements ------------------------------------------------------

    def visitProgram(self, ctx: PLCParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)
        return None
    
#dvojita deklarace chyba
    def visitDeclStmt(self, ctx: PLCParser.DeclStmtContext):
        t = self.visit(ctx.type_())
        for ident in ctx.IDENT():
            name = ident.getText()
            if not self.symbols.declare(name, t):
                self._err(ctx, f"variable '{name}' already declared")
        return None

    def visitReadStmt(self, ctx: PLCParser.ReadStmtContext):
        for ident in ctx.IDENT():
            name = ident.getText()
            if not self.symbols.is_declared(name):
                self._err(ctx, f"variable '{name}' not declared")
        return None

    def visitWriteStmt(self, ctx: PLCParser.WriteStmtContext):
        for e in ctx.expression():
            t = self.visit(e)
            if t == PLCType.ERROR:
                continue  # already reported
            if t not in (PLCType.INT, PLCType.FLOAT, PLCType.BOOL, PLCType.STRING):
                self._err(e, f"cannot write value of type {t.value}")
        return None

    def visitBlockStmt(self, ctx: PLCParser.BlockStmtContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitIfStmt(self, ctx: PLCParser.IfStmtContext):
        cond_t = self.visit(ctx.expression())
        if cond_t != PLCType.BOOL and cond_t != PLCType.ERROR:
            self._err(ctx.expression(), "if condition must be bool")
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitWhileStmt(self, ctx: PLCParser.WhileStmtContext):
        cond_t = self.visit(ctx.expression())
        if cond_t != PLCType.BOOL and cond_t != PLCType.ERROR:
            self._err(ctx.expression(), "while condition must be bool")
        self.visit(ctx.statement())
        return None

    def visitExprStmt(self, ctx: PLCParser.ExprStmtContext):
        self.visit(ctx.expression())
        return None

    def visitEmptyStmt(self, ctx):
        return None

    # ====================================================================
    # EXTENSION: for cycle (Vašínek)
    #   for (init; cond; step) statement
    #   init, step are arbitrary expressions; cond must be bool.
    # ====================================================================
    def visitForStmt(self, ctx: PLCParser.ForStmtContext):
        self.visit(ctx.expression(0))                    # init
        cond_t = self.visit(ctx.expression(1))           # cond
        if cond_t != PLCType.BOOL and cond_t != PLCType.ERROR:
            self._err(ctx.expression(1), "for condition must be bool")
        self.visit(ctx.expression(2))                    # step
        self.visit(ctx.statement())
        return None

    # ====================================================================
    # EXTENSION: FILE / fopen / fappend
    #   Per the .md notes from the cviko, type checking for these is
    #   intentionally lax — we only verify that the file variable was
    #   declared as FILE. fappend's value arguments are not type-checked.
    # ====================================================================

    def visitFopenStmt2(self, ctx):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
        elif self.symbols.type_of(name) != PLCType.FILE:
            self._err(ctx, f"fopen requires a FILE variable")
        return None

    def visitFwriteStmt(self, ctx):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
        elif self.symbols.type_of(name) != PLCType.FILE:
            self._err(ctx, f"fwrite target must be FILE")
        for e in ctx.expression():
            self.visit(e)
        return None

#kontrola jestli ident (f) jeste neexistuje
    def visitFileDeclStmt(self, ctx: PLCParser.FileDeclStmtContext):
        for ident in ctx.IDENT():
            name = ident.getText()
            if not self.symbols.declare(name, PLCType.FILE):
                self._err(ctx, f"variable '{name}' already declared")
        return None

    def visitFopenStmt(self, ctx: PLCParser.FopenStmtContext):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
        elif self.symbols.type_of(name) != PLCType.FILE:
            self._err(ctx, f"fopen requires a FILE variable, got {self.symbols.type_of(name).value}")
        path_t = self.visit(ctx.expression())
        if path_t != PLCType.STRING and path_t != PLCType.ERROR:
            self._err(ctx.expression(), "fopen path must be a string")
        return None

#kontrola fappend f, "abc";   ← ale nikde není FILE f;
    def _check_file_handle(self, ctx, name: str):
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return False
        if self.symbols.type_of(name) != PLCType.FILE:
            self._err(ctx, f"fappend target must be FILE, got {self.symbols.type_of(name).value}")
            return False
        return True

    def visitFappendV1Stmt(self, ctx: PLCParser.FappendV1StmtContext):
        # `fappend f, v1, v2, ... ;`
        self._check_file_handle(ctx, ctx.IDENT().getText())
        for e in ctx.expression():
            self.visit(e)  # any type is fine, no cross-check per spec note
        return None

    def visitFappendV2Stmt(self, ctx: PLCParser.FappendV2StmtContext):
        # `f << v1 << v2 << ... ;`
        self._check_file_handle(ctx, ctx.IDENT().getText())
        for e in ctx.expression():
            self.visit(e)
        return None

    # --- types -----------------------------------------------------------

    def visitTypeInt(self, ctx):
        return PLCType.INT

    def visitTypeFloat(self, ctx):
        return PLCType.FLOAT

    def visitTypeBool(self, ctx):
        return PLCType.BOOL

    def visitTypeString(self, ctx):
        return PLCType.STRING

    # --- literals --------------------------------------------------------

    def visitIntLit(self, ctx):
        return PLCType.INT

    def visitFloatLit(self, ctx):
        return PLCType.FLOAT

    def visitBoolLit(self, ctx):
        return PLCType.BOOL

    def visitStringLit(self, ctx):
        return PLCType.STRING

    def visitLiteralExpr(self, ctx: PLCParser.LiteralExprContext):
        t = self.visit(ctx.literal())
        return self._annotate(ctx, t)

    def visitParenExpr(self, ctx: PLCParser.ParenExprContext):
        t = self.visit(ctx.expression())
        return self._annotate(ctx, t)

    # --- expressions -----------------------------------------------------
#kontrola bez deklarace typu
    def visitIdentExpr(self, ctx: PLCParser.IdentExprContext):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return self._annotate(ctx, PLCType.ERROR)
        return self._annotate(ctx, self.symbols.type_of(name))

    def visitUnaryExpr(self, ctx: PLCParser.UnaryExprContext):
        op = ctx.op.text
        t = self.visit(ctx.expression())
        if t == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if op == "-":
            if t in _NUMERIC:
                return self._annotate(ctx, t)
            self._err(ctx, "unary '-' requires int or float")
        else:  # op == '!'
            if t == PLCType.BOOL:
                return self._annotate(ctx, PLCType.BOOL)
            self._err(ctx, "unary '!' requires bool")
        return self._annotate(ctx, PLCType.ERROR)

    def _binary_numeric(self, ctx, lt, rt, op):
        # Integer-only unless either side is float; result type follows the
        # standard implicit int -> float promotion.
        if lt == PLCType.FLOAT or rt == PLCType.FLOAT:
            if lt in _NUMERIC and rt in _NUMERIC:
                return PLCType.FLOAT
        elif lt == PLCType.INT and rt == PLCType.INT:
            return PLCType.INT
        self._err(ctx, f"operator '{op}' requires numeric operands")
        return PLCType.ERROR

    def visitMulDivExpr(self, ctx: PLCParser.MulDivExprContext):
        op = ctx.op.text
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if op == "%":
            if lt == PLCType.INT and rt == PLCType.INT:
                return self._annotate(ctx, PLCType.INT)
            self._err(ctx, "operator '%' requires int operands")
            return self._annotate(ctx, PLCType.ERROR)
        return self._annotate(ctx, self._binary_numeric(ctx, lt, rt, op))

    def visitAddSubConcatExpr(self, ctx: PLCParser.AddSubConcatExprContext):
        op = ctx.op.text
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if op == ".":
            if lt == PLCType.STRING and rt == PLCType.STRING:
                return self._annotate(ctx, PLCType.STRING)
            self._err(ctx, "operator '.' requires string operands")
            return self._annotate(ctx, PLCType.ERROR)
        return self._annotate(ctx, self._binary_numeric(ctx, lt, rt, op))

    def visitRelExpr(self, ctx: PLCParser.RelExprContext):
        op = ctx.op.text
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if lt in _NUMERIC and rt in _NUMERIC:
            return self._annotate(ctx, PLCType.BOOL)
        self._err(ctx, f"operator '{op}' requires numeric operands")
        return self._annotate(ctx, PLCType.ERROR)

    def visitEqExpr(self, ctx: PLCParser.EqExprContext):
        op = ctx.op.text
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        # Spec: == / != allowed for {INT, FLOAT, STRING}.
        if lt in _NUMERIC and rt in _NUMERIC:
            return self._annotate(ctx, PLCType.BOOL)
        if lt == PLCType.STRING and rt == PLCType.STRING:
            return self._annotate(ctx, PLCType.BOOL)
        self._err(ctx, f"operator '{op}' operand type mismatch")
        return self._annotate(ctx, PLCType.ERROR)

    def visitAndExpr(self, ctx: PLCParser.AndExprContext):
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.BOOL and rt == PLCType.BOOL:
            return self._annotate(ctx, PLCType.BOOL)
        if lt != PLCType.ERROR and rt != PLCType.ERROR:
            self._err(ctx, "operator '&&' requires bool operands")
        return self._annotate(ctx, PLCType.ERROR)

    def visitOrExpr(self, ctx: PLCParser.OrExprContext):
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.BOOL and rt == PLCType.BOOL:
            return self._annotate(ctx, PLCType.BOOL)
        if lt != PLCType.ERROR and rt != PLCType.ERROR:
            self._err(ctx, "operator '||' requires bool operands")
        return self._annotate(ctx, PLCType.ERROR)

    def visitAssignExpr(self, ctx: PLCParser.AssignExprContext):
        # leva strana musi byt deklarovana (INT, STR nelze prevest)
        left = ctx.expression(0)
        right = ctx.expression(1)
        rt = self.visit(right)

        # Tighten the LHS check: only an IdentExpr is a valid target.
        if not isinstance(left, PLCParser.IdentExprContext):
            self.visit(left)
            self._err(ctx, "left side of '=' must be a variable")
            return self._annotate(ctx, PLCType.ERROR)

        name = left.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return self._annotate(ctx, PLCType.ERROR)
        lt = self.symbols.type_of(name)
        left.plc_type = lt  # annotate even though we skipped visit()

        if rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if not can_implicitly_convert(rt, lt):
            self._err(ctx, f"cannot assign {rt.value} to variable of type {lt.value}")
            return self._annotate(ctx, PLCType.ERROR)

        # Record whether codegen needs an itof for this assignment.
        self.needs_itof[id(ctx)] = (rt == PLCType.INT and lt == PLCType.FLOAT)
        return self._annotate(ctx, lt)

    # ====================================================================
    # EXTENSION: charAt — s[i]ffor
    #   string × int -> string  (returns a 1-char string).
    # ====================================================================
    def visitCharAtExpr(self, ctx: PLCParser.CharAtExprContext):
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if lt != PLCType.STRING:
            self._err(ctx, "charAt requires a string on the left of '['")
            return self._annotate(ctx, PLCType.ERROR)
        if rt != PLCType.INT:
            self._err(ctx, "charAt index must be int")
            return self._annotate(ctx, PLCType.ERROR)
        return self._annotate(ctx, PLCType.STRING)

    # ====================================================================
    # EXTENSION: ternary operator  cond ? a : b
    #   cond must be bool. a and b must share a numeric/common type;
    #   if one is int and the other float, result is float (with int side
    #   widened — codegen emits `itof` for the narrower branch).
    # ====================================================================
    def visitTernaryExpr(self, ctx: PLCParser.TernaryExprContext):
        cond_t = self.visit(ctx.expression(0))
        a_t = self.visit(ctx.expression(1))
        b_t = self.visit(ctx.expression(2))
        if cond_t != PLCType.BOOL and cond_t != PLCType.ERROR:
            self._err(ctx.expression(0), "ternary condition must be bool")
            return self._annotate(ctx, PLCType.ERROR)
        if a_t == PLCType.ERROR or b_t == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if a_t == b_t:
            return self._annotate(ctx, a_t)
        if a_t in _NUMERIC and b_t in _NUMERIC:
            return self._annotate(ctx, PLCType.FLOAT)
        self._err(ctx, f"ternary branches have incompatible types: {a_t.value} vs {b_t.value}")
        return self._annotate(ctx, PLCType.ERROR)
