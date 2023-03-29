from sly import Lexer
from tabulate import tabulate


class SymbolTable:
    def __init__(self) -> None:
        self.table = {}


class CalcLexer(Lexer):
    # Set of token names.   This is always required
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

    # reserved = [
    #     "def",
    #     "if",
    #     "int",
    #     "float",
    #     "string",
    #     "break",
    #     "int_constant",
    #     "float_constant",
    #     "string constant",
    #     "null",
    #     "read",
    #     "return",
    #     "for",
    #     "print",
    #     "new",
    #     "else",
    # ]

    # String containing ignored characters between tokens
    ignore = " \t \n"

    # Regular expression rules for tokens

    # ID
    IDENT = r"[a-z][a-zA-Z0-9_]*"
    FLOAT_CONSTANT = r"[0-9]+\.[0-9]+"
    INT_CONSTANT = r"[0-9]+"
    STRING_CONSTANT = r"\'[a-zA-Z0-9_ ]*\'"
    COMMENT = r"#[^\n]*"

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
    COMMA_POINT = r";"

    # Reserved words
    # #reserved = {'def', 'if', 'int', 'float', 'string', 'break', 'null', 'read', 'return', 'for', 'print', 'new', 'else'
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


def main():
    f = open("test", "r")
    n = f.readlines()
    st = SymbolTable()

    tokens = []
    for i in range(0, len(n)):
        print(n[i])

        data = n[i]
        lexer = CalcLexer()

        for tok in lexer.tokenize(data):
            print("type=%r, value=%r, index = %r" % (tok.type, tok.value, tok.index))

            if tok.type != "COMMENT":
                if tok.type == "IDENT":
                    st.table.setdefault(tok.value, []).append(
                        (i + 1, tok.index + 1)
                    )
                tokens.append([tok.value, tok.type])

    print(tabulate([(k, v) for k, v in st.table.items()], headers=["nome", "ocorrencias"]))
    print(tabulate(tokens, headers=["lexema", "padrao"]))

if __name__ == "__main__":
    main()
