import ply.lex as lex
from enum import Enum

class LexTypes(Enum):
    INTNUM = 1
    FLOATNUM = 2
    NAME = 3
    INTDCL = 4
    FLOATDCL = 5
    PRINT = 6
    AND_OP = 7
    OR_OP = 8
    BOOL_TRUE = 9
    BOOL_FALSE = 10
    BOOL_DCL = 11
    EQUALS = 12
    NOT_EQUAL = 13
    GREATER_EQUAL = 14
    LESS_EQUAL = 15
    WHILE = 16
    FOR = 17
    IF = 18
    ELIF = 19
    ELSE = 20
    STRING_DCL = 21
    SENTENCE_END = 22

class Lexer:
    literals = ['+', '-', '*', '/', '=', '^', '>', '<', '(', ')', '{', '}', '"']

    reserved = {
        'int': LexTypes.INTDCL.name,
        'float': LexTypes.FLOATDCL.name,
        'print': LexTypes.PRINT.name,
        'and': LexTypes.AND_OP.name,
        'or': LexTypes.OR_OP.name,
        'if': LexTypes.IF.name,
        'elif': LexTypes.ELIF.name,
        'else': LexTypes.ELSE.name,
        'while': LexTypes.WHILE.name,
        'for': LexTypes.FOR.name,
        'string': LexTypes.STRING_DCL.name,
        'bool': LexTypes.BOOL_DCL.name,
        'true': LexTypes.BOOL_TRUE.name,
        'false': LexTypes.BOOL_FALSE.name,
    }

    tokens = [
        LexTypes.INTNUM.name,
        LexTypes.FLOATNUM.name,
        LexTypes.NAME.name,
        LexTypes.NAME.name,
        LexTypes.EQUALS.name,
        LexTypes.NOT_EQUAL.name,
        LexTypes.GREATER_EQUAL.name,
        LexTypes.LESS_EQUAL.name,
        LexTypes.SENTENCE_END.name,
    ] + list(reserved.values())

    t_EQUALS = r'=='
    t_NOT_EQUAL = r'!='
    t_GREATER_EQUAL = r'>='
    t_LESS_EQUAL = r'<='
    t_SENTENCE_END = r';'
    t_ignore = ' \t'

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, LexTypes.NAME.name)
        return t

    def t_FNUMBER(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        t.type = LexTypes.FLOATNUM.name
        return t

    def t_INUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        t.type = LexTypes.INTNUM.name
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def createLexer(self):
        lexer = lex.lex(module=self)
        return lexer
