# Analysis of Algorithms
# Assignment 2: Prim's Algorithm 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018 

import sys 
import random 
import math 

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

class vertex:
    'Contains vertex and information about cheapest edges connected to it'

    def __init__(self, vertex_number, cheapest_edge_cost):
       self.vertex_number = vertex_number
       self.name = vertices[vertex_number]
       self.cheapest_edge_cost = cheapest_edge_cost
       
    def get_name(self):
        return self.name

    def get_key(self):
        return self.cheapest_edge_cost

    def find_cheapest_edge(self):
        return 0 



# Initialize T, an empty tree that will later become our MCST. 
tree = []

# pick the arbitrary root to use as our starting point 
# starting_node = random.randint(0, (len(vertices) - 1))
starting_node = 0 
print("Starting Prim's algorithm at arbitrary root", vertices[starting_node])

# pseudocode:
#____________________________________________________________________

# create an array parents[] of size V and fill it with NULL
parents = [None for index in range(len(vertices))]

# create a min heap of size V. let the min heap be B[]
B = [None for index in range(len(vertices))]

for new_vertex in range(len(B)):
    B[new_vertex] = vertex(new_vertex, math.inf) 
    print("added", B[new_vertex].name)



# while B is not empty: 
while(len(B) != 0):

#   a) u (a vertex) = get min(B)
    u = B.pop()
    print("(",u.name,",", u.cheapest_edge_cost,")")

#   b) for every adjacent v of u:
#           if v is in B:
#               update key value of v in B if weight of edge (u,v) is
#               smaller than current key value of v 
#               parent[v] = u 


