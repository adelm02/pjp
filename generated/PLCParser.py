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
        4,1,38,141,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,42,8,1,10,1,12,1,45,9,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,
        1,55,9,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,85,8,1,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,107,8,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,130,8,3,10,3,12,3,133,9,3,1,4,1,4,1,4,1,4,3,4,139,8,4,1,4,0,
        1,6,5,0,2,4,6,8,0,5,1,0,9,10,1,0,11,13,2,0,9,9,14,15,1,0,16,17,1,
        0,18,19,166,0,13,1,0,0,0,2,84,1,0,0,0,4,90,1,0,0,0,6,106,1,0,0,0,
        8,138,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,
        0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,
        1,1,0,0,0,18,85,5,1,0,0,19,20,3,4,2,0,20,21,5,36,0,0,21,22,5,2,0,
        0,22,23,5,34,0,0,23,24,5,3,0,0,24,25,5,1,0,0,25,85,1,0,0,0,26,27,
        3,4,2,0,27,32,5,36,0,0,28,29,5,4,0,0,29,31,5,36,0,0,30,28,1,0,0,
        0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,
        1,0,0,0,35,36,5,1,0,0,36,85,1,0,0,0,37,38,5,26,0,0,38,43,5,36,0,
        0,39,40,5,4,0,0,40,42,5,36,0,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,
        1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,85,5,1,0,0,
        47,48,5,27,0,0,48,53,3,6,3,0,49,50,5,4,0,0,50,52,3,6,3,0,51,49,1,
        0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,
        53,1,0,0,0,56,57,5,1,0,0,57,85,1,0,0,0,58,62,5,5,0,0,59,61,3,2,1,
        0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,
        1,0,0,0,64,62,1,0,0,0,65,85,5,6,0,0,66,67,5,23,0,0,67,68,5,7,0,0,
        68,69,3,6,3,0,69,70,5,8,0,0,70,73,3,2,1,0,71,72,5,24,0,0,72,74,3,
        2,1,0,73,71,1,0,0,0,73,74,1,0,0,0,74,85,1,0,0,0,75,76,5,25,0,0,76,
        77,5,7,0,0,77,78,3,6,3,0,78,79,5,8,0,0,79,80,3,2,1,0,80,85,1,0,0,
        0,81,82,3,6,3,0,82,83,5,1,0,0,83,85,1,0,0,0,84,18,1,0,0,0,84,19,
        1,0,0,0,84,26,1,0,0,0,84,37,1,0,0,0,84,47,1,0,0,0,84,58,1,0,0,0,
        84,66,1,0,0,0,84,75,1,0,0,0,84,81,1,0,0,0,85,3,1,0,0,0,86,91,5,28,
        0,0,87,91,5,29,0,0,88,91,5,30,0,0,89,91,5,31,0,0,90,86,1,0,0,0,90,
        87,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,5,1,0,0,0,92,93,6,3,-1,
        0,93,94,5,7,0,0,94,95,3,6,3,0,95,96,5,8,0,0,96,107,1,0,0,0,97,98,
        5,36,0,0,98,99,5,2,0,0,99,100,3,6,3,0,100,101,5,3,0,0,101,107,1,
        0,0,0,102,103,7,0,0,0,103,107,3,6,3,10,104,107,3,8,4,0,105,107,5,
        36,0,0,106,92,1,0,0,0,106,97,1,0,0,0,106,102,1,0,0,0,106,104,1,0,
        0,0,106,105,1,0,0,0,107,131,1,0,0,0,108,109,10,9,0,0,109,110,7,1,
        0,0,110,130,3,6,3,10,111,112,10,8,0,0,112,113,7,2,0,0,113,130,3,
        6,3,9,114,115,10,7,0,0,115,116,7,3,0,0,116,130,3,6,3,8,117,118,10,
        6,0,0,118,119,7,4,0,0,119,130,3,6,3,7,120,121,10,5,0,0,121,122,5,
        20,0,0,122,130,3,6,3,6,123,124,10,4,0,0,124,125,5,21,0,0,125,130,
        3,6,3,5,126,127,10,3,0,0,127,128,5,22,0,0,128,130,3,6,3,3,129,108,
        1,0,0,0,129,111,1,0,0,0,129,114,1,0,0,0,129,117,1,0,0,0,129,120,
        1,0,0,0,129,123,1,0,0,0,129,126,1,0,0,0,130,133,1,0,0,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,7,1,0,0,0,133,131,1,0,0,0,134,139,5,
        34,0,0,135,139,5,33,0,0,136,139,5,32,0,0,137,139,5,35,0,0,138,134,
        1,0,0,0,138,135,1,0,0,0,138,136,1,0,0,0,138,137,1,0,0,0,139,9,1,
        0,0,0,12,13,32,43,53,62,73,84,90,106,129,131,138
    ]

class PLCParser ( Parser ):

    grammarFileName = "PLC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'['", "']'", "','", "'{'", "'}'", 
                     "'('", "')'", "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", 
                     "'.'", "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", 
                     "'='", "'if'", "'else'", "'while'", "'read'", "'write'", 
                     "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "WHILE", "READ", "WRITE", "INT_T", "FLOAT_T", "BOOL_T", 
                      "STR_T", "BOOL", "FLOAT", "INT", "STRING", "IDENT", 
                      "COMMENT", "WS" ]

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
    IF=23
    ELSE=24
    WHILE=25
    READ=26
    WRITE=27
    INT_T=28
    FLOAT_T=29
    BOOL_T=30
    STR_T=31
    BOOL=32
    FLOAT=33
    INT=34
    STRING=35
    IDENT=36
    COMMENT=37
    WS=38

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137413789346) != 0):
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


    class ArrayDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(PLCParser.TypeContext,0)

        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def INT(self):
            return self.getToken(PLCParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclStmt" ):
                return visitor.visitArrayDeclStmt(self)
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



    def statement(self):

        localctx = PLCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = PLCParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(PLCParser.T__0)
                pass

            elif la_ == 2:
                localctx = PLCParser.ArrayDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.type_()
                self.state = 20
                self.match(PLCParser.IDENT)
                self.state = 21
                self.match(PLCParser.T__1)
                self.state = 22
                self.match(PLCParser.INT)
                self.state = 23
                self.match(PLCParser.T__2)
                self.state = 24
                self.match(PLCParser.T__0)
                pass

            elif la_ == 3:
                localctx = PLCParser.DeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.type_()
                self.state = 27
                self.match(PLCParser.IDENT)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 28
                    self.match(PLCParser.T__3)
                    self.state = 29
                    self.match(PLCParser.IDENT)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(PLCParser.T__0)
                pass

            elif la_ == 4:
                localctx = PLCParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(PLCParser.READ)
                self.state = 38
                self.match(PLCParser.IDENT)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 39
                    self.match(PLCParser.T__3)
                    self.state = 40
                    self.match(PLCParser.IDENT)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.match(PLCParser.T__0)
                pass

            elif la_ == 5:
                localctx = PLCParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.match(PLCParser.WRITE)
                self.state = 48
                self.expression(0)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 49
                    self.match(PLCParser.T__3)
                    self.state = 50
                    self.expression(0)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(PLCParser.T__0)
                pass

            elif la_ == 6:
                localctx = PLCParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.match(PLCParser.T__4)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137413789346) != 0):
                    self.state = 59
                    self.statement()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(PLCParser.T__5)
                pass

            elif la_ == 7:
                localctx = PLCParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.match(PLCParser.IF)
                self.state = 67
                self.match(PLCParser.T__6)
                self.state = 68
                self.expression(0)
                self.state = 69
                self.match(PLCParser.T__7)
                self.state = 70
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.match(PLCParser.ELSE)
                    self.state = 72
                    self.statement()


                pass

            elif la_ == 8:
                localctx = PLCParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.match(PLCParser.WHILE)
                self.state = 76
                self.match(PLCParser.T__6)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(PLCParser.T__7)
                self.state = 79
                self.statement()
                pass

            elif la_ == 9:
                localctx = PLCParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.expression(0)
                self.state = 82
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = PLCParser.TypeIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(PLCParser.INT_T)
                pass
            elif token in [29]:
                localctx = PLCParser.TypeFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(PLCParser.FLOAT_T)
                pass
            elif token in [30]:
                localctx = PLCParser.TypeBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(PLCParser.BOOL_T)
                pass
            elif token in [31]:
                localctx = PLCParser.TypeStringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 89
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


    class ArrayAccessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(PLCParser.IDENT, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = PLCParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 93
                self.match(PLCParser.T__6)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(PLCParser.T__7)
                pass

            elif la_ == 2:
                localctx = PLCParser.ArrayAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(PLCParser.IDENT)
                self.state = 98
                self.match(PLCParser.T__1)
                self.state = 99
                self.expression(0)
                self.state = 100
                self.match(PLCParser.T__2)
                pass

            elif la_ == 3:
                localctx = PLCParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103
                self.expression(10)
                pass

            elif la_ == 4:
                localctx = PLCParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.literal()
                pass

            elif la_ == 5:
                localctx = PLCParser.IdentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(PLCParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = PLCParser.MulDivExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 108
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 109
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = PLCParser.AddSubConcatExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 112
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 49664) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = PLCParser.RelExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 115
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = PLCParser.EqExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 117
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 118
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = PLCParser.AndExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 121
                        self.match(PLCParser.T__19)
                        self.state = 122
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = PLCParser.OrExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 124
                        self.match(PLCParser.T__20)
                        self.state = 125
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = PLCParser.AssignExprContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 127
                        self.match(PLCParser.T__21)
                        self.state = 128
                        self.expression(3)
                        pass

             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = PLCParser.IntLitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(PLCParser.INT)
                pass
            elif token in [33]:
                localctx = PLCParser.FloatLitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(PLCParser.FLOAT)
                pass
            elif token in [32]:
                localctx = PLCParser.BoolLitContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(PLCParser.BOOL)
                pass
            elif token in [35]:
                localctx = PLCParser.StringLitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 137
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
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




