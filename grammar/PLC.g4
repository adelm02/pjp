grammar PLC;

program
    : statement* EOF
    ;

statement
    : ';'                                                                    # EmptyStmt
    | type IDENT (',' IDENT)* ';'                                            # DeclStmt
    | 'read' IDENT (',' IDENT)* ';'                                          # ReadStmt
    | 'write' expression (',' expression)* ';'                               # WriteStmt
    | '{' statement* '}'                                                     # BlockStmt
    | 'if' '(' expression ')' statement ('else' statement)?                  # IfStmt
    | 'while' '(' expression ')' statement                                   # WhileStmt



    // --------------
    // EXTENSION: Pondělí
    // fopen f "soubor.txt"
    //   FILE / open / fwrite N
    // --------------
    | 'fopen' IDENT STRING ';'                                              # FopenStmt2
    | 'fwrite' IDENT (',' expression)+ ';'                                  # FwriteStmt



    // --------------
    // EXTENSION: for cycle (Vašínek)
    //   for (init; cond; step) statement
    //   - init and step are expressions, cond must be bool.
    //   - Behaves like the equivalent while loop.
    // --------------
    | 'for' '(' expression ';' expression ';' expression ')' statement       # ForStmt

    // --------------
    // EXTENSION: FILE / fopen / fappend
    //  fopen f, "soubor.txt";
    //   Two syntactic variants of fappend coexist; pick one in your project:
    //     V1 (Běhálek):  fappend f, v1, v2, ... ;          // file is consumed
    //     V2 (Vašínek):  f << v1 << v2 << ... ;            // file kept, then pop
    // --------------
    | 'FILE' IDENT (',' IDENT)* ';'                                          # FileDeclStmt
    | 'fopen' IDENT ',' expression ';'                                       # FopenStmt
    | 'fappend' IDENT (',' expression)+ ';'                                  # FappendV1Stmt
    | IDENT ('<<' expression)+ ';'                                           # FappendV2Stmt

    | expression ';'                                                         # ExprStmt
    ;

type
    : 'int'    # TypeInt
    | 'float'  # TypeFloat
    | 'bool'   # TypeBool
    | 'string' # TypeString
    ;

// Expression rules ordered from highest to lowest precedence so that ANTLR4
// resolves the precedence climbing automatically. Right-associative ones
// (assignment, ternary) are marked with <assoc=right>.
expression
    : '(' expression ')'                                              # ParenExpr

    // --------------
    // EXTENSION: charAt — postfix string indexing  s[i]
    //   String × int -> string (single character).
    //   Highest precedence so a[i]+b parses as (a[i])+b.
    // --------------
    | expression '[' expression ']'                                   # CharAtExpr

    | op=('-' | '!') expression                                       # UnaryExpr
    | expression op=('*' | '/' | '%') expression                      # MulDivExpr
    | expression op=('+' | '-' | '.') expression                      # AddSubConcatExpr
    | expression op=('<' | '>') expression                            # RelExpr
    | expression op=('==' | '!=') expression                          # EqExpr
    | expression '&&' expression                                      # AndExpr
    | expression '||' expression                                      # OrExpr

    // --------------
    // EXTENSION: ternary operator  cond ? a : b
    //   Right-associative; binds tighter than '=' but looser than '||'.
    //   cond must be bool; a and b must share a numeric/common type.
    // --------------
    | <assoc=right> expression '?' expression ':' expression          # TernaryExpr

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

// Keywords (must come before IDENT)
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
FWRITE  : 'fwrite' ;

// EXTENSION keywords (FILE / fopen / fappend / for)
FILE_T  : 'FILE' ;
FOPEN   : 'fopen' ;
FAPPEND : 'fappend' ;
FOR     : 'for' ;

// Literals
FLOAT  : [0-9]+ '.' [0-9]+ ;
INT    : [0-9]+ ;
STRING : '"' (~["\\] | '\\' .)* '"' ;

IDENT  : [a-zA-Z][a-zA-Z0-9]* ;

// Comments are bounded by two slashes and the end of the line.
COMMENT : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;
