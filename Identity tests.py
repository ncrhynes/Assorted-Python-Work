import math

def nCr(n, r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

def test(n, c):
    sum = 0
    for i in range(n+1):
        sum += nCr(n, i)*math.pow(c - 1, i)
    return int(sum)
"""
for c in range(2, 12):
    for i in range(30):
        a = int(math.pow(c, i))
        b = test(i, c)
        print(i, "|", a, "|", b, "|", a - b)
"""


#print(nCr(12, 7))
