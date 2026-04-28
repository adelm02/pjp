grammar PLC;

program
    : statement* EOF
    ;

statement
    : ';'                                                                    # EmptyStmt
    | type IDENT '[' INT ']' ';'                                             # ArrayDeclStmt
    | type IDENT (',' IDENT)* ';'                                            # DeclStmt
    | 'read' IDENT (',' IDENT)* ';'                                          # ReadStmt
    | 'write' expression (',' expression)* ';'                               # WriteStmt
    | '{' statement* '}'                                                     # BlockStmt
    | 'if' '(' expression ')' statement ('else' statement)?                  # IfStmt
    | 'while' '(' expression ')' statement                                   # WhileStmt
    | expression ';'                                                         # ExprStmt
    ;

type
    : 'int'    # TypeInt
    | 'float'  # TypeFloat
    | 'bool'   # TypeBool
    | 'string' # TypeString
    ;

expression
    : '(' expression ')'                                              # ParenExpr

    // --------------
    // EXTENSION: array — a[i]
    //   IDENT [ index ] — pristup k prvku pola
    //   prva cast je nazov pola, druha je index (int)
    // --------------
    | IDENT '[' expression ']'                                        # ArrayAccessExpr

    | op=('-' | '!') expression                                       # UnaryExpr
    | expression op=('*' | '/' | '%') expression                      # MulDivExpr
    | expression op=('+' | '-' | '.') expression                      # AddSubConcatExpr
    | expression op=('<' | '>') expression                            # RelExpr
    | expression op=('==' | '!=') expression                          # EqExpr
    | expression '&&' expression                                      # AndExpr
    | expression '||' expression                                      # OrExpr
    | <assoc=right> expression '=' expression                         # AssignExpr
    | literal                                                         # LiteralExpr
    | IDENT                                                           # IdentExpr
    ;

literal
    : INT     # IntLit
    | FLOAT   # FloatLit
    | BOOL    # BoolLit
    | STRING  # StringLit
    ;

// --------------
// Lexer rules
// --------------

IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;
READ    : 'read' ;
WRITE   : 'write' ;
INT_T   : 'int' ;
FLOAT_T : 'float' ;
BOOL_T  : 'bool' ;
STR_T   : 'string' ;
BOOL    : 'true' | 'false' ;

FLOAT  : [0-9]+ '.' [0-9]+ ;
INT    : [0-9]+ ;
STRING : '"' (~["\\] | '\\' .)* '"' ;

IDENT  : [a-zA-Z][a-zA-Z0-9]* ;

COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;

// * = nula nebo více (např. statement*)
// + = jeden nebo více (např. expression+)
// ? = nepovinné (např. ('else' statement)?)
