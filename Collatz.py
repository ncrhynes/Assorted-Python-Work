def CC_o(x):
    if x%2 == 1:
        x = 3*x + 1
    while x%2 == 0:
        x /= 2
    return int(x)

def CC_l(x):
    L = []
    L.append(x)
    while x != 1:
        r = CC_o(x)
        L.append(r)
        x = r
    return L

def maxLenUpTo(n):
    M = []
    max = 0
    for i in range(2, n):
        c = len(CC_l(i))
        if c > max:
            M.append(i)
            max = c
            print(i, ":", len(CC_l(i)))
    print(M)

def maxOnPath(x):
    max = 0
    L = CC_l(x)
    for i in range(len(L)):
        current = L[i]
        if current > max:
            max = current
    return max

'''
Following two don't work yet
'''
def listRepeats(L):
    if list(set(L)) == L:
        return False
    else:
        return True
    
def negCycle():
    for i in range(1, 100, 2):
        x = -1*i
        c = 0
        L = []
        while(x <= -1 and not listRepeats(L)):
            L.append(x)
            x = CC_o(x)
            c += 1
        #del L[c-1]
        print(L)

max = 0
n = 200
for i in range(2, n):
    maxL = maxOnPath(i)
    if maxL > max:
        max = maxL        
    print(i, ":", len(CC_l(i)), ":", maxL)
    print(CC_l(i))
print(max) 

#negCycle()
#maxList(1000)
'''
x = 17
print(CC_l(x))
print(len(CC_l(x)))
'''
#input("Press Enter to exit.")
