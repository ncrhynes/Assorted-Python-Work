def gcdDiv(x, y):
    step = 0
    if x < y:
        x, y = y, x
    while x%y != 0:
        #print("x =", x, ", y =", y)
        q = x//y
        print(x, "=", y, "*", q, "+", x-y*q)
        x, y = y, x%y
        step += 1
    q = x//y
    print(x, "=", y, "*", q, "+", x-y*q)
    step+=1
    print(step, "step(s)")
    if y < 0:
        y *= -1
    return y
#Does NOT work with negatives!

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    if y < 0:
        y *= -1
    return y


def gcdSub(x, y):
    step = 0
    while x != y:
        print("x =", x, ", y =", y)
        if 0 < x < y:
            x, y = y, x
        x, y = y, x - y
        step += 1
    print(step, " step(s)")
    if x < 0:
        x *= -1
    return x

def extEA(a, b, P):
    g = gcd(a, b)
    if a < b:
        a, b = b, a
    A = a
    B = b
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while b != g:
        q = a//b
        r = a - b*q
        x0, x1 = x1, x0 - q*x1
        y0, y1 = y1, y0 - q*y1
        if P:
            print(A, "*", x1,"+", B, "*", y1, "=", r)
        a, b = b, r
    return [x1, y1]

"""
a = 61358
b = 2090
print("GCF = ", gcdDiv(a, b))
"""
'''
print("______________________")
print("GCF = ", gcdSub(a, b))
'''
#print(gcdDiv(3.5, 4.6))
print(extEA(11, 13, True))
