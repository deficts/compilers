import ply.lex as lex

reserved = (
    'BOOL',
    'INT',
    'FLOAT',
    'STRING',
    'IF',
    'ELIF',
    'ELSE',
    'WHILE',
    'AND',
    'OR',
    'TRUE',
    'FALSE',
)

tokens = reserved + (
    'ID',
    'INT_CONST',
    'FLOAT_CONST',
    'STRING_CONST',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREATER',
    'GREATER_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
)

literals = [
    '(',
    ')',
    '{',
    '}',
    '+',
    '-',
    '*',
    '/',
    '^',
    '=',
    ';',
]

t_ignore = ' \t'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


t_LESS_THAN = r'<'
t_GREATER = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_INT_CONST = r'-?\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FLOAT_CONST = r'-?((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_STRING_CONST = r'\"([^\\\n]|(\\.))*?\"'

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
