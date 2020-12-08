import math

def nCr(n, r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

def pascalTriRow(n):
    L = []
    for i in range(n, -1, -1):
        L.append(nCr(n, i))
    return L

def fullTriangle(n):
    for i in range(n):
        print(pascalTriRow(i))

#print(pascalTriRow(10))
fullTriangle(20)
