# Felipe Valentin Nascimento (20100523) e  Anderson Sales Zambeli (20104138).
import sys

from sly import Lexer
from sly import Parser
from tabulate import tabulate
from collections import defaultdict


class CalcLexer(Lexer):
    def __init__(self):
        self.old_index = 0

    # Set of token names.
    tokens = {
        IDENT,
        INT_CONSTANT,
        FLOAT_CONSTANT,
        STRING_CONSTANT,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        RESTDIV,
        ASSIGN,
        NOTEQ,
        EQ,
        BEQ,
        LEQ,
        BIG,
        LES,
        LPAREN,
        RPAREN,
        LBRACK,
        RBRACK,
        LBRACE,
        RBRACE,
        COMMA,
        COMMA_POINT,
        DEF,
        IF,
        INT,
        FLOAT,
        STRING,
        BREAK,
        NULL,
        READ,
        RETURN,
        FOR,
        PRINT,
        NEW,
        ELSE,
        FUNC,
    }

    # String containing ignored characters between tokens
    ignore = " \t"

    # Regular expression definitions
    # ID
    IDENT = r"[a-zA-Z][a-zA-Z0-9_]*"
    FLOAT_CONSTANT = r"[0-9]+\.[0-9]+"
    INT_CONSTANT = r"[0-9]+"
    STRING_CONSTANT = r"\'[a-zA-Z0-9_ ]*\'"
    ignore_comment = r"\#.*"

    # Comparison Operators
    NOTEQ = r"!="
    EQ = r"=="
    BEQ = r">="
    LEQ = r"<="
    BIG = r">"
    LES = r"<"

    # Aritimethics Operators
    PLUS = r"\+"
    MINUS = r"-"
    TIMES = r"\*"
    DIVIDE = r"/"
    RESTDIV = r"%"
    ASSIGN = r"="

    # Parenthesis, brackets, braces
    LPAREN = r"\("
    RPAREN = r"\)"
    LBRACK = r"\["
    RBRACK = r"\]"
    LBRACE = r"{"
    RBRACE = r"}"
    COMMA = r","
    COMMA_POINT = r";"

    # Reserved words
    IDENT["def"] = DEF
    IDENT["if"] = IF
    IDENT["int"] = INT
    IDENT["float"] = FLOAT
    IDENT["string"] = STRING
    IDENT["break"] = BREAK
    IDENT["null"] = NULL
    IDENT["read"] = READ
    IDENT["return"] = RETURN
    IDENT["for"] = FOR
    IDENT["print"] = PRINT
    IDENT["new"] = NEW
    IDENT["else"] = ELSE
    IDENT["func"] = FUNC
    

    # Line number tracking
    @_(r"\n+")
    def ignore_newline(self, token):
        self.lineno += token.value.count("\n")
        self.old_index = self.index

    def error(self, token):
        column = self.find_column(token)
        print(
            f"Erro léxico, Linha {self.lineno}, Coluna: {column}, Carácter inválido: {token.value[0]}"
        )
        exit()

    def find_column(self, token):
        last_cr = self.text.rfind("\n", 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column


class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    start = 'program'

    # Grammar rules and actions
    @_('')
    def empty(self, p):
        pass

    @_('statement')
    def program(self, p):
        return 

    @_('funclist')
    def program(self, p):
        return 
    
    @_('empty')
    def program(self, p):
        return 
    
    @_('funcdef f1')
    def funclist(self, p):
        return 
    
    @_('funclist')
    def f1(self, p):
        return 

    @_('empty')
    def f1(self, p):
        return
    
    @_('DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE')
    def funcdef(self, p):
        return

    @_('INT IDENT f2')
    def paramlist(self, p):
        return
    
    @_('FLOAT IDENT f2')
    def paramlist(self, p):
        return
    
    @_('STRING IDENT f2')
    def paramlist(self, p):
        return
    
    @_('empty')
    def paramlist(self, p):
        return
    
    @_('COMMA paramlist')
    def f2(self, p):
        return
    
    @_('empty')
    def f2(self, p):
        return

    @_('vardecl COMMA_POINT')
    def statement(self, p):
        return
    
    @_('atribstat COMMA_POINT')
    def statement(self, p):
        return

    @_('printstat COMMA_POINT')
    def statement(self, p):
        return
    
    @_('readstat COMMA_POINT')
    def statement(self, p):
        return
    
    @_('returnstat COMMA_POINT')
    def statement(self, p):
        return
    
    @_('ifstat')
    def statement(self, p):
        return
    
    @_('forstat')
    def statement(self, p):
        return
    
    @_('LBRACE statelist RBRACE')
    def statement(self, p):
        return
    
    @_('BREAK COMMA_POINT')
    def statement(self, p):
        return
    
    @_('COMMA_POINT')
    def statement(self, p):
        return

    @_('vardecl COMMA_POINT')
    def statementnoif(self, p):
        return
    
    @_('atribstat COMMA_POINT')
    def statementnoif(self, p):
        return

    @_('printstat COMMA_POINT')
    def statementnoif(self, p):
        return
    
    @_('readstat COMMA_POINT')
    def statementnoif(self, p):
        return
    
    @_('returnstat COMMA_POINT')
    def statementnoif(self, p):
        return
     
    @_('forstat')
    def statementnoif(self, p):
        return
    
    @_('LBRACE statelist RBRACE')
    def statementnoif(self, p):
        return
    
    @_('BREAK COMMA_POINT')
    def statementnoif(self, p):
        return
    
    @_('COMMA_POINT')
    def statementnoif(self, p):
        return
    
    @_('INT IDENT e1')
    def vardecl(self, p):
        return
    
    @_('FLOAT IDENT e1')
    def vardecl(self, p):
        return
    
    @_('STRING IDENT e1')
    def vardecl(self, p):
        return
    
    @_('LBRACK INT_CONSTANT RBRACK e1')
    def e1(self, p):
        return

    @_('empty')
    def e1(self, p):
        return
    
    @_('lvalue ASSIGN f4')
    def atribstat(self, p):
        return
    
    @_('expression')
    def f4(self, p):
        return
    
    @_('allocexpression')
    def f4(self, p):
        return
    
    @_('funccall')
    def f4(self, p):
        return
    
    @_('FUNC IDENT LPAREN paramlistcall RPAREN')
    def funccall(self, p):
        return
    
    @_('IDENT f5')
    def paramlistcall(self, p):
        return
    
    @_('empty')
    def paramlistcall(self, p):
        return
    
    @_('COMMA paramlistcall')
    def f5(self, p):
        return
    
    @_('empty')
    def f5(self, p):
        return
    
    @_('PRINT expression')
    def printstat(self, p):
        return
    
    @_('READ lvalue')
    def readstat(self, p):
        return
    
    @_('RETURN f13')
    def returnstat(self, p):
        return
    
    @_('term')
    def f13(self, p):
        return
    
    @_('empty')
    def f13(self, p):
        return
    
    @_('IF LPAREN expression RPAREN LBRACE statementnoif RBRACE f12')
    def ifstat(self, p):
        return
    
    @_('ELSE LBRACE statement RBRACE')
    def f12(self, p):
        return
    
    @_('empty')
    def f12(self, p):
        return
    
    @_('FOR LPAREN atribstat COMMA_POINT expression COMMA_POINT atribstat RPAREN statement')
    def forstat(self, p):
        return
    
    @_('statement f6')
    def statelist(self, p):
        return
    
    @_('statelist')
    def f6(self, p):
        return
    
    @_('empty')
    def f6(self, p):
        return
    
    @_('NEW f7')
    def allocexpression(self, p):
        return
    
    @_('INT e2')
    def f7(self, p):
        return
    
    @_('FLOAT e2')
    def f7(self, p):
        return
    
    @_('STRING e2')
    def f7(self, p):
        return
    
    @_('LBRACK numexpression RBRACK f8')
    def e2(self, p):
        return
    
    @_('e2')
    def f8(self, p):
        return
    
    @_('empty')
    def f8(self, p):
        return
    
    @_('numexpression f9')
    def expression(self, p):
        return
    
    @_('LES numexpression')
    def f9(self, p):
        return
    
    @_('BIG numexpression')
    def f9(self, p):
        return
    
    @_('LEQ numexpression')
    def f9(self, p):
        return
    
    @_('BEQ numexpression')
    def f9(self, p):
        return
    
    @_('EQ numexpression')
    def f9(self, p):
        return
    
    @_('NOTEQ numexpression')
    def f9(self, p):
        return
    
    @_('empty')
    def f9(self, p):
        return
    
    @_('term e3')
    def numexpression(self, p):
        return
    
    @_('PLUS term e3')
    def e3(self, p):
        return
    
    @_('MINUS term e3')
    def e3(self, p):
        return
    
    @_('empty')
    def e3(self, p):
        return
    
    @_('unaryexpr e4')
    def term(self, p):
        return
    
    @_('TIMES unaryexpr e4')
    def e4(self, p):
        return
    
    @_('DIVIDE unaryexpr e4')
    def e4(self, p):
        return
    
    @_('RESTDIV unaryexpr e4')
    def e4(self, p):
        return
    
    @_('empty')
    def e4(self, p):
        return
    
    @_('factor')
    def unaryexpr(self, p):
        return
    
    @_('PLUS factor')
    def unaryexpr(self, p):
        return
    
    @_('MINUS factor')
    def unaryexpr(self, p):
        return
    
    @_('INT_CONSTANT')
    def factor(self, p):
        return
    
    @_('FLOAT_CONSTANT')
    def factor(self, p):
        return
    
    @_('STRING_CONSTANT')
    def factor(self, p):
        return
    
    @_('NULL')
    def factor(self, p):
        return
    
    @_('lvalue')
    def factor(self, p):
        return
    
    @_('LPAREN numexpression RPAREN')
    def factor(self, p):
        return
    
    @_('IDENT e5')
    def lvalue(self, p):
        return
    
    @_('LBRACK numexpression RBRACK f8')
    def e5(self, p):
        return
    
    @_('empty')
    def e5(self, p):
        return
    
    def error(self, p):
        if p:
            lineno = getattr(p, 'lineno', 0)
            if lineno:
                sys.stderr.write(f'Syntax error at line {lineno}, token={p.type}\n')
                print(self.symstack, "\n")
                sys.exit()
            else:
                sys.stderr.write(f'Syntax error, token={p.type}')
                sys.exit()
        else:
            sys.stderr.write('Parse error in input. EOF\n')
        
    


class SymbolTable:
    def __init__(self):
        self.table = defaultdict(lambda: defaultdict(lambda: []))

    def __repr__(self):
        headers = [
            key for value in self.table.values() for key in ["lexeme", *value.keys()]
        ]
        table = ((k1, *v1.values()) for k1, v1 in self.table.items())
        return tabulate(table, headers, "rounded_grid")

    def __getitem__(self, item):
        return self.table[item]


def main():
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        code = file.read()
        lexer = CalcLexer()
        symbol_table = SymbolTable()
        token_list = []

        for token in lexer.tokenize(code):
            token_list.append([token.value, token.type])

            if token.type == "IDENT":
                symbol_table[token.value]["ocurrence"].append((token.lineno, token.index - lexer.old_index))

        #print("Lista de tokens")
        #print(tabulate(token_list))

        #print("Tabela de símbolos")
        #print(symbol_table)

        parser = CalcParser()
        result = parser.parse(lexer.tokenize(code))
        if (result == None):
            print("Sucesso na análise sintática!!!")
        

if __name__ == "__main__":
    main()
