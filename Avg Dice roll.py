def gcfDiv(x, y):
    step = 0
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
        step += 1
    if y < 0:
        y *= -1
    return y

def reduce(n, d):
    g = gcfDiv(n, d)
    n /= g
    d /= g
    if d == 1:
        return str(n)
    return str(int(n))+"/"+str(int(d))

def avgAdvD(n):
    k = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            k += max(i, j)
    return reduce(k, n**2) + " = " + str(k/n**2)

def avgDisD(n):
    k = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            k += min(i, j)
    return reduce(k, n**2) + " = " + str(k/n**2)

for i in range(1, 21):
    a = avgAdvD(i)
    d = avgDisD(i)
    print(str(i) + " | " + a + " | " + d)
    
#print(reduce(30, 24))
