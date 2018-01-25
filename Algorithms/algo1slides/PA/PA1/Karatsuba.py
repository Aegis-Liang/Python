

def Karatsuba():
    return int('3') * int('4')

def multi(strA, strB):
    lenA = len(strA)
    lenB = len(strA)
    if lenA == 1 and lenB == 1:
        return str(int(strA) * int(strB))
    
    a, b = split(strA)
    c, d = split(strB)
    
def split(strX):
    lenX = len(strX)
    if lenX == 1:
        return '0', strX
    

if __name__ == "__main__":
    A = 3141592653589793238462643383279502884197169399375105820974944592
    B = 2718281828459045235360287471352662497757247093699959574966967627
    strA = str(A)
    strB = str(B)
    
    #print Karatsuba()
    
    # Base case:
    #strA = '9'
    #strB = '8'
    #print multi(strA, strB)