import math

#Checks the proximity of two constants.
def proxCheckDif(x, y):
    return math.log(2, 1 + abs(x - y))

def proxCheckQuo(x, y):
    if x > y:
        return abs(math.log(2, x/y))

def main():
    a, b = eval(input("Enter the two numbers >0 whose proximities would like to calculate: "))
    print("By difference, score is:", proxCheckDif(a, b))
    print("By quotient, score is:", proxCheckQuo(a, b))

main()


