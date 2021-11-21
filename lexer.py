import ply.lex as lex

reserved = ('IF', 'ELSE', 'WHILE', 'PRINT',
            'ANDALSO', 'ORELSE', 'NOT')

tokens = reserved + (
    'ID',
    'GREATER',
    'GREATEREQUAL',
    'NOTEQUAL',
    'EQUAL',
    'LESSEQUAL',
    'LESSTHAN',
    'MINUS',
    'PLUS',
    'INTDIV',
    'DIV',
    'MUL',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'INT',
    'FLOAT',
    'STRING',
    'BOOL',
    'SEMI',
    'ASSIGN',
)

t_ASSIGN = r'='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_NOTEQUAL = r'<>'
t_EQUAL = r'=='
t_LESSEQUAL = r'<='
t_LESSTHAN = r'<'
t_MINUS = r'-'
t_PLUS = r'\+'
t_INTDIV = r'div'
t_DIV = r'/'
t_MUL = r'\*'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_ignore = ' \t'


def t_FLOAT(t):
    r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'[0-9]+'
    #r'[-+]?[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
     r'(\"([^\"]|(\\.))*\")|((\'([^\"]|(\\.))*\'))'
     return t

def t_BOOL(t):
    r'True|False'
    return t;

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t
    
def t_error(t):
    error_syntax = 1;
    return

lex.lex()
