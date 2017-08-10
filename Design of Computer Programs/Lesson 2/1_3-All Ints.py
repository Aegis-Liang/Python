# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    i = 0
    while True:
        yield (-1)**(i+1) * ((i+1)//2)
        i = i + 1
        
    # Norvig's solution:
    #yield 0
    #i = 0
    #while True:
    #    yield i
    #    yield -i
    #    i = i + 1