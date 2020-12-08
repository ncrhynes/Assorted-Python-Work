import random

def statRoller():
    L = []
    for i in range(6):
        M = []
        sum = 0
        for j in range(4):
            M.append(random.randint(1, 6))
        M = sorted(M)
        M.reverse()
        M.pop()
        for i in range(3):
            sum += M.pop()
        L.append(sum)
    return sorted(L)

def LSum(L):
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum

def ModSum(L):
    sum = 0
    for i in range(len(L)):
        a = L[i]
        if a%2 == 1:
            a -= 1
        sum += (a-10)/2
    return int(sum)

L = statRoller()
print(L)
print(LSum(L))
print(ModSum(L))
'''
k = 0
c = 1
while True:
    L = statRoller()
    sum = LSum(L)
    
    #print(L)
    #print(sum)
    '''
'''
    k += 1
    if k == c*10**4:
        print(k)
        c += 1
    if sum == 108:
        print(k)
        break
    '''        
