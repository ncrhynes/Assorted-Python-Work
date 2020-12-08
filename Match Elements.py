'''
L is sublist of N in a different order.
Returns a list of elements that are in L but retain the order in N.
'''
def matchElements(L, N):
    M = []
    for i in range(len(N)):
        n = N[i]
        if n in L:
            M.append(n)
    return M

L = [1, 2, 3, 4]
N = [4, 2, 5, 7, 8, 3, 1]

print(matchElements(L, N))
    
