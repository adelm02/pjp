from generated.PLCParser import PLCParser
from generated.PLCVisitor import PLCVisitor

from .symbol_table import SymbolTable
from .types import PLCType, default_value


class PLCCodeGenerator(PLCVisitor):
    def __init__(self, symbols: SymbolTable, needs_itof: dict[int, bool]):
        self.symbols = symbols
        self.needs_itof = needs_itof
        self._lines: list[str] = []
        self._next_label = 0

    def emit(self, line: str):
        # Prida jednu instrukciu do zoznamu — ako napisat krok do receptu
        self._lines.append(line)

    def new_label(self) -> int:
        # Vrati unikatne cislo pre label (pouziva sa pre if/while skoky)
        n = self._next_label
        self._next_label += 1
        return n

    def output(self) -> str:
        return "\n".join(self._lines) + ("\n" if self._lines else "")

    def generate(self, tree):
        self.visit(tree)
        return self.output()

    def _emit_push_default(self, t: PLCType):
        v = default_value(t)
        if t == PLCType.INT:    self.emit(f"push I {v}")
        elif t == PLCType.FLOAT:  self.emit(f"push F {v}")
        elif t == PLCType.BOOL:   self.emit(f"push B {'true' if v else 'false'}")
        elif t == PLCType.STRING: self.emit(f'push S ""')

    def _emit_with_promotion(self, expr_ctx, target: PLCType):
        self.visit(expr_ctx)
        if expr_ctx.plc_type == PLCType.INT and target == PLCType.FLOAT:
            self.emit("itof")

    # --- statements ------------------------------------------------------

    def visitProgram(self, ctx: PLCParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)

    # EXTENSION: array declaration — int a[10];
    # Generuje: createarray a 10
    # createarray uz ulozi pole priamo do vars — nepotrebujeme save
    def visitArrayDeclStmt(self, ctx):
        name = ctx.IDENT().getText()   # nazov pola napr. "a"
        size = ctx.INT().getText()     # velkost pola napr. "10"
        self.emit(f"createarray {name} {size}")  # vytvor pole a uloz do vars
        return None

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
        for e in ctx.expression():
            self.visit(e)
        self.emit(f"print {len(ctx.expression())}")

    def visitIfStmt(self, ctx: PLCParser.IfStmtContext):
        self.visit(ctx.expression())
        else_label = self.new_label()
        end_label = self.new_label()
        self.emit(f"fjmp {else_label}")
        self.visit(ctx.statement(0))
        self.emit(f"jmp {end_label}")
        self.emit(f"label {else_label}")
        if ctx.statement(1) is not None:
            self.visit(ctx.statement(1))
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
        self.emit("pop")

    # --- expressions -----------------------------------------------------

    def visitParenExpr(self, ctx):
        self.visit(ctx.expression())

    def visitLiteralExpr(self, ctx: PLCParser.LiteralExprContext):
        self.visit(ctx.literal())

    def visitIntLit(self, ctx):    self.emit(f"push I {ctx.getText()}")
    def visitFloatLit(self, ctx):  self.emit(f"push F {ctx.getText()}")
    def visitBoolLit(self, ctx):   self.emit(f"push B {ctx.getText()}")
    def visitStringLit(self, ctx): self.emit(f"push S {ctx.getText()}")

    def visitIdentExpr(self, ctx: PLCParser.IdentExprContext):
        self.emit(f"load {ctx.IDENT().getText()}")

    # EXTENSION: array access — a[i]
    # Generuje: load a / push index / loadarray a
    def visitArrayAccessExpr(self, ctx):
        name = ctx.IDENT().getText()
        self.emit(f"load {name}")        # nacitaj pole na zasobnik
        self.visit(ctx.expression())     # nacitaj index na zasobnik
        self.emit(f"loadarray {name}")   # vezmi pole a index, vrat hodnotu

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
            self.visit(l); self.visit(r)
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
        left = ctx.expression(0)
        right = ctx.expression(1)

        # EXTENSION: array assign — a[i] = value
        # Generuje: hodnota / load a / index / savearray a / load a / index / loadarray a
        # Na konci musime nechat hodnotu na zasobniku (ExprStmt ju potom popne)
        if isinstance(left, PLCParser.ArrayAccessExprContext):
            name = left.IDENT().getText()
            self.visit(right)                          # hodnota na zasobnik
            if self.needs_itof.get(id(ctx), False):
                self.emit("itof")
            self.emit(f"load {name}")                  # nacitaj pole
            self.visit(left.expression())              # index na zasobnik
            self.emit(f"savearray {name}")             # uloz do pola
            # Nechaj hodnotu na zasobniku — rovnako ako normalne priradenie
            self.emit(f"load {name}")                  # nacitaj pole
            self.visit(left.expression())              # index na zasobnik
            self.emit(f"loadarray {name}")             # nacitaj hodnotu spat
            return

        # Normalne priradenie
        self.visit(right)
        if self.needs_itof.get(id(ctx), False):
            self.emit("itof")
        name = left.IDENT().getText()
        self.emit(f"save {name}")
        self.emit(f"load {name}")


# ===========================================================================
# VYSVETLENIE PRE OBHAJOBU
# ===========================================================================
# Co robi CodeGenerator?
#   Prechádza strom (uz skontrolovany TypeCheckerom) a generuje instrukcie.
#   emit() prida jednu instrukciu — ako napisat krok receptu.
#   VM potom instrukcie vykona.
#
# visitArrayDeclStmt — pre "int a[10];"
#   emit("createarray a 10") — vytvor pole menom 'a' s 10 prvkami
#   createarray uz ulozi pole priamo do vars — save a nie je potrebne
#
# visitArrayAccessExpr — pre "a[1]" (citanie)
#   emit("load a")           — daj pole na zasobnik
#   visit(index)             — daj index (1) na zasobnik
#   emit("loadarray a")      — vezmi pole a index, vrat hodnotu
#
# visitAssignExpr pre pole — pre "a[1] = 5"
#   visit(right)             — daj hodnotu (5) na zasobnik
#   emit("load a")           — daj pole na zasobnik
#   visit(index)             — daj index (1) na zasobnik
#   emit("savearray a")      — uloz hodnotu do pola na index
#   potom znova load a / index / loadarray a — nechaj hodnotu na zasobniku
#   (ExprStmt ju potom popne cez pop)
#
# new_label() — vrati unikatne cislo pre skoky v if/while
# ===========================================================================