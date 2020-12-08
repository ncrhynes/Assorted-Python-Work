L = ["A", "D", "G", "J", "M", "P", "S", "V", "Y"]
C = ["B", "E", "H", "K", "N", "Q", "T", "W", "Z"]
R = ["C", "F", "I", "L", "O", "R", "U", "X"]

def code(str):
    S = list(str)
    for i in range(len(S)):
        if S[i] == " ":
            S.remove(" ")
    return S

print(code("The bananas land"))
    
