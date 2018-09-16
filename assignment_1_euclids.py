# Analysis of Algorithms
# Assignment 1 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Problem 1.9(c), Euclid's Extended Algorithm 

import sys 

m = 0
n = 0

while (m <= 0): m = int(input("Please input an integer greater than 0: "))
while (n <= 0): n = int(input("And just one more, please: "))

def get_euclids_extended(m, n): 
    a = 0
    b = 1
    x = 1
    y = 0
    c = m 
    d = n 

    while(True):
        q = c / d
        r = c % d

        if (r == 0):
            return(a,b)

        c = d
        d = r
        t = x
        x = a
        a = t - (q * a)
        t = y
        y = b
        b = t - (q * b)

print(get_euclids_extended(m,n))

# Make sure that the post-condition requirements were met 

