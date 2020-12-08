import time

def recSeq(a, b, n, x0, x1):
    if n == 0:
        return x0
    elif n == 1:
        return x1
    else:
        return a*recSeq(a, b, n-1, x0, x1)+b*recSeq(a, b, n-2, x0, x1)

def recSeqL(a, b, n, x0, x1):
    L = []
    L.append(x0)
    L.append(x1)
    for i in range(n-1):
        L.append(a*L[-1]+b*L[-2])
    return L

"""
for k in range(5, 45, 5):
    print("*******", k, "*******")
    
    t0 = time.time()
    for i in range(k+1):
        print(recSeq(2, 3, i, 1, 1))
    t1 = time.time()
    print(t1-t0)

    t0 = time.time()
    M = recSeqL(2, 3, k, 1, 1)
    print(M)
    t1 = time.time()
    print(t1-t0)
"""
print("Fibonacci:", recSeqL(1, 1, 20, 1, 1))
print("Powers of 2:", recSeqL(2, 0, 20, 1, 2))
print("Numbers that multiply to be 1 away from each power of 2:", recSeqL(1, 2, 20, 1, 1))
#print("Some neat other thing:", recSeqL(2, 1, 20, 1, 1))
