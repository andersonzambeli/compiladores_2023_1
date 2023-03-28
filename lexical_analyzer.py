from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { IDENT, INT_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, COMMENT,
               PLUS, MINUS, TIMES, DIVIDE, RESTDIV, ASSIGN,
               NOTEQ, EQ, BEQ, LEQ, BIG, LES,
               LPAREN, RPAREN, LBRACK, RBRACK, LBRACE, RBRACE,
               DEF, IF, INT, FLOAT, STRING,
               BREAK, NULL,
               READ, RETURN, FOR, PRINT, NEW, ELSE }
    
    #reserved = {'def', 'if', 'int', 'float', 'string', 'break', 'int_constant', 'float_constant', 'string constant', 'null', 'read', 'return', 'for', 'print', 'new', 'else'
                
    # String containing ignored characters between tokens
    ignore = ' \t \n'

    # Regular expression rules for tokens
    
    


    # ID
    IDENT               = r'[a-z][a-zA-Z0-9_]*'
    FLOAT_CONSTANT      = r'[0-9]+.[0-9]+'
    INT_CONSTANT        = r'[0-9]+'
    STRING_CONSTANT     = r'\'[a-zA-Z0-9_ ]*\''
    COMMENT             = r'#[^\n]*'
    

    
    # Comparison Operators
    NOTEQ = r'!='
    EQ    = r'=='
    BEQ   = r'>='
    LEQ   = r'<='
    BIG   = r'>'
    LES   = r'<'

    # Aritimethics Operators
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    RESTDIV = r'%'
    ASSIGN  = r'='

    # Parenthesis, brackets, braces
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK  = r'\['
    RBRACK  = r'\]'
    LBRACE  = r'{'
    RBRACE  = r'}'



    # Reserved words
    # #reserved = {'def', 'if', 'int', 'float', 'string', 'break', 'null', 'read', 'return', 'for', 'print', 'new', 'else'
    IDENT['def'] = DEF
    IDENT['if'] = IF
    IDENT['int'] = INT
    IDENT['float'] = FLOAT
    IDENT['string'] = STRING
    IDENT['break'] = BREAK
    IDENT['null'] = NULL
    IDENT['read'] = READ
    IDENT['return'] = RETURN
    IDENT['for'] = FOR
    IDENT['print'] = PRINT
    IDENT['new'] = NEW
    IDENT['else'] = ELSE

    

    

if __name__ == '__main__':
    f = open('test', 'r')
    n = f.readlines()
    for i in range(0,len(n)):
        print(n[i])
        data = n[i]
        lexer = CalcLexer()
        for tok in lexer.tokenize(data):
            print('type=%r, value=%r' % (tok.type, tok.value))
