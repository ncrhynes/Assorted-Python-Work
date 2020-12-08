import math

'''
Returns the minimum number of trials required for the probability of an event
NOT occuring to become <=0.5

Input inverse of probability p.
'''

def probNot(p):
    return math.ceil(-1*math.log(2)/math.log(1-1/p))

print(probNot(20/3))


def main():
    for i in range(2, 2001):
        print(i, "|", probNot(i))
       
#main()    
