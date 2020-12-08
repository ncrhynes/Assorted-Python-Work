import time

def numSections(a, b):
    L = []
    prod = a*b
    p = b
    q = a
    k = 0
    while k <= prod:
        L.append(k)
        k += p
    #print(L)
    k = q
    while k < prod:
        if k not in L:
            L.append(k)
        k += q
    L.sort()
    #print(L)
    return len(L)-1

def numSecConj(a, b):
    return a + b - gcdDiv(a, b)

def gcdDiv(x, y):
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    if y < 0:
        y *= -1
    return y
'''
t1 = time.time()
'''
max = 51
numTrue = 0
numTries = 0
prevTuples = []
for i in range(1, max):
    for j in range(1, max):
        c1 = i
        c2 = j
        if c2 < c1:
            c1, c2 = c2, c1
        t = (c1, c2)
        if t not in prevTuples:
            a = numSections(i, j)
            b = numSecConj(i, j)
            if a == b:
                numTrue += 1
            numTries += 1
            print("(", i, ",", j, ") |", a, "|", b, "|", a == b)
            prevTuples.append(t)
'''
t2 = time.time()
T1 = t2-t1
print(numTrue)
print(numTries)
print(T1, "s")
t1 = time.time()


max = 101
numTrue = 0
numTries = 0
prevTuples = []
for i in range(1, max):
    for j in range(1, max):
        c1 = i
        c2 = j
        if c2 < c1:
            c1, c2 = c2, c1
        t = (c1, c2)
        if t not in prevTuples:
            a = numSections(i, j)
            b = numSecConj(i, j)
            if a == b:
                numTrue += 1
            numTries += 1
            prevTuples.append(t)

t2 = time.time()
T2 = t2-t1
print(T2, "s")
print(T1-T2, "s faster")
'''
print(numTrue)
print(numTries)
if numTrue == numTries:
            print("Success!")



            
