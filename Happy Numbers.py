def hap(x):
    L = list(str(x))
    x = 0
    for i in range(len(L)):
        x += int(L[i])**2
    return x

def hapL(x):
    L = []
    L.append(x)
    v = hap(x)
    x = v
    L.append(v)
    while v != 4 and v > 1:
        v = hap(x)
        x = v
        L.append(v)
    return L

def isHap(x):
    L = hapL(x)
    if L[-1] == 1:
        return True
    else:
        return False

'''
print(hap(25))
print(hapL(25))
'''
'''
for i in range(1, 201):
    print(i, "|", hapL(i))
'''
L = []
for i in range(1, 10001):
    if isHap(i):
        L.append(i)
print(L)
print(len(L))
