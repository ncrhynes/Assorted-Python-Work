import random

R = []

for i in range(6):
    for j in range(6):
        R.append(str(i+1) + "R" + str(j+1) + "Y")
        
def main():
    S = list(R)
    random.shuffle(S)
    loop = True
    while loop == True:
        t = input()
        if t == "end":
            break
        if not S:
            S = list(R)
            random.shuffle(S)
        roll = S.pop()
        print(roll)
        print(int(roll[0])+int(roll[2]))
        print(len(S), "rolls remaining.")

main()
        
    



