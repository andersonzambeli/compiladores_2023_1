import sys

from sly import Lexer
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
        COMMENT,
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

    # Line number tracking
    @_(r"\n+")
    def ignore_newline(self, token):
        self.lineno += token.value.count("\n")
        self.old_index = self.index

    def error(self, token):
        column = self.find_column(token)
        raise Exception(
            f"Line {self.lineno}, Column: {column}: Bad character {token.value[0]}"
        )

    def find_column(self, token):
        last_cr = self.text.rfind("\n", 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column


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
        for token in lexer.tokenize(code):
            # print(token)
            if token.type == "IDENT":
                print(token.lineno, token.value, token.index - lexer.old_index)
                symbol_table[token.value]["ocurrence"].append((token.lineno, token.index - lexer.old_index))
        print(symbol_table)


if __name__ == "__main__":
    main()
