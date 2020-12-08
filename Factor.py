import math

'''
def pFactor(n):
    F = []
    for 
'''
def factor(n):
    F = []
    for i in range(1, n+1):
        if n%i == 0:
            F.append(i)
    return F

def primeCheck(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    else:
        c = int(math.sqrt(abs(x)))
        for i in range(3, c+1, 2):
            if x%i == 0:
                return False
        return True
            
print(primeCheck(1117))       
        
