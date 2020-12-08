import math

def facSum(x):
    sum = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            sum += i + x/i
            if i**2 == x:
                sum -= i
    return int(sum)
'''
Not entirely correct if final if statement is commented out.
When x = n^2 for some natural number n, there will be an extra
factor, in that n will be recorded twice.
Keep out for use of most mass factorisations for efficiency.
'''
def factor(x):
    L = [1]
    c = math.sqrt(x)
    for i in range(2, int(c) + 1):
        if(x % i == 0):
            L.append(i)
            L.append(int(x/i))
    if c%1 == 0:
        L = list(set(L))
    L = sorted(L)
    return L

def numFac(x):
    return len(factor(x))

def isPrime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    else:
        c = int(math.sqrt(abs(x)))
        for i in range(3, c+1, 2):
            if x%i == 0:
                return False
        return True

def primeList(n):
    L = []
    for i in range(1, n):
        if isPrime(i):
            L.append(i)
    return L

def primeFac(x):
    L = factor(x)
    for i in range(len(L)):
        if isPrime(L[i]) == False:
            del L[i]
    return L
         
            

#print(numFac(360))

"""
#Max factor set
max = 0
M = []
for i in range(1, 100001):
    hold = len(factor(i))
    if hold > max:
        print(i, ":", hold)
        max = hold
        M.append(i)
print()
print(M)
"""
'''
max = 0
M = []
for i in range(1, 100001):
    hold = facSum(i)/i
    if hold > max:
        print(i, ":", hold)
        max = hold
        M.append(i)
print()
print(M)
'''
#print(factor(123654))
#Efficiency: (n^2+n)sqrt(n)
for i in range(1, 100):
    print(i)
    print(facSum(i))
    print(factor(i))
    print("_______________")
    

