Nadia Hynes - Python portfolio

A collection of python works, all written by me.
These are mostly made for fun, usually to automate or make more efficient a mathematical 
process I find interesting.

[TO REMOVE FROM FINAL GITHUB:
derangements
fuck R
listadd
miranda's swap
modSquare
Name Match (Maybe revisit?)
Neat Code
NP Test
Colours
Power Set
Primes
Print String
Product Average Calc
Recursive Product
Square Spiral
Square Fractal
SquaresLessThan
SquareSum5
]

Highlights:
(Descriptions are below, alphabetized by topic) 

Totient.py

r(n, x).py

GCD.py

Dice.py

Find Inverses.py

PairSum5.py

Permutation to Val.py

Product Set.py - MAYBE

Pure Powers.py

Recursive Sequence.py

Square Sum.py

Number Theory:

Additive Sequence.py - A collection of functions to generate and analyse additive recursive
sequences, like the Fibonacci Sequence.

Collatz.py - A collection of functions to find the path using the Collatz conjecture back to
1 for any natural number.

Cypher.py - A program to test out some ideas I had about a new type of cypher based on
multiplicative modulo groups.

Diophantine.py - A function made to find many specific solutions to Diophantine Equations.

Factor.py - An integer factoring program.

FactorSum.py - Program to find the sum of the factors of an integer.

Find Inverses.py - Find all multiplicative inverses with in the group of integers modulo n.

GCD.py - Compute the GCD of two integers, including the option to show the math a human would 
do by hand to find it.

Happy Numbers.py - Compute whether a number is a happy number base 10.

Identity Tests.py - Function to test many values on a way to calculate integer powers by way
of adding nCr values.

intDiv.py - Practice for recursive functions using the problem of integer division solved 
with multiple methods.

log.py - Method to determine logarithms with binary search, with time comparison to python
default method.

Multisplit Problem.py - Taking a length L and two integers a, b, less than L, L is divided
into sections of length L/a and L/b. This function find how many sections L is cut into.

nCr.py - Including an implementation of nCr, this generates the pascal triangle at any 
desired row.

PairSum5.py - Given k (int), this finds a pair of values a, b such that a^2 + b^2 = 5^k
Uses multiple implementations and contains time testing for many values.
Ex: 5^11  =  2642^2 + 6469^2

Perfect Numbers.py - Finds all perfect numbers up to a given number very efficiently.

Permutation to Val.py - This is a function to turn each possible permutation from a given 
length N into a unique integer. This was used to make cheap bookkeeping for a project on 
using Ant-Colony optimization to solve the Traveling Salesman problem.

Pure Powers.py - This finds every number in a given range of natural numbers that is a pure
power (a number that is a perfect square, perfect cube, etc).

Pythagorean Triples.py - This generates a pythagorean triple for any pair of integers.

Quadratic Number Field.py - This finds units for any positive quadratic number field (an 
extension of the concept of Guassian integers [A+B*i, A, B are integers] to any other root, 
such as A+Bsqrt(5) and finds the numbers that can multiply their conjugate to equal 1.)

r(n, x).py - COME BACK TO THIS!

Recursive Collatz.py - Another implementation of the Collatz Conjecture, but recursive.

Recursive Sequence.py - General program to generate sequences in the form 
x_n = a*x_n-1 + b*x_n-2. Useful for making many integer sequences, like any pure powers, 
the Fibonacci Sequence, or the Bernoulli Sequence.

Square Sum.py - For any N, this finds a pair of coprime numbers A, B such that A^2+B^2=N if
possible. 

toBin.py - Convert an integer to binary.

Totient.py - This contains my best implementation of a factoring function and an
implementation of Euler's Totient function, an important function for number theory. For a 
more thorough explanation and demonstration of its implementation and properties, I prepared
a demonstration function inside.

Statistics:

Avg Dice roll.py - Calculations of average rolls with disadvantage and advantage (D&D terms)

Dice Deck.py - Program to simulate a deck of all dice rolls possible by rolling 2d6, for use 
with games heavily based on rolling these dice. Inspired by frustrations with Catan, where
you can know a particular hex has 5/36 probability of being rolled on each turn, but instead,
this guarantees a roll will come up 5 times every 36 turns.

Dice.py - A long collection of functions I made to facilitate the various rolls that come 
up in D&D.

probNot.py - A function to find the number of times for a situation to occur for the odds of 
it NOT happening once to become less than 50%. 
Ex: If the desired event is rolling a 20 on a 20-sided die, it takes 14 rolls for the odds
of not rolling a 20 in any of those times to become less than 50%.

ProductSet.py - For a given A and B, this program generates a graph of the probabilities of 
rolling 1dA*1dB. 

Stats.py - A collection of functions to compute useful statistical values, made to avoid the 
manual calculations requested for a statistics course assignment.

Other Math: 

Compare.py - Quick function to compare quadratic and exponential functions.

Draw Polygon.py - A program to draw any regular polygon using turtle graphics.

Match Elements.py - With two lists, L and N, this returns a list of elements that are in L 
but retain the order in N.

Proximity Check - This uses two different methods of evalutating the closeness of two 
constants. Useful for checking approximations for important constants, like how 
17/12 ~= sqrt(2).

Other: 

GenerateBracket.py - Generate a bracket for a knockout tournament.

Split List.py - Given a list L and an element K which is known to be in L, this generates two
lists, one including all elements appearing before K, the other including all elements after
K.