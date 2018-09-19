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

    while(True):
        q = int(c / d)   
        r = c % d

        if (r == 0):
            return (int(a),int(b))

        c = d
        d = r
        t = x
        x = a
        a = (t - (q * a))
        t = y
        y = b
        b = (t - (q * b))

print(get_euclids_extended(m,n))

# Make sure that the POST-CONDITION requirements were met 
# Euclid's extended algorith, given integers m and n, should return (a,b): 
#       a*m + b*n = gcd(m, n)
