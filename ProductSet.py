import matplotlib.pyplot as plt

def productSet(a, b):
    L = []
    for i in range(1, a+1):
        for j in range(1, b+1):
            if i*j not in L:
                L.append(i*j)
    L = sorted(L)
    R = [[x, 0] for x in L]
    #print(R)
    for i in range(1, a+1):
        for j in range(1, b+1):
            k = L.index(i*j)
            R[k][1] += 1
    return R

'''
Returns the product with the highest number of ways to multiply to it in the
product set as a 2-element list
'''
def maxkby2L(L):
    maxVal = 0
    maxInd = 0
    for i in range(len(L)):
        T = L[i]
        #print(T[1])
        if T[1] > maxVal:
            maxVal = T[1]
            maxInd = i
            #print(maxVal)
    return L[maxInd]

def findHighest(N):
    B = []
    for i in range(1, N+1):
        K = productSet(i, i)
        l = len(K)
        #print(i, ":", K)
        #print(len(K))
        T = maxkby2L(K)
        if T not in B:
            print(i, ":", len(K))
            print(T)
            B.append(T)
            '''
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        '''
    print(B) 

def graphMultOdds(a, b):
    P = productSet(a, b)
    X = []
    Y = []
    X2 = []
    Y2 = []
    sum = 0
    for i in range(1, a*b+1):
        found = False
        X.append(i)
        for j in range(len(P)):
            if P[j][0] == i:
                Y.append(P[j][1])
                found = True
                Y2.append(P[j][1])
                X2.append(i)
                break
        if not found:
            Y.append(0)
        sum += X[i-1]*Y[i-1]
    print(sum)
    g = gcd(sum, a*b)
    avgNum = sum / g
    avgDom = a*b / g
    avgNum = int(avgNum)
    avgDom = int(avgDom)
    #print(P)
    #print(X)
    #print(Y)
    print(avgNum, "/",avgDom)
    print(X)
    print(Y)
    plt.plot(X, Y)
    #plt.plot(X2, Y2)
    plt.show()

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x%y != 0:
        x, y = y, x%y
    if y < 0:
        y *= -1
    return y

graphMultOdds(4, 7)
#findHighest(300)  

'''
print(productSet(4, 8))
print(productSet(8, 4))
print(len(productSet(4, 8)))
'''
