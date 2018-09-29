# Analysis of Algorithms
# Assignment 1 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Problem 1.9(c), Euclid's Extended Algorithm 

import sys 
import random
import numpy as np
import matplotlib.pyplot as plt

m = 0
n = 0

# This step acquires inputs while verifying that the algorithm's PRE-CONDITIONS are being met. 
while (m <= 0): m = int(input("Please input an integer greater than 0: "))
while (n <= 0): n = int(input("And just one more, please: "))

# Implementation of Euclid's Extended Algorithm
def get_euclids_extended(m, n): 
    a = 0  
    x = 1  
    b = 1  
    y = 0  
    c = m   
    d = n    
    iterations = 0

    while(True):
        q = int(c / d)   
        r = c % d
        iterations += 1

        if (r == 0):
            return (int(d),int(a),int(b), int(iterations))

        c = d
        d = r
        t = x
        x = a
        a = (t - (q * a))
        t = y
        y = b
        b = (t - (q * b))

def plotResults(xvals, yvals):
    plt.title("Iterations as a function of encoding length for Euclid's Extended Algorithm")
    plt.xlabel("Encoding length (in bits)")
    plt.ylabel("Average iterations")
    plt.plot(xvals, yvals)
    plt.show()

# Function to run trials and get average runtime (in iterations)
def runEuclidsExtended(maxBitLength, runsPerLength): 
    lengths = []
    results = []
    avg = 0;
    for bitlength in range(1, maxBitLength):
        lengths.append(bitlength)
        for i in range(0, runsPerLength):
            smallNum = 0
            bigNum = 0
            while(smallNum <= 0): smallNum = random.getrandbits(bitlength)
            while(bigNum <= 0): bigNum = random.getrandbits(150) # size is bounded by the smaller one, so guarantee the smaller one is smallNum
            avg += get_euclids_extended(bigNum, smallNum)[3]
        results.append(avg / runsPerLength)
    plotResults(lengths, results)

results = get_euclids_extended(m,n)
print("GCD: ", results[0])
print("Coefficients x and y: ", results[1], ", ", results[2])

runEuclidsExtended(15, 1)


# Make sure that the POST-CONDITION requirements were met 
# Euclid's extended algorith, given integers m and n, should return (a,b): 
#       a*m + b*n = gcd(m, n)
# It should also return gcd(m, n)
