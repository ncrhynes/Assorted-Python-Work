import math
def var(L):
    sum = 0
    n = len(L)
    for i in range(n):
        sum += L[i]
    avg = sum/n
    sum = 0
    for i in range(n):
        sum += (L[i] - avg)**2
    return sum/(n-1)

def stanDev(L):
    return math.sqrt(var(L))

def mean(L):
    sum = 0
    n = len(L)
    for i in range(n):
        sum += L[i]
    return sum/n

def median(L):
    L = sorted(L)
    n = len(L)
    if n%2 == 1:
        return L[int((n-1)/2)]
    else:
        a = int(n/2)
        return (L[a]+L[a-1])/2
    
def addMul(L, elem, n):
    for i in range(n):
        L.append(elem)
    return L

def QLLF():
    #quick long list of floats
    n = 1
    L = []
    while(n != 0):
        n = float(input(""))
        L.append(n)
    return L


L = [3096.79, 3607.14, 3584.78, 3256.73, 3286.95, 2788.97, 2958.56, 3027.64, 2976.7, 3147.04, 3069.44, 3535.94, 3119.75, 3072.45, 2975.42, 3045.6, 3130.37, 3485.87, 3508.62, 4213.49, 3233.1, 3264.95, 3116.21, 2954.5, 3279.18, 3227.24, 2664.38]
L = sorted(L)


'''
print(L)
for i in range(len(L)):
    print(L[i])
print(len(L))
'''
'''  
M = [7.94, 8.292, 4.643, 7.470, 8.882, 7.585, 7.650, 2.412, 6.000, 8.833, 7.470, 5.528, 7.167, 7.571, 4.700, 8.167, 7.822, 7.598, 4.000, 6.231, 7.643, 1.760, 6.419, 9.648, 10.700, 10.580, 9.429, 8.000, 9.585, 9.571, 8.998, 8.333, 8.175, 8.000, 9.333, 9.5000, 9.167, 10.140, 9.999, 10.760, 9.763, 9.410, 9.167, 9.348, 8.167, 3.647, 3.408, 3.936, 7.167, 7.647, 0.530, 6.173, 7.295, 7.295, 8.938, 7.882, 8.353, 5.062, 8.175, 8.235, 7.588, 7.647, 5.237, 7.825, 7.333, 9.167, 7.996, 8.714, 7.833, 4.885, 7.998, 3.820, 5.936, 9.000, 9.500, 6.057, 6.057, 6.938] 
for i in range(len(L)):
    M[i] /= 2
'''
'''
L = [441409.10]
L = addMul(L, 2430.9, 150)
L = addMul(L, 76.2, 9067)
L = addMul(L, 10, 176083)
L = addMul(L, 5, 127346)
'''
'''
print(mean(L))
print(median(L))
print(var(L))
print(stanDev(L))
'''
#print(QLLF())
x = mean(L)
s = stanDev(L)
for i in range(1, 4):
    print(x - i*s, ",", x + i*s)

