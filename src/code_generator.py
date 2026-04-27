from generated.PLCParser import PLCParser
from generated.PLCVisitor import PLCVisitor

from .symbol_table import SymbolTable
from .types import PLCType, default_value


class PLCCodeGenerator(PLCVisitor):
    """Walks the (already type-checked) parse tree and emits the textual
    stack-machine program defined in the assignment. Expects the type
    checker has annotated every expression node with `plc_type` and recorded
    `needs_itof[id(assign_ctx)]` for every assignment that needs an
    implicit int -> float conversion."""

    def __init__(self, symbols: SymbolTable, needs_itof: dict[int, bool]):
        self.symbols = symbols
        self.needs_itof = needs_itof
        self._lines: list[str] = []
        self._next_label = 0

    # --- emission helpers ------------------------------------------------

    def emit(self, line: str):
        self._lines.append(line)

#skok, while, for
    def new_label(self) -> int:
        n = self._next_label
        self._next_label += 1
        return n

    def output(self) -> str:
        return "\n".join(self._lines) + ("\n" if self._lines else "")

    # --- entry -----------------------------------------------------------

    def generate(self, tree):
        self.visit(tree)
        return self.output()

    def _emit_push_default(self, t: PLCType):
        v = default_value(t)
        if t == PLCType.INT:
            self.emit(f"push I {v}")
        elif t == PLCType.FLOAT:
            self.emit(f"push F {v}")
        elif t == PLCType.BOOL:
            self.emit(f"push B {'true' if v else 'false'}")
        elif t == PLCType.STRING:
            self.emit(f'push S ""')
        # FILE has no default initialization — only `fopen` produces a value.

    def _emit_with_promotion(self, expr_ctx, target: PLCType):
        self.visit(expr_ctx)
        if expr_ctx.plc_type == PLCType.INT and target == PLCType.FLOAT:
            self.emit("itof")

    # --- statements ------------------------------------------------------

    def visitProgram(self, ctx: PLCParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)

    def visitDeclStmt(self, ctx: PLCParser.DeclStmtContext):
        t = self.symbols.type_of(ctx.IDENT(0).getText())
        for ident in ctx.IDENT():
            self._emit_push_default(t)
            self.emit(f"save {ident.getText()}")
        return None

    def visitEmptyStmt(self, ctx):
        return None

    def visitBlockStmt(self, ctx: PLCParser.BlockStmtContext):
        for st in ctx.statement():
            self.visit(st)

    def visitReadStmt(self, ctx: PLCParser.ReadStmtContext):
        for ident in ctx.IDENT():
            name = ident.getText()
            t = self.symbols.type_of(name)
            self.emit(f"read {t.code}")
            self.emit(f"save {name}")

    def visitWriteStmt(self, ctx: PLCParser.WriteStmtContext):
        # Push every value, then a single `print n` consumes them all.
        for e in ctx.expression():
            self.visit(e)
        self.emit(f"print {len(ctx.expression())}")

    def visitIfStmt(self, ctx: PLCParser.IfStmtContext):
        self.visit(ctx.expression())  # condition (bool) on stack
        else_label = self.new_label()
        end_label = self.new_label()
        self.emit(f"fjmp {else_label}")
        self.visit(ctx.statement(0))  # then branch
        self.emit(f"jmp {end_label}")
        self.emit(f"label {else_label}")
        if ctx.statement(1) is not None:
            self.visit(ctx.statement(1))  # else branch
        self.emit(f"label {end_label}")

    def visitWhileStmt(self, ctx: PLCParser.WhileStmtContext):
        cond_label = self.new_label()
        end_label = self.new_label()
        self.emit(f"label {cond_label}")
        self.visit(ctx.expression())
        self.emit(f"fjmp {end_label}")
        self.visit(ctx.statement())
        self.emit(f"jmp {cond_label}")
        self.emit(f"label {end_label}")

    def visitExprStmt(self, ctx: PLCParser.ExprStmtContext):
        self.visit(ctx.expression())
        # The expression's value is unused; discard it.
        self.emit("pop")

    # ====================================================================
    # EXTENSION: for cycle (Vašínek)
    #   Lowered to the equivalent while:
    #     init; while (cond) { body; step; }
    # ====================================================================
    def visitForStmt(self, ctx: PLCParser.ForStmtContext):
        # init expression — value discarded
        self.visit(ctx.expression(0))
        self.emit("pop")
        cond_label = self.new_label()
        end_label = self.new_label()
        self.emit(f"label {cond_label}")
        self.visit(ctx.expression(1))                    # cond
        self.emit(f"fjmp {end_label}")
        self.visit(ctx.statement())                      # body
        self.visit(ctx.expression(2))                    # step
        self.emit("pop")
        self.emit(f"jmp {cond_label}")
        self.emit(f"label {end_label}")

    # ====================================================================
    # EXTENSION: FILE / fopen / fappend
    #   Two variants of fappend coexist (see grammar header).
    # ====================================================================
    def visitFileDeclStmt(self, ctx: PLCParser.FileDeclStmtContext):
        # FILE handles aren't initialized — they only become valid after
        # fopen. We emit nothing for the declaration itself.
        return None

    def visitFopenStmt(self, ctx: PLCParser.FopenStmtContext):
        # Convention from the .md notes:  push S <path>; fopen; save f
        self.visit(ctx.expression())                     # path on stack
        self.emit("fopen")
        self.emit(f"save {ctx.IDENT().getText()}")

#fopen pondeli
    def visitFopenStmt2(self, ctx):
    # push S "soubor.txt"; open; save f
        path = ctx.STRING().getText()      # získej "soubor.txt" přímo z gramatiky
        self.emit(f"push S {path}")        # dej cestu na zásobník
        self.emit("open")                  # instrukce open (ne fopen!)
        self.emit(f"save {ctx.IDENT().getText()}")  # ulož handle do f

    def visitFwriteStmt(self, ctx):
        # load f; push v1; push v2; ...; fwrite N
        name = ctx.IDENT().getText()       # získej "f"
        self.emit(f"load {name}")          # dej f na zásobník
        for e in ctx.expression():         # pro každý výraz ("abc", 1+2...)
            self.visit(e)                  # vygeneruj instrukce pro výraz
        self.emit(f"fwrite {len(ctx.expression())}")  # fwrite N kde N = počet výrazů
#--------

    def visitFappendV1Stmt(self, ctx: PLCParser.FappendV1StmtContext):
        # `fappend f, v1, v2, ... ;`
        # -> load f; push v1; push v2; ...; fappend N
        # where N is the total number of values pushed (file handle + values).
        name = ctx.IDENT().getText()
        self.emit(f"load {name}")
        for e in ctx.expression():
            self.visit(e)
        self.emit(f"fappend {1 + len(ctx.expression())}")

    def visitFappendV2Stmt(self, ctx: PLCParser.FappendV2StmtContext):
        # `f << v1 << v2 << ... ;`
        # -> load f; (push v1; fappend; push v2; fappend; ...); pop
        # `fappend` (no count) writes 1 value and leaves the file handle on
        # the stack so the next `<<` can chain.
        name = ctx.IDENT().getText()
        self.emit(f"load {name}")
        for e in ctx.expression():
            self.visit(e)
            self.emit("fappend")
        self.emit("pop")

    # --- expressions -----------------------------------------------------

    def visitParenExpr(self, ctx):
        self.visit(ctx.expression())

    def visitLiteralExpr(self, ctx: PLCParser.LiteralExprContext):
        self.visit(ctx.literal())

    def visitIntLit(self, ctx):
        self.emit(f"push I {ctx.getText()}")

    def visitFloatLit(self, ctx):
        self.emit(f"push F {ctx.getText()}")

    def visitBoolLit(self, ctx):
        self.emit(f"push B {ctx.getText()}")

    def visitStringLit(self, ctx):
        # Keep the surrounding quotes; the spec's instruction set uses
        # `push S "..."` form already.
        self.emit(f"push S {ctx.getText()}")

    def visitIdentExpr(self, ctx: PLCParser.IdentExprContext):
        self.emit(f"load {ctx.IDENT().getText()}")

    def visitUnaryExpr(self, ctx: PLCParser.UnaryExprContext):
        op = ctx.op.text
        self.visit(ctx.expression())
        if op == "-":
            self.emit(f"uminus {ctx.expression().plc_type.code}")
        else:
            self.emit("not")

    def _emit_binary_numeric(self, ctx, opname: str):
        result_t = ctx.plc_type
        self._emit_with_promotion(ctx.expression(0), result_t)
        self._emit_with_promotion(ctx.expression(1), result_t)
        self.emit(f"{opname} {result_t.code}")

    def visitMulDivExpr(self, ctx: PLCParser.MulDivExprContext):
        op = ctx.op.text
        if op == "%":
            self.visit(ctx.expression(0))
            self.visit(ctx.expression(1))
            self.emit("mod")
            return
        self._emit_binary_numeric(ctx, {"*": "mul", "/": "div"}[op])

    def visitAddSubConcatExpr(self, ctx: PLCParser.AddSubConcatExprContext):
        op = ctx.op.text
        if op == ".":
            self.visit(ctx.expression(0))
            self.visit(ctx.expression(1))
            self.emit("concat")
            return
        self._emit_binary_numeric(ctx, {"+": "add", "-": "sub"}[op])

    def visitRelExpr(self, ctx: PLCParser.RelExprContext):
        op = ctx.op.text
        l, r = ctx.expression(0), ctx.expression(1)
        target = PLCType.FLOAT if PLCType.FLOAT in (l.plc_type, r.plc_type) else PLCType.INT
        self._emit_with_promotion(l, target)
        self._emit_with_promotion(r, target)
        self.emit(f"{'gt' if op == '>' else 'lt'} {target.code}")

    def visitEqExpr(self, ctx: PLCParser.EqExprContext):
        op = ctx.op.text
        l, r = ctx.expression(0), ctx.expression(1)
        if l.plc_type == PLCType.STRING:
            self.visit(l)
            self.visit(r)
            self.emit("eq S")
        else:
            target = PLCType.FLOAT if PLCType.FLOAT in (l.plc_type, r.plc_type) else PLCType.INT
            self._emit_with_promotion(l, target)
            self._emit_with_promotion(r, target)
            self.emit(f"eq {target.code}")
        if op == "!=":
            self.emit("not")

    def visitAndExpr(self, ctx: PLCParser.AndExprContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.emit("and")

    def visitOrExpr(self, ctx: PLCParser.OrExprContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.emit("or")

    def visitAssignExpr(self, ctx: PLCParser.AssignExprContext):
        # Evaluate RHS, possibly widen, store into LHS variable, and leave
        # the value on the stack (so `=` can be used inside larger exprs).
        right = ctx.expression(1)
        self.visit(right)
        if self.needs_itof.get(id(ctx), False):
            self.emit("itof")
        name = ctx.expression(0).IDENT().getText()
        self.emit(f"save {name}")
        self.emit(f"load {name}")

    # ====================================================================
    # EXTENSION: charAt — postfix s[i]
    #   stack: ..., string, int -> charAt -> ..., string(1)
    # ====================================================================
    def visitCharAtExpr(self, ctx: PLCParser.CharAtExprContext):
        self.visit(ctx.expression(0))                    # string
        self.visit(ctx.expression(1))                    # index (int)
        self.emit("charAt")

    # ====================================================================
    # EXTENSION: ternary operator  cond ? a : b
    #   eval cond; fjmp Lf; eval a; jmp Lend; label Lf; eval b; label Lend;
    #   With int->float promotion if branches mix int and float.
    # ====================================================================
    def visitTernaryExpr(self, ctx: PLCParser.TernaryExprContext):
        cond = ctx.expression(0)
        a = ctx.expression(1)
        b = ctx.expression(2)
        target = ctx.plc_type

        false_label = self.new_label()
        end_label = self.new_label()
        self.visit(cond)
        self.emit(f"fjmp {false_label}")
        self._emit_with_promotion(a, target)
        self.emit(f"jmp {end_label}")
        self.emit(f"label {false_label}")
        self._emit_with_promotion(b, target)
        self.emit(f"label {end_label}")
