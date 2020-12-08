import random

def main():
    Vals = []
    Perms = []
    N = 6
    P = [i for i in range(1, N+1)]
    runs = fact(N)
    Matches = []
    #matches = 0
    runCheck = 0
    numPerms = 0 
    while numPerms <runs:
        runCheck +=1
        random.seed()
        #print("Before:", Perms)
        K = newPerm(P)
        #print(K)
        #print(Perms)
        #print("After:", Perms)
        if K not in Perms:
            numPerms += 1
            '''
            if numPerms%10000 == 0:
                print(numPerms)
            '''
            #print("Before:", Perms)
            Perms.append(K)
            #print("After:", Perms)
            #print(K)
            val = Exp(K)
            #print(val)
            if val not in Vals:
                Vals.append(val)
            else:
                print("Match found!")
                pos = Vals.index(val)
                Matches.append([K, Perms[pos]])
                print(K, "has same value as", Perms[pos])
                #matches += 1
    print(sorted(Vals))
    minVal = min(Vals)
    maxVal = max(Vals)
    m = Vals.index(minVal)
    M = Vals.index(maxVal)
    print(minVal, "at", Perms[m])
    print(maxVal, "at", Perms[M])
    print(numPerms, "unique permutations")
    print(runCheck, "attempts")
    print(len(Matches), "matches found")
    
            

def U(L): #fractional method
    sum = 0
    for i in range(len(L)-1):
        sum += L[i+1]/L[i]
    return sum

def R(L): #factorial method
    sum = 0
    for i in range(len(L)):
        #print(fact(i+1)*L[i])
        sum += fact(i+1)*L[i]
    return sum

def Exp(L): #power method
    sum = 0
    n = len(L)
    for i in range(n):
        #print((n**(n-i-1)))
        sum += L[i]*(n**(n-i-1))
    return sum

def newPerm(L):
    R = list(L)
    random.shuffle(R)
    #print(L)
    return R

def fact(x):
    if x == 1 or x == 0:
        return 1
    return fact(x-1)*x

main()
'''
print(U([3, 7, 8, 2, 9, 10, 5, 4, 1, 6]))
print(U([1, 10, 9, 8, 4, 5, 3, 6, 2, 7]))
'''
'''
for i in range(10):
    N = 4
    L = [i for i in range(1, N+1)]
    random.shuffle(L)
    print(L)
    print(R(L))
'''
#R([1, 2, 3, 4, 5])
#R([5, 4, 3, 2, 1])
#print(Exp([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#print(Exp([9-i for i in range(10)]))
#print(Exp([3, 2, 1]))
