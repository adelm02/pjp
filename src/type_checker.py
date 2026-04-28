from generated.PLCParser import PLCParser
from generated.PLCVisitor import PLCVisitor

from .symbol_table import SymbolTable
from .types import PLCType, can_implicitly_convert


_NUMERIC = {PLCType.INT, PLCType.FLOAT}


class PLCTypeChecker(PLCVisitor):
    def __init__(self):
        self.symbols = SymbolTable()
        self.errors: list[str] = []
        self.needs_itof: dict[int, bool] = {}

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

    # EXTENSION: array — int a[10];
    # Zkontroluje ze 'a' jeste neexistuje a zapise ho do tabulky promennych
    def visitArrayDeclStmt(self, ctx):
        t = self.visit(ctx.type_())
        name = ctx.IDENT().getText()
        if not self.symbols.declare(name, t):
            self._err(ctx, f"variable '{name}' already declared")
        return None

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
                continue
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

    # --- types -----------------------------------------------------------

    def visitTypeInt(self, ctx):    return PLCType.INT
    def visitTypeFloat(self, ctx):  return PLCType.FLOAT
    def visitTypeBool(self, ctx):   return PLCType.BOOL
    def visitTypeString(self, ctx): return PLCType.STRING

    # --- literals --------------------------------------------------------

    def visitIntLit(self, ctx):     return PLCType.INT
    def visitFloatLit(self, ctx):   return PLCType.FLOAT
    def visitBoolLit(self, ctx):    return PLCType.BOOL
    def visitStringLit(self, ctx):  return PLCType.STRING

    def visitLiteralExpr(self, ctx: PLCParser.LiteralExprContext):
        return self._annotate(ctx, self.visit(ctx.literal()))

    def visitParenExpr(self, ctx: PLCParser.ParenExprContext):
        return self._annotate(ctx, self.visit(ctx.expression()))

    # --- expressions -----------------------------------------------------

    def visitIdentExpr(self, ctx: PLCParser.IdentExprContext):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return self._annotate(ctx, PLCType.ERROR)
        return self._annotate(ctx, self.symbols.type_of(name))

    # EXTENSION: array access — a[i]
    # Zkontroluje ze pole 'a' existuje a ze index je int
    # Vrati typ prvku pole (napr. INT pre int a[10])
    def visitArrayAccessExpr(self, ctx):
        name = ctx.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return self._annotate(ctx, PLCType.ERROR)
        idx_t = self.visit(ctx.expression())
        if idx_t != PLCType.INT and idx_t != PLCType.ERROR:
            self._err(ctx, "array index must be int")
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
        else:
            if t == PLCType.BOOL:
                return self._annotate(ctx, PLCType.BOOL)
            self._err(ctx, "unary '!' requires bool")
        return self._annotate(ctx, PLCType.ERROR)

    def _binary_numeric(self, ctx, lt, rt, op):
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
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if lt in _NUMERIC and rt in _NUMERIC:
            return self._annotate(ctx, PLCType.BOOL)
        self._err(ctx, f"operator '{ctx.op.text}' requires numeric operands")
        return self._annotate(ctx, PLCType.ERROR)

    def visitEqExpr(self, ctx: PLCParser.EqExprContext):
        lt = self.visit(ctx.expression(0))
        rt = self.visit(ctx.expression(1))
        if lt == PLCType.ERROR or rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if lt in _NUMERIC and rt in _NUMERIC:
            return self._annotate(ctx, PLCType.BOOL)
        if lt == PLCType.STRING and rt == PLCType.STRING:
            return self._annotate(ctx, PLCType.BOOL)
        self._err(ctx, f"operator '{ctx.op.text}' operand type mismatch")
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
        left = ctx.expression(0)
        right = ctx.expression(1)
        rt = self.visit(right)

        # EXTENSION: array assign — a[i] = value
        # Zkontroluje ze pole existuje a typ hodnoty sedi
        if isinstance(left, PLCParser.ArrayAccessExprContext):
            name = left.IDENT().getText()
            if not self.symbols.is_declared(name):
                self._err(ctx, f"variable '{name}' not declared")
                return self._annotate(ctx, PLCType.ERROR)
            lt = self.symbols.type_of(name)
            left.plc_type = lt
            self.visit(left.expression())
            if rt == PLCType.ERROR:
                return self._annotate(ctx, PLCType.ERROR)
            if not can_implicitly_convert(rt, lt):
                self._err(ctx, f"cannot assign {rt.value} to array of type {lt.value}")
                return self._annotate(ctx, PLCType.ERROR)
            self.needs_itof[id(ctx)] = (rt == PLCType.INT and lt == PLCType.FLOAT)
            return self._annotate(ctx, lt)

        # Normalne priradenie do premennej
        if not isinstance(left, PLCParser.IdentExprContext):
            self.visit(left)
            self._err(ctx, "left side of '=' must be a variable")
            return self._annotate(ctx, PLCType.ERROR)
        name = left.IDENT().getText()
        if not self.symbols.is_declared(name):
            self._err(ctx, f"variable '{name}' not declared")
            return self._annotate(ctx, PLCType.ERROR)
        lt = self.symbols.type_of(name)
        left.plc_type = lt
        if rt == PLCType.ERROR:
            return self._annotate(ctx, PLCType.ERROR)
        if not can_implicitly_convert(rt, lt):
            self._err(ctx, f"cannot assign {rt.value} to variable of type {lt.value}")
            return self._annotate(ctx, PLCType.ERROR)
        self.needs_itof[id(ctx)] = (rt == PLCType.INT and lt == PLCType.FLOAT)
        return self._annotate(ctx, lt)


# ===========================================================================
# VYSVETLENIE PRE OBHAJOBU
# ===========================================================================
# Co robi TypeChecker?
#   Prechádza strom a kontroluje typy. Zbiera VSETKY chyby naraz (nie len prvu).
#
# visitArrayDeclStmt — pre "int a[10];"
#   Zkontroluje ze 'a' este neexistuje, zapise do tabulky premennych ako INT
#
# visitArrayAccessExpr — pre "a[1]"
#   Zkontroluje ze 'a' je deklarovane a ze index je INT
#   Vrati typ prvku pola (INT pre int a[10])
#
# visitAssignExpr — pre "a[1] = 5"
#   Ak je lava strana ArrayAccessExpr → array assign
#   Zkontroluje ze pole existuje a typ hodnoty sedi
#
# _annotate — zapise typ vyrazu do uzla stromu (ctx.plc_type)
#   CodeGenerator ho potom precita cez ctx.plc_type
# ===========================================================================