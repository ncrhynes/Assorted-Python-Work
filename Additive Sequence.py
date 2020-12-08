import matplotlib.pyplot as plt

def addSeq(a, b, n):
    L = []
    L.append(a)
    L.append(b)
    for i in range(2, n):
        L.append(L[i-1] + L[i-2])
    return L

def fibSeq(n):
    return addSeq(0, 1, n)

def fibSeqRat(n):
    L = fibSeq(n)
    M = []
    for i in range(n-2):
        M.append(L[i+2]/L[i+1])
    return M
    
def listMod(L, n):
    for i in range(len(L)):
        L[i] = L[i]%n
    return L

def elementFlag(L, n):
    M = []
    for i in range(len(L)):
        if L[i] == n:
            M.append(i)
    return M

def berSeq(n): #CHECK NAME
    return addSeq(1, 3, n)

def histogram(L, bin):
    plt.hist(L, bin)
    plt.show()

histogram(listMod(fibSeq(10000), 10), 10)

#print(addSeq(4, 5, 20))
#print(fibSeqRat(100))
'''
for i in range(2, 13):
    print(i)
    print(elementFlag(listMod(fibSeq(1000), i), 0))
'''
