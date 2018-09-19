# Analysis of Algorithms
# Practice Assignment 1
# Author: Julia Maliauka
# Quiz 6 - The Gale-Shapley Algorithm 

"""
Given two sets of size n
    B = {b1, b2, ... , bn} and G = {g1, g2, ... , gn}
Let <i denote the ranking of boy b(i) to a g.
g(i) < g(i) denotes favorites of girls to that specific b. 

Blocking pair definition - 
b is involved with g'
b' is involved with g 
but g prefers b and b prefers g than their current matches. 

A matching M is stable if it contains no blocking pairs. 
"""

stage = 0 

class Boy():
    def __init__(self, name, preferences):
        self.name = name 
        self.preferences = preferences
        self.partner = None

    def elope(self, partner):
        self.partner = partner

class Girl():
    def __init__(self, name, preferences):
        self.name = name 
        self.preferences = preferences
        self.partner = None

    def elope(self, partner):
        self.partner = partner

b1 = Boy("Johnny", [1,2,4,3])
b2 = Boy("Jesse",  [2,3,4,1])
b3 = Boy("Thomas", [4,1,3,2])
b4 = Boy("Connor", [4,3,2,1])

g1 = Girl("Yulia",    [1,2,4,3])
g2 = Girl("Kelly",    [2,1,3,4])
g3 = Girl("Margaret", [1,2,4,3])
g4 = Girl("Avery",    [1,3,4,2])

B = [b1, b2, b3, b4]
G = [g1, g2, g3, g4]
Matches = [] # initialize empty set of matches 

# Finally, the algorithm 
# Stage 1 - Initialization. The first proposal is made...
# b1 chooses his top g and this pairing is added to Matches
