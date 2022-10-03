#COMP1126 Lab 2
#Romario Mclean 620154705
#October 1, 2022

import math

#Question 1
def quadRoots(a, b, c):
    """ this function returns the greater of the two quadratic roots. """

    discriminant = (b**2) - (4*a*c)

    if discriminant > 0:

        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)

        if root1 > root2:
            return root1
        else:
            return root2
    else: print("No real roots")

# Question 2
def perfectSquare(n):
  
    answer = 0
    if n > 0:
        #Use the while loop to find the square root of n
        while answer * answer < n:
            answer = answer + 1

        #Check to see if answer is the sqrt of n
        if answer * answer != n:
            return False
        else:
            return True
    else:
        return False #When n is negative or == 0

#Question 3
def isPrime(number):
    if number > 1 :
        for x in range(2,number):
            if number % x == 0:
                return False
        return True
    else:
        return False

def addPrimes (x):


    primeSum = 0

    for i in range(2,x+1):

        if isPrime (i):
            primeSum = primeSum + i

    return primeSum
