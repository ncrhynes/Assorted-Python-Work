L = []

for x in range(1, 1001):
    y = (94-49*x)/37
    if y%1 == 0:
        L.append((x,int(y)))
    y = (94+49*x)/37
    if y%1 ==0:
        L.append((-x, int(y)))

print(L)
