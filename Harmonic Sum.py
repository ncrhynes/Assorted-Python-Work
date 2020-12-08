import time

def harmonicSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/i
    return sum

def harmonicSumFrac(n):
    a=1
    b=1
    for i in range(2, n+1):
        a = a*i+b
        b = b*i
        g = gcdDiv(a, b)
        a /= g
        b /= g
        a = int(a)
        b = int(b)
    return (a, b)

def gcdDiv(x, y):
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    if y < 0:
        y *= -1
    return y

n=2000
'''
for i in range(1, n+1):
    t = harmonicSumFrac(i)
    print(i, ":", harmonicSum(i),"=", str(t[0])+"/"+str(t[1]))
'''
i = 80
print(i)
t1 = time.time()
print(harmonicSum(i))
t2 = time.time()
print("Time1 =", t2-t1)
t1 = time.time()
t = harmonicSumFrac(i)
print(str(t[0])+"/"+str(t[1]))
t2=time.time()
print("Time2 =", t2-t1)
