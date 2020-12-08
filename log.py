import math, random, time

def log(b, x):
    U = 1
    k = 0
    L = 1
    j = 0
    #Find upper
    while U < x:
        k += 1
        U = b**k
    #find lower bound
    while L > x:
        j -= 1
        L = b**j
   
    #print([j, k])
    #print(U)
    #print(x)
    #print(abs(U-x))
    i = ((k+j)/2)
    M = b**i
    a = -2
    if x >= 1:
        while abs(U - x) > 10**(a):
            U = b**k
            L = b**j
            if x >= M:
                j = i
            else:
                k = i
            i = ((k+j)/2)
            M = b**i
            #print([j, k])
        return k
    else:
        while abs(L-x) > 10**a:
            U = b**k
            L = b**j
            if x >= M:
                j = i
            else:
                k = i
            i = ((k+j)/2)
            M = b**i
            #print([j, k])
        return j
    

def compare():
    k = 4
    t1 = time.time()
    for i in range(1, 10**k):
        math.log(i, 2)
    t2 = time.time()
    T1 = t2-t1
    print("Official time:", T1)
    t1 = time.time()
    for i in range(1, 10**k):
        log(2, i)
    t2 = time.time()
    T2 = t2-t1
    print("My time:", T2)
    print("Ratio is:", T2/T1)

#compare()

b = 2
k = log(b, 1000)
#print(b**k)

