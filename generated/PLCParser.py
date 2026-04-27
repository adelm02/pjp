# Generated from /Users/adelamartynkova/Downloads/PJP_PR/plc/grammar/PLC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,
        1,1,1,1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,1,1,5,1,
        54,8,1,10,1,12,1,57,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,83,
        8,1,11,1,12,1,84,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,103,8,1,10,1,12,1,106,9,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,119,8,1,11,1,12,1,120,1,1,1,1,1,1,
        1,1,1,1,4,1,128,8,1,11,1,12,1,129,1,1,1,1,1,1,1,1,1,1,3,1,137,8,
        1,1,2,1,2,1,2,1,2,3,2,143,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,154,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,188,8,3,10,3,12,3,191,9,3,1,4,1,4,1,4,1,4,3,4,
        197,8,4,1,4,0,1,6,5,0,2,4,6,8,0,5,1,0,10,11,1,0,12,14,2,0,10,10,
        15,16,1,0,17,18,1,0,19,20,235,0,13,1,0,0,0,2,136,1,0,0,0,4,142,1,
        0,0,0,6,153,1,0,0,0,8,196,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,
        0,16,17,5,0,0,1,17,1,1,0,0,0,18,137,5,1,0,0,19,20,3,4,2,0,20,25,
        5,44,0,0,21,22,5,2,0,0,22,24,5,44,0,0,23,21,1,0,0,0,24,27,1,0,0,
        0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,
        5,1,0,0,29,137,1,0,0,0,30,31,5,29,0,0,31,36,5,44,0,0,32,33,5,2,0,
        0,33,35,5,44,0,0,34,32,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,137,5,1,0,0,40,41,5,30,0,
        0,41,46,3,6,3,0,42,43,5,2,0,0,43,45,3,6,3,0,44,42,1,0,0,0,45,48,
        1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,
        49,50,5,1,0,0,50,137,1,0,0,0,51,55,5,3,0,0,52,54,3,2,1,0,53,52,1,
        0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,
        55,1,0,0,0,58,137,5,4,0,0,59,60,5,26,0,0,60,61,5,5,0,0,61,62,3,6,
        3,0,62,63,5,6,0,0,63,66,3,2,1,0,64,65,5,27,0,0,65,67,3,2,1,0,66,
        64,1,0,0,0,66,67,1,0,0,0,67,137,1,0,0,0,68,69,5,28,0,0,69,70,5,5,
        0,0,70,71,3,6,3,0,71,72,5,6,0,0,72,73,3,2,1,0,73,137,1,0,0,0,74,
        75,5,38,0,0,75,76,5,44,0,0,76,77,5,43,0,0,77,137,5,1,0,0,78,79,5,
        36,0,0,79,82,5,44,0,0,80,81,5,2,0,0,81,83,3,6,3,0,82,80,1,0,0,0,
        83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,
        1,0,0,87,137,1,0,0,0,88,89,5,40,0,0,89,90,5,5,0,0,90,91,3,6,3,0,
        91,92,5,1,0,0,92,93,3,6,3,0,93,94,5,1,0,0,94,95,3,6,3,0,95,96,5,
        6,0,0,96,97,3,2,1,0,97,137,1,0,0,0,98,99,5,37,0,0,99,104,5,44,0,
        0,100,101,5,2,0,0,101,103,5,44,0,0,102,100,1,0,0,0,103,106,1,0,0,
        0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,
        0,107,137,5,1,0,0,108,109,5,38,0,0,109,110,5,44,0,0,110,111,5,2,
        0,0,111,112,3,6,3,0,112,113,5,1,0,0,113,137,1,0,0,0,114,115,5,39,
        0,0,115,118,5,44,0,0,116,117,5,2,0,0,117,119,3,6,3,0,118,116,1,0,
        0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,122,1,0,
        0,0,122,123,5,1,0,0,123,137,1,0,0,0,124,127,5,44,0,0,125,126,5,7,
        0,0,126,128,3,6,3,0,127,125,1,0,0,0,128,129,1,0,0,0,129,127,1,0,
        0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,1,0,0,132,137,1,0,
        0,0,133,134,3,6,3,0,134,135,5,1,0,0,135,137,1,0,0,0,136,18,1,0,0,
        0,136,19,1,0,0,0,136,30,1,0,0,0,136,40,1,0,0,0,136,51,1,0,0,0,136,
        59,1,0,0,0,136,68,1,0,0,0,136,74,1,0,0,0,136,78,1,0,0,0,136,88,1,
        0,0,0,136,98,1,0,0,0,136,108,1,0,0,0,136,114,1,0,0,0,136,124,1,0,
        0,0,136,133,1,0,0,0,137,3,1,0,0,0,138,143,5,31,0,0,139,143,5,32,
        0,0,140,143,5,33,0,0,141,143,5,34,0,0,142,138,1,0,0,0,142,139,1,
        0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,5,1,0,0,0,144,145,6,3,
        -1,0,145,146,5,5,0,0,146,147,3,6,3,0,147,148,5,6,0,0,148,154,1,0,
        0,0,149,150,7,0,0,0,150,154,3,6,3,11,151,154,3,8,4,0,152,154,5,44,
        0,0,153,144,1,0,0,0,153,149,1,0,0,0,153,151,1,0,0,0,153,152,1,0,
        0,0,154,189,1,0,0,0,155,156,10,10,0,0,156,157,7,1,0,0,157,188,3,
        6,3,11,158,159,10,9,0,0,159,160,7,2,0,0,160,188,3,6,3,10,161,162,
        10,8,0,0,162,163,7,3,0,0,163,188,3,6,3,9,164,165,10,7,0,0,165,166,
        7,4,0,0,166,188,3,6,3,8,167,168,10,6,0,0,168,169,5,21,0,0,169,188,
        3,6,3,7,170,171,10,5,0,0,171,172,5,22,0,0,172,188,3,6,3,6,173,174,
        10,4,0,0,174,175,5,23,0,0,175,176,3,6,3,0,176,177,5,24,0,0,177,178,
        3,6,3,4,178,188,1,0,0,0,179,180,10,3,0,0,180,181,5,25,0,0,181,188,
        3,6,3,3,182,183,10,12,0,0,183,184,5,8,0,0,184,185,3,6,3,0,185,186,
        5,9,0,0,186,188,1,0,0,0,187,155,1,0,0,0,187,158,1,0,0,0,187,161,
        1,0,0,0,187,164,1,0,0,0,187,167,1,0,0,0,187,170,1,0,0,0,187,173,
        1,0,0,0,187,179,1,0,0,0,187,182,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,7,1,0,0,0,191,189,1,0,0,0,192,197,5,
        42,0,0,193,197,5,41,0,0,194,197,5,35,0,0,195,197,5,43,0,0,196,192,
        1,0,0,0,196,193,1,0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,9,1,
        0,0,0,16,13,25,36,46,55,66,84,104,120,129,136,142,153,187,189,196
    ]

class PLCParser ( Parser ):

    grammarFileName = "PLC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'{'", "'}'", "'('", "')'", 
                     "'<<'", "'['", "']'", "'-'", "'!'", "'*'", "'/'", "'%'", 
                     "'+'", "'.'", "'<'", "'>'", "'=='", "'!='", "'&&'", 
                     "'||'", "'?'", "':'", "'='", "'if'", "'else'", "'while'", 
                     "'read'", "'write'", "'int'", "'float'", "'bool'", 
                     "'string'", "<INVALID>", "'fwrite'", "'FILE'", "'fopen'", 
                     "'fappend'", "'for'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELSE", "WHILE", "READ", 
                      "WRITE", "INT_T", "FLOAT_T", "BOOL_T", "STR_T", "BOOL", 
                      "FWRITE", "FILE_T", "FOPEN", "FAPPEND", "FOR", "FLOAT", 
                      "INT", "STRING", "IDENT", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_type = 2
    RULE_expression = 3
    RULE_literal = 4

    ruleNames =  [ "program", "statement", "type", "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    IF=26
    ELSE=27
    WHILE=28
    READ=29
    WRITE=30
    INT_T=31
    FLOAT_T=32
    BOOL_T=33
    STR_T=34
    BOOL=35
    FWRITE=36
    FILE_T=37
    FOPEN=38
    FAPPEND=39
    FOR=40
    FLOAT=41
    INT=42
    STRING=43
    IDENT=44
    COMMENT=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLCParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)


        def getRuleIndex(self):
            return PLCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184170765354) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PLCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FwriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FWRITE(self):
            return self.getToken(PLCParser.FWRITE, 0)
        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFwriteStmt" ):
                return visitor.visitFwriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class FileDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILE_T(self):
            return self.getToken(PLCParser.FILE_T, 0)
        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PLCParser.IDENT)
            else:
                return self.getToken(PLCParser.IDENT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileDeclStmt" ):
                return visitor.visitFileDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class FappendV2StmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFappendV2Stmt" ):
                return visitor.visitFappendV2Stmt(self)
            else:
                return visitor.visitChildren(self)


    class FopenStmt2Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOPEN(self):
            return self.getToken(PLCParser.FOPEN, 0)
        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def STRING(self):
            return self.getToken(PLCParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStmt2" ):
                return visitor.visitFopenStmt2(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PLCParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(PLCParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(PLCParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(PLCParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(PLCParser.WRITE, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class FopenStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOPEN(self):
            return self.getToken(PLCParser.FOPEN, 0)
        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStmt" ):
                return visitor.visitFopenStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(PLCParser.READ, 0)
        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PLCParser.IDENT)
            else:
                return self.getToken(PLCParser.IDENT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(PLCParser.TypeContext,0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PLCParser.IDENT)
            else:
                return self.getToken(PLCParser.IDENT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStmt" ):
                return visitor.visitDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(PLCParser.FOR, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)

        def statement(self):
            return self.getTypedRuleContext(PLCParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)


    class FappendV1StmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FAPPEND(self):
            return self.getToken(PLCParser.FAPPEND, 0)
        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFappendV1Stmt" ):
                return visitor.visitFappendV1Stmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PLCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = PLCParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(PLCParser.T__0)
                pass

            elif la_ == 2:
                localctx = PLCParser.DeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.type_()
                self.state = 20
                self.match(PLCParser.IDENT)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 21
                    self.match(PLCParser.T__1)
                    self.state = 22
                    self.match(PLCParser.IDENT)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(PLCParser.T__0)
                pass

            elif la_ == 3:
                localctx = PLCParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(PLCParser.READ)
                self.state = 31
                self.match(PLCParser.IDENT)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 32
                    self.match(PLCParser.T__1)
                    self.state = 33
                    self.match(PLCParser.IDENT)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(PLCParser.T__0)
                pass

            elif la_ == 4:
                localctx = PLCParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.match(PLCParser.WRITE)
                self.state = 41
                self.expression(0)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 42
                    self.match(PLCParser.T__1)
                    self.state = 43
                    self.expression(0)
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 49
                self.match(PLCParser.T__0)
                pass

            elif la_ == 5:
                localctx = PLCParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(PLCParser.T__2)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184170765354) != 0):
                    self.state = 52
                    self.statement()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(PLCParser.T__3)
                pass

            elif la_ == 6:
                localctx = PLCParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.match(PLCParser.IF)
                self.state = 60
                self.match(PLCParser.T__4)
                self.state = 61
                self.expression(0)
                self.state = 62
                self.match(PLCParser.T__5)
                self.state = 63
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 64
                    self.match(PLCParser.ELSE)
                    self.state = 65
                    self.statement()


                pass

            elif la_ == 7:
                localctx = PLCParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.match(PLCParser.WHILE)
                self.state = 69
                self.match(PLCParser.T__4)
                self.state = 70
                self.expression(0)
                self.state = 71
                self.match(PLCParser.T__5)
                self.state = 72
                self.statement()
                pass

            elif la_ == 8:
                localctx = PLCParser.FopenStmt2Context(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.match(PLCParser.FOPEN)
                self.state = 75
                self.match(PLCParser.IDENT)
                self.state = 76
                self.match(PLCParser.STRING)
                self.state = 77
                self.match(PLCParser.T__0)
                pass

            elif la_ == 9:
                localctx = PLCParser.FwriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.match(PLCParser.FWRITE)
                self.state = 79
                self.match(PLCParser.IDENT)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 80
                    self.match(PLCParser.T__1)
                    self.state = 81
                    self.expression(0)
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 86
                self.match(PLCParser.T__0)
                pass

            elif la_ == 10:
                localctx = PLCParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 88
                self.match(PLCParser.FOR)
                self.state = 89
                self.match(PLCParser.T__4)
                self.state = 90
                self.expression(0)
                self.state = 91
                self.match(PLCParser.T__0)
                self.state = 92
                self.expression(0)
                self.state = 93
                self.match(PLCParser.T__0)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(PLCParser.T__5)
                self.state = 96
                self.statement()
                pass

            elif la_ == 11:
                localctx = PLCParser.FileDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 98
                self.match(PLCParser.FILE_T)
                self.state = 99
                self.match(PLCParser.IDENT)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 100
                    self.match(PLCParser.T__1)
                    self.state = 101
                    self.match(PLCParser.IDENT)
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self.match(PLCParser.T__0)
                pass

            elif la_ == 12:
                localctx = PLCParser.FopenStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 108
                self.match(PLCParser.FOPEN)
                self.state = 109
                self.match(PLCParser.IDENT)
                self.state = 110
                self.match(PLCParser.T__1)
                self.state = 111
                self.expression(0)
                self.state = 112
                self.match(PLCParser.T__0)
                pass

            elif la_ == 13:
                localctx = PLCParser.FappendV1StmtContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 114
                self.match(PLCParser.FAPPEND)
                self.state = 115
                self.match(PLCParser.IDENT)
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 116
                    self.match(PLCParser.T__1)
                    self.state = 117
                    self.expression(0)
                    self.state = 120 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 122
                self.match(PLCParser.T__0)
                pass

            elif la_ == 14:
                localctx = PLCParser.FappendV2StmtContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 124
                self.match(PLCParser.IDENT)
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.match(PLCParser.T__6)
                    self.state = 126
                    self.expression(0)
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break

                self.state = 131
                self.match(PLCParser.T__0)
                pass

            elif la_ == 15:
                localctx = PLCParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 133
                self.expression(0)
                self.state = 134
                self.match(PLCParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeFloatContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_T(self):
            return self.getToken(PLCParser.FLOAT_T, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFloat" ):
                return visitor.visitTypeFloat(self)
            else:
                return visitor.visitChildren(self)


    class TypeBoolContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_T(self):
            return self.getToken(PLCParser.BOOL_T, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBool" ):
                return visitor.visitTypeBool(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_T(self):
            return self.getToken(PLCParser.INT_T, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeInt" ):
                return visitor.visitTypeInt(self)
            else:
                return visitor.visitChildren(self)


    class TypeStringContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR_T(self):
            return self.getToken(PLCParser.STR_T, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeString" ):
                return visitor.visitTypeString(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = PLCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = PLCParser.TypeIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(PLCParser.INT_T)
                pass
            elif token in [32]:
                localctx = PLCParser.TypeFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(PLCParser.FLOAT_T)
                pass
            elif token in [33]:
                localctx = PLCParser.TypeBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(PLCParser.BOOL_T)
                pass
            elif token in [34]:
                localctx = PLCParser.TypeStringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.match(PLCParser.STR_T)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdentExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class CharAtExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharAtExpr" ):
                return visitor.visitCharAtExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(PLCParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcatExpr" ):
                return visitor.visitAddSubConcatExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpr" ):
                return visitor.visitTernaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = PLCParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 145
                self.match(PLCParser.T__4)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(PLCParser.T__5)
                pass
            elif token in [10, 11]:
                localctx = PLCParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.expression(11)
                pass
            elif token in [35, 41, 42, 43]:
                localctx = PLCParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.literal()
                pass
            elif token in [44]:
                localctx = PLCParser.IdentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(PLCParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PLCParser.MulDivExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 156
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 157
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = PLCParser.AddSubConcatExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 159
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 99328) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = PLCParser.RelExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 162
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = PLCParser.EqExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 165
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = PLCParser.AndExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 168
                        self.match(PLCParser.T__20)
                        self.state = 169
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = PLCParser.OrExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 171
                        self.match(PLCParser.T__21)
                        self.state = 172
                        self.expression(6)
                        pass

                    elif la_ == 7:
                        localctx = PLCParser.TernaryExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 174
                        self.match(PLCParser.T__22)
                        self.state = 175
                        self.expression(0)
                        self.state = 176
                        self.match(PLCParser.T__23)
                        self.state = 177
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = PLCParser.AssignExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 180
                        self.match(PLCParser.T__24)
                        self.state = 181
                        self.expression(3)
                        pass

                    elif la_ == 9:
                        localctx = PLCParser.CharAtExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 183
                        self.match(PLCParser.T__7)
                        self.state = 184
                        self.expression(0)
                        self.state = 185
                        self.match(PLCParser.T__8)
                        pass

             
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatLitContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PLCParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLit" ):
                return visitor.visitFloatLit(self)
            else:
                return visitor.visitChildren(self)


    class IntLitContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PLCParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLit" ):
                return visitor.visitIntLit(self)
            else:
                return visitor.visitChildren(self)


    class BoolLitContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(PLCParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLit" ):
                return visitor.visitBoolLit(self)
            else:
                return visitor.visitChildren(self)


    class StringLitContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PLCParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLit" ):
                return visitor.visitStringLit(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = PLCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                localctx = PLCParser.IntLitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(PLCParser.INT)
                pass
            elif token in [41]:
                localctx = PLCParser.FloatLitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(PLCParser.FLOAT)
                pass
            elif token in [35]:
                localctx = PLCParser.BoolLitContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(PLCParser.BOOL)
                pass
            elif token in [43]:
                localctx = PLCParser.StringLitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(PLCParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         




