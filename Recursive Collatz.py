L = []

def CC_r(n, L):
    while n%2 == 0:
        n = n/2
    L.append(int(n))
    if n == 1:
        return L
    else:
        return CC_r(3*n + 1, L)

print(CC_r(31, L))
        
        
    
