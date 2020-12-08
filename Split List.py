import random

def listSplitPre(L, n):
    M = []
    for i in range(len(L)):
        if L[i] == n:
            break
        else:
            M.append(L[i])
    return M

def listSplitPost(L, n):
    p = L.index(n)
    M = []
    for i in range(p + 1, len(L)):
        M.append(L[i])
    return M

def lSplit(L, n):
    M = [[], []]
    p = L.index(n)
    for i in range(p):
        M[0].append(L[i])
    for i in range(p+1, len(L)):
        M[1].append(L[i])
    return M

L = [x for x in range(10)]
random.shuffle(L)
print(L)
print(listSplitPre(L, 4))
print(listSplitPost(L, 4))
print(lSplit(L, 4))       
        
    
