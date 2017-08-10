# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

import itertools, re, string
# My solution
'''
def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    times = 1
    strResult = ""
    while word:
        if not word[0].isupper():
            strResult += word[0]
            word = word[1:]
            continue
        
        i = 0
        while i<len(word) and word[i].isupper():
            i = i + 1
        strUpperWord = word[0:i]
        strThisWord = ""
        for j in range(len(strUpperWord)):
            strThisWord += str(10**(len(strUpperWord)-j-1)) + "*" + strUpperWord[j] +  (" + " if j < len(strUpperWord) - 1 else "")
        
        strResult += strThisWord
        word = word[i:]
        
    return strResult
'''

# Norvig's solution
def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word
    
def faster_solve(formula):
    """Given a formula line 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula, True)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass
        
def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. For example, 'YOU == ME**2' returns 
    (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters
        
if __name__=="__main__":
    print faster_solve('ODD + ODD == EVEN') # Here we must use "==" instead of "=", otherwise it will return an error