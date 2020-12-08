import math

def toBinary(N):
    result = ""
    L = math.floor(math.log(N, 2))
    k = L
    #print(k)
    N -= 2**k
    result += "1"
    k -= 1
    while N > 0:
        #print(k)
        if N >= 2**k:
            N -= 2**k
            result = result + "1"
        else:
            result = result + "0"
        k -= 1
    
    while len(result) < L+1:
        result += "0"
    
    return result

k = 100
P = [2**n for n in range(1, math.ceil(math.log(k)))]
print(P)
for i in range(1, k+1):
    j = 0
    if i in P:
        j += 1
    print(i**2, ":", toBinary(i**2), "|", math.ceil(math.log(i**2, 2))+j, "digits")            
    
        
        
