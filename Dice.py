import random, math, matplotlib.pyplot as plt

def roll(numSides):
    return random.randint(1, numSides)

def rollChoices():
    L = []
    N = 1
    print("Please enter the number of sides for each die to roll.")
    print("Enter 0 when finished.")
    while True:
       N = int(input(""))
       if N == 0:
           break
       L.append(roll(N))
    print(L)

def multDice(quant, sides):
    x = 0
    for i in range(quant):
        x += roll(sides)
    return x

def elvenAccuracy():
    sum = 0
    num = 0
    '''
    for i in range(1, 21):
        x = i
        x0 = i
        for j in range(1, 21):
            y = j
            y0 = j
            if y > x:
                x, y = y, x
            
            for k in range(1, 21):
                y = k
                z0 = k
                if y > x:
                    x, y = y, x
                if x != 20:
                    print("######")
                    print("######")
                    print("######")
                    print("######")
                print(x0, "|", y0, "|", z0)
                if x != 20:
                    print("######")
                    print("######")
                    print("######")
                    print("######")
                num += 1
                sum += x
    '''
    for i in range(1, 21):
        x = i
        for j in range(1, 21):
            y = j
            for k in range(1, 21):
                z = k
                a = min(x, y)
                b = max(a, z)
                num += 1
                sum += b    
    sum /= num
    print(num)
    return sum

'''
Returns the result continually rerolling 1dS and
adding the result if the result is greater than
S - T => probability of reroll is T/(Q*S)
'''
def explode(Q, S, T):
    if T > Q*(S-1):
        return "Infinite"
    sum = 0
    #out = False
    while True:
        R = multDice(Q, S)
        sum += R
        if R <= Q*S - T:
            break
    return sum

def statRoller():
    L = []
    for i in range(6):
        M = []
        sum = 0
        for j in range(4):
            M.append(random.randint(1, 6))
        M = sorted(M)
        M.reverse()
        M.pop()
        for i in range(3):
            sum += M.pop()
        L.append(sum)
    return L

def LSum(L):
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum

def ModSum(L):
    sum = 0
    for i in range(len(L)):
        a = L[i]
        if a%2 == 1:
            a -= 1
        sum += (a-10)/2
    return int(sum)

def rollMultPlayers(N):
    stats = []
    for i in range(N):
        stats = stats + statRoller()
    stats = sorted(stats)
    #print(stats)
    S = [[] for i in range(N)]
    for i in range(N*3):
        #S = []
        S[i%N].append(stats.pop(0))
        S[i%N].append(stats.pop())
    for i in range(N):
        S[i] = sorted(S[i])
        print(S[i])
        print(ModSum(S[i]))  
        
rollMultPlayers(6)
#print(23+multDice(10, 8))
#print(multDice(2, 8)+4+multDice(2, 10)+4+multDice(8, 10))

'''
rollChoices()
input("Press Enter to close.")
'''
"""
for j in range(100):
    c = 0
    s = 10
    q = 9
    for i in range(1, 1000):
        c += multDice(s, q)
    d = c/i
    print(d)
    f = (s+1)*q/2
    print(f)
    print(abs(f-d))
"""
'''
print(multDice(4, 4)*10)
input("Press Enter to exit")
'''
#print(8+multDice(2, 8)+multDice(2, 6)+5*3)
#print(8+2*5+2*4+5*3)
'''
s = 6
q = 2
X = [i for i in range(1, (s-1)*q+1)]
Y = []
for i in range(1, q*(s-1)+1):
    sum = 0
    k = 1000
    for j in range(k):
        val = explode(q, s, i)
        if val == "Infinite":
            print("Threshold too high")
            break
        sum += explode(q, s, i)
    sum /= k
    Y.append(sum)
    print(i, ":", sum) 
plt.plot(X, Y)
plt.show()
'''
