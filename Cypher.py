def modPowerConvert(x):
    x = x%26
    x = (x**5)%26
    return x

#def convert(str):
    

A = [chr(64+n) for n in range(1, 27)]
B = []

for i in range(26):
    x = chr(65+modPowerConvert(i))
    B.append(x)
    print(A[i]+"|"+str(x))

print(B)

for i in range(26):
    if(A[i] in B):
        B.remove(A[i])

print(B)
print(len(B))
