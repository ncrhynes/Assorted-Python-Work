'''
Returns the highest number of times that x, x-1, and x can be divided by n
while the resultant quotient is a whole number.
Example: r(2, 193) = 6
192 = 3*2**6
193 = 193*2**0
194 = 97*2
'''
def r(n, x):
    val = -1
    L = [-1, 0, 1]
    y = x
    if x in L:
        return "infinity"
    for c in L:
        z = y + c
        curVal = -1
        while z%1 == 0:
            z /= n
            curVal += 1
        if curVal > val:
            val = curVal
    return val

#Returns the lowest natural number p multiplied by a such that r(2, (a*p)) == n
#UNFINSHED, but works for all odd ints
def p2(n, a): 
    b = 1
    c = r(2, (a*b))
    while c < n:
        b = 2**c - b
        #print(b)
        c = r(2, (a*b))
    if c > n:
       while c > n:
           b = 2**(c-1) - b
           #print(b)
           c = r(2, (a*b))
       if b < 0:
           b *= -1
       b = b%(2**(n+1))
    return b

'''
Returns the smallest value of x-1, x, and x+1 when divided by n**(r(n, x))
Example: reduce(2, 193) = 3
192 = 3*2**6
193 = 193*2**0
194 = 97*2**1
reduce(n, x)*(n**r(n,x)) = x+/-1 OR reduce(n, x)*(n**r(n,x)) = x
'''
def q(n, x):
    L = [-1, 0, 1]
    p = r(n, x)
    if x in L:
        return 0
    for c in L:
        k = (x+c)/n**p
        if k - int(k) == 0:
            return int(k)

def s(n, x):
    L = [-1, 0, 1]
    p = r(n, x)
    k = q(n, x)
    return x - k*(n**p)

def listFull(L):
    k = len(L)
    c = 0
    for i in range(k):
        if L[i] != None:
            c += 1
    if c == k:
        return True
    else:
        return False
'''
NOT FINISHED! Do it soon, it seems fun.
'''
def reducList(n, R):
    c = 4 - n
    X = []
    l = len(X)
    Y = []
    i = 5
    if c < 0:
        c = 0
    while l < R or not listFull(X):
        k = q(n, i**2)
        val = r(n, k)
        if l < val:
            while len(X) < val - 1:
                X.append(None)
                Y.append(None)
            X.append(i)
            Y.append(k)
        elif X[val] == None:
            X[val] = i
            Y[val] = k   
        l = len(X)
        i += 2
    return [X, Y]
    
def main():
    a = int(input("Please input the index you wish to use: "))
    b = int(input("Please input the number to analyse: "))
    print(r(a, b))

def main2():
    for b in range(2, 6):
        print(b)
        for a in range(2, 101):
            print(a, ":", r(b, a)) 

def main3():
    c = 25
    print("n =", c) 
    for i in range(2, 100):
        print(i, ":", r(c, i), "|", r(c, i**c))

def main4():
    for i in range(1, 41):
        c = 8*(2**i+(-1)**(i+1))/3+(-1)**i
        d = c**2-400
        print(i, "|", r(2, d))

def main5():
    for j in range(3, 67, 2):
        print("_____")
        print(j)
        print("_____")
        for i in range(2, 17):
            print(i, "|", p2(i, j))

def main6():
    for i in range(2, 33):
        print(i, "|", p2(i, 655321))

#NOT FINISHED
#Consider redesigning so check happens with all preceding values of a. It seems that some could be
#missed by over a higher value and then not returning to it.
def main7():
    a = 3
    p = 2
    val = [None, None]
    while p <= 120:
        b = a**2
        c = q(2, b)
        d = r(2, c)
        if d == p:
            p += 1
            val.append(a)
        a += 2
    print(val)
'''
Prints a list of the products
'''
def productSquarePair(n, max):
    for i in range(2, max):
        print(i, "|", r(n, i**2), "|", q(n, i**2))
        
#main7()
#print(r(8, 417^8))
'''
L = reducList(2, 10)
print(L[0])
print(L[1])
'''
#input("Press enter to close.")
#print(p2(2, 257))
#print(q(2, 2039))
productSquarePair(3, 100)

