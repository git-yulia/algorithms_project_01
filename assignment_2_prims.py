# Analysis of Algorithms
# Assignment 2: Prim's Algorithm 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018 

import sys 
import random 

# Prim's algorithm for constructing MCSTs grows trees in a natural way, 
# starting from an arbitrary root. 
# At each stage, it adds a new branch to the already-constructed tree T. 
# The algorithm stops when all nodes have been reached. 

# Initialize our graph using our edge weights 
graph = [ [0,2,3,0,0],
          [2,0,0,1,8],
          [3,0,0,1,0],
          [0,1,1,0,2],
          [0,8,0,2,0]
]

# Initialize V using all the vertices from the graph. 
vertices = ["v1","v2","v3","v4","v5"]

# Initialize T, an empty tree that will later become our MCST. 
tree = []

# Initialize B using v, an arbitrary vertex of V (all the vertices). 
# B is a min-priority queue B
# keeps track of all the vertices NOT in the tree T 
# uses: min weight of any edge connecting vertex to t 
# infinity if no edge exists 
B = [] 

# pick the arbitrary root to use as our starting point 
starting_node = random.randint(0, (len(vertices) - 1))
print("Starting Prim's algorithm at arbitrary root", vertices[starting_node])

# while B is not empty:
