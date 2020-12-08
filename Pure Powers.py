import math

def pbn(n, p1, p2): #Perfect powers Below N
    sum = int(math.pow(n, 1/p1)+0.000001)
    sum += int(math.pow(n, 1/p2)+0.000001)
    sum -= int(math.pow(n, 1/(p1*p2))+0.000001)
    return sum

#print(pbn(216, 2, 3))

n = 10000
L = [1]
a = 1
for i in range(1, n+1):
    b = pbn(i, 2, 3)
    if b > a:
        print(i, "|", b)
        L.append(i)
    a = b

print(L)
print(len(L))

'''
S = []
for j in range(1, int(math.pow(n, 1/2)+1.00001)):
    S.append(j**2)
for k in range(2, int(math.pow(n, 1/3)+1.00001)):
    S.append(k**3)
S = sorted(S)
print(S)

L = set(L)
S = set(S)
print(len(S))

S = S.difference(L)
S = list(S)
print(S)
'''
