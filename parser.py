import ply.yacc as yacc
from lexer import *

variables = {}
stack = [True]

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LESSTHAN', 'LESSEQUAL', 'EQUAL',
     'NOTEQUAL', 'GREATEREQUAL', 'GREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
)

def reviewBooleanExpression(expr):
    if expr is None:
        return None

    if type(expr) is str:
        if len(expr) > 0:
            return True
        else:
            return False

    if expr != 0:
        return True
    else:
        return False

def p_start(p):
    '''
    start : program
    '''
    pass

def p_program(p):
    ''' 
    program : stmt program
            | expr SEMI program
            |
    '''
    pass

def p_expr_binop(p):
    '''
    expr :           expr PLUS expr
                   | expr MINUS expr
                   | expr MUL expr
                   | expr DIV expr
    '''
    if not stack[-1]:
        return
    try:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    except Exception as e:
        raise(Exception('Error at binary operation'))

def p_expr_id(p):
    """
    expr : ID
    """
    if not stack[-1]:
        return

    global variables
    value = variables.get(p[1])
    if value is not None:
        p[0] = value
        return value
    else:
        return None

def p_expr(p):
    '''
    expr : INT
           | FLOAT
           | BOOL
           | STRING
           | 
    '''
    if not stack[-1]:
        return
    p[0] = p[1]

def p_expr_string(p):
    '''
    expr_string : STRING
    '''
    if not stack[-1]:
            return
    p[0] = p[1][1:-1]

def p_expr_id_assign_expr(p):
    """
    expr :  INTDECL ID ASSIGN expr
            | FLOATDECL ID ASSIGN expr 
            | BOOLDECL ID ASSIGN expr 
            | STRINGDECL ID ASSIGN expr_string
            | INTDECL ID ASSIGN expr SEMI 
            | FLOATDECL ID ASSIGN expr SEMI 
            | BOOLDECL ID ASSIGN expr SEMI
            | STRINGDECL ID ASSIGN expr_string SEMI
    """
    if not stack[-1]:
        return
    global variables
    if p[4] is not None:
        variables[p[2]] = p[4]
        p[1] = p[4]

def p_print_stmt(p):
    """
    stmt :  PRINT LPAREN ID RPAREN SEMI
            | PRINT LPAREN STRING RPAREN SEMI
    """
    if not stack[-1]:
        return

    if p[3] is not None:
        if(p[3] in variables):
            print(variables[p[3]])
        elif(type(p[3]) is str):
            print(p[3])
        else:
            raise(Exception('Variable is not declared'))


def p_error(p):
    if p:
        print(p)
        raise(Exception("Syntax error at line '%s' character '%s'" %
              (p.lineno, p.lexpos)))
    else:
        raise(Exception("Syntax error at EOF"))

parser = yacc.yacc()

# File input
lines = []
with open('test.txt') as file:
    lines = file.readlines()

for line in lines:
    yacc.parse(line)
print('Compiled successfully')
