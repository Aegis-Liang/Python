# JavaScript: Comments & Keywords
#
# In this exercise you will write token definition rules for all of the
# tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and
# STRING. In addition, you will handle // end of line comments
# as well as /* delimited comments */. 
#
# We will assume that JavaScript is case sensitive and that keywords like
# 'if' and 'true' must be written in lowercase. There are 26 possible
# tokens that you must handle. The 'tokens' variable below has been 
# initialized below, listing each token's formal name (i.e., the value of
# token.type). In addition, each token has its associated textual string
# listed in a comment. For example, your lexer must convert && to a token
# with token.type 'ANDAND' (unless the && is found inside a comment). 
#
# Hint 1: Use an exclusive state for /* comments */. You may want to define
# t_comment_ignore and t_comment_error as well. 

import ply.lex as lex

def test_lexer(lexer,input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result

tokens = (
    'ANDAND',       # &&
    'COMMA',        # ,
    'DIVIDE',       # /
    'ELSE',         # else
    'EQUAL',        # =
    'EQUALEQUAL',   # ==
    'FALSE',        # false
    'FUNCTION',     # function
    'GE',           # >=
    'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
'IF',           # if
'LBRACE',       # {
'LE',           # <=
'LPAREN',       # (
'LT',           # <
'MINUS',        # -
'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
'OROR',         # ||
'PLUS',         # +
'RBRACE',       # }
'RETURN',       # return
'RPAREN',       # )
'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem. 
'TIMES',        # *
'TRUE',         # true
'VAR',          # var
)

#
# Write your code here. 
#


t_ignore = ' \t\v\r' # whitespace 


    
def t_comment1(t):
    r'//[^\n]*?\n'
    
# This regular expression is tricky, cannot use [] here
def t_comment2(t):
    r'/\*(?:\n|.)*?\*/'  

    
def t_andand(t):
    r'&&'
    t.type = 'ANDAND'
    return t

def t_oror(t):
    r'\|\|'
    t.type = 'OROR'
    return t

def t_comma(t):
    r','
    t.type = 'COMMA'
    return t

def t_divide(t):
    r'/'
    t.type = 'DIVIDE'
    return t

def t_else(t):
    r'else'
    t.type = 'ELSE'
    return t

def t_equalequal(t):
    r'=='
    t.type = 'EQUALEQUAL'
    return t

def t_ge(t):
    r'>='
    t.type = 'GE'
    return t

def t_le(t):
    r'<='
    t.type = 'LE'
    return t

def t_gt(t):
    r'>'
    t.type = 'GT'
    return t

def t_lt(t):
    r'<'
    t.type = 'LT'
    return t

def t_equal(t):
    r'='
    t.type = 'EQUAL'
    return t

def t_false(t):
    r'false'
    t.type = 'FALSE'
    return t

def t_true(t):
    r'true'
    t.type = 'TRUE'
    return t

def t_function(t):
    r'function'
    t.type = 'FUNCTION'
    return t

def t_if(t):
    r'if'
    t.type = 'IF'
    return t

def t_lbrace(t):
    r'{'
    t.type = 'LBRACE'
    return t

def t_rbrace(t):
    r'}'
    t.type = 'RBRACE'
    return t

def t_lparen(t):
    r'\('
    t.type = 'LPAREN'
    return t

def t_rparen(t):
    r'\)'
    t.type = 'RPAREN'
    return t

def t_minus(t):
    r'-'
    t.type = 'MINUS'
    return t

def t_plus(t):
    r'\+'
    t.type = 'PLUS'
    return t

def t_not(t):
    r'!'
    t.type = 'NOT'
    return t

def t_return(t):
    r'return'
    t.type = 'RETURN'
    return t

def t_semicolon(t):
    r';'
    t.type = 'SEMICOLON'
    return t

def t_times(t):
    r'\*'
    t.type = 'TIMES'
    return t

def t_var(t):
    r'var'
    t.type = 'VAR'
    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character " + t.value[0]
    t.lexer.skip(1)
    
    
# Offical Answer for comment:
states = (
    ('comment', 'exclusive')
)

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')
    
def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_comment_error(t):
    t.lexer.skip(1)
    
def t_eolcomment(t):
    r'//.*'
    pass
    

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own. 

lexer = lex.lex() 

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1)
print test_lexer(input1) == output1
print ''

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2)
print test_lexer(input2) == output2