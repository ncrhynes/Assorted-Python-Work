import random

def generateBracket(L):
    M = []
    N = len(L)
    if N%2 == 1:
       c = random.randint(0, N-1)
       by = L.pop(c)
       N -= 1
       M.append(by)
    random.shuffle(L)
    for i in range(int(N/2)):
        x = L.pop()
        y = L.pop()
        M.append((x, y))
    return M
    
L = ["Violet", "Pigeon", "Zoro", "Zairres", "Nayra", "Kira", "Kaitlyn", "Timothy"]

print(generateBracket(L))
