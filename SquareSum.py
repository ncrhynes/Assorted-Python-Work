import math

def squareSum(x):
    for i in range(1, int(math.sqrt(x)+1)):
        a = math.sqrt(x-i**2)
        if a%1 == 0 and a != 0:
            if gcdDiv(i, a) == 1:
                return (i,int(a))
            #return (i, int(a))

def gcdDiv(x, y):
    step = 0
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    if y < 0:
        y *= -1
    return y

def main():
    for i in range(5, 2001):
    #if i%3 != 0:
        #print(i)
        t = squareSum(i)
        if t != None:
            print(i, "=", str(t[0])+"^2 +", str(t[1])+"^2")

#print(squareSum(52))
main()
