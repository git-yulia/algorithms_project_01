# Analysis of Algorithms
# Assignment 1 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Problem 1.9(c), Euclid's Extended Algorithm 

import sys 

m = 0
n = 0

# This step acquires inputs while verifying that the algorithm's PRE-CONDITIONS are being met. 
while (m <= 0): m = int(input("Please input an integer greater than 0: "))
while (n <= 0): n = int(input("And just one more, please: "))

def get_euclids_extended(m, n): 
    a = 0  
    x = 1  
    b = 1  
    y = 0  
    c = m   
    d = n    

    counter = 1 

    while(True):
        print("phase ", counter)
        q = int(c / d)   
        print("q = ", q)
        r = c % d
        print("r = ", r)

        if (r == 0):
            return (int(a),int(b))

        c = d
        print("c set to ", c)
        d = r
        print("d set to ", d)
        t = x
        print("t set to ", t)
        x = a
        print("x set to ", x)
        a = (t - (q * a))
        print("a set to ", a)
        t = y
        print("t set to ", t)
        y = b
        print("y set to ", y)
        b = (t - (q * b))
        print("b set to ", b)

        counter = counter + 1
        print("\n")

print(get_euclids_extended(m,n))

# Make sure that the POST-CONDITION requirements were met 
# Euclid's extended algorith, given integers m and n, should return (a,b): 
#       a*m + b*n = gcd(m, n)
