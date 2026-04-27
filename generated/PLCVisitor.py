# Generated from /Users/adelamartynkova/Downloads/PJP_PR/plc/grammar/PLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLCParser import PLCParser
else:
    from PLCParser import PLCParser

# This class defines a complete generic visitor for a parse tree produced by PLCParser.

class PLCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLCParser#program.
    def visitProgram(self, ctx:PLCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#EmptyStmt.
    def visitEmptyStmt(self, ctx:PLCParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#DeclStmt.
    def visitDeclStmt(self, ctx:PLCParser.DeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ReadStmt.
    def visitReadStmt(self, ctx:PLCParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#WriteStmt.
    def visitWriteStmt(self, ctx:PLCParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#BlockStmt.
    def visitBlockStmt(self, ctx:PLCParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IfStmt.
    def visitIfStmt(self, ctx:PLCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#WhileStmt.
    def visitWhileStmt(self, ctx:PLCParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FopenStmt2.
    def visitFopenStmt2(self, ctx:PLCParser.FopenStmt2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FwriteStmt.
    def visitFwriteStmt(self, ctx:PLCParser.FwriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ForStmt.
    def visitForStmt(self, ctx:PLCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FileDeclStmt.
    def visitFileDeclStmt(self, ctx:PLCParser.FileDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FopenStmt.
    def visitFopenStmt(self, ctx:PLCParser.FopenStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FappendV1Stmt.
    def visitFappendV1Stmt(self, ctx:PLCParser.FappendV1StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FappendV2Stmt.
    def visitFappendV2Stmt(self, ctx:PLCParser.FappendV2StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ExprStmt.
    def visitExprStmt(self, ctx:PLCParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TypeInt.
    def visitTypeInt(self, ctx:PLCParser.TypeIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TypeFloat.
    def visitTypeFloat(self, ctx:PLCParser.TypeFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TypeBool.
    def visitTypeBool(self, ctx:PLCParser.TypeBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TypeString.
    def visitTypeString(self, ctx:PLCParser.TypeStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AndExpr.
    def visitAndExpr(self, ctx:PLCParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IdentExpr.
    def visitIdentExpr(self, ctx:PLCParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#RelExpr.
    def visitRelExpr(self, ctx:PLCParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:PLCParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#OrExpr.
    def visitOrExpr(self, ctx:PLCParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AssignExpr.
    def visitAssignExpr(self, ctx:PLCParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#CharAtExpr.
    def visitCharAtExpr(self, ctx:PLCParser.CharAtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:PLCParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#EqExpr.
    def visitEqExpr(self, ctx:PLCParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:PLCParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AddSubConcatExpr.
    def visitAddSubConcatExpr(self, ctx:PLCParser.AddSubConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ParenExpr.
    def visitParenExpr(self, ctx:PLCParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TernaryExpr.
    def visitTernaryExpr(self, ctx:PLCParser.TernaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IntLit.
    def visitIntLit(self, ctx:PLCParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FloatLit.
    def visitFloatLit(self, ctx:PLCParser.FloatLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#BoolLit.
    def visitBoolLit(self, ctx:PLCParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#StringLit.
    def visitStringLit(self, ctx:PLCParser.StringLitContext):
        return self.visitChildren(ctx)



del PLCParser