import math, time

def pairSum5(n):
    if n%2 == 0:
        n = int(n/2)
        T = 5**n
        t = pairSum5(n)
        a = t[0]*t[1]*2
        b = int(math.sqrt((T-a)*(T+a)))
        return (a, b)
    else:
        T = 5**n
        for a in range(1, T):
            b = math.sqrt(T - a**2)
            if b.is_integer() and a%5 != 0:
                return (a, int(b))

def pairSum5_V1(n):
    T = 5**n
    for a in range(1, T):
        b = math.sqrt(T - a**2)
        if b.is_integer() and a%5 != 0:
            return (a, int(b))
 
t1i = time.time()
for i in range(1, 21):
    t = pairSum5_V1(i)
    print("5^"+str(i), " = ", str(t[0])+"^2 + "+str(t[1])+"^2")
t1f = time.time()
print(int((t1f-t1i)*100)/100, "seconds")

t2i = time.time()   
for i in range(1, 21):
    t = pairSum5(i)
    print("5^"+str(i), " = ", str(t[0])+"^2 + "+str(t[1])+"^2")
t2f = time.time()
print(int((t2f-t2i)*100)/100, "seconds")

"""
for i in range(10):
    print(pairSum5(64))
"""
