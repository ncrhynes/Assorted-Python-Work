#returns True if L contains a number that is not a factor of n, else returns False
def nPres(L, n):
    for x in range(len(L)):
        if L[x]%n != 0:
            return True
    return False

def gcf(x, y):
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    return y

#returns pythagorean triple from arguments in reduced form
def pyTri(a, b):
    L = []
    if b > a:
        b, a = a, b
    c = gcf(a, b)
    a /= c
    b /= c
    L.append(int(a**2+b**2))
    L.append(int(2*a*b))
    L.append(int(abs(a**2-b**2)))
    if a%2 == b%2 == 1:
        L = [int(x/2) for x in L]
    return L

def printTriple(L):
    print(L[0], "^2 = ", L[1], "^2 + ", L[2], "^2", sep = '')

printTriple(pyTri(18, 25))

