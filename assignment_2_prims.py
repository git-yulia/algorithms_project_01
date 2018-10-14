# Analysis of Algorithms
# Assignment 2: Prim's Algorithm 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018 

import sys 
import random 
import math 

HIGHEST_PRIORITY = 0 

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

    def __init__(self, vertex_number):
       self.vertex_number = vertex_number
       self.name = vertices[vertex_number]
       self.cheapest_edge_cost = math.inf 
       
    def get_name(self):
        return self.name

    'get_key: returns the cost of the cheapest edge connected to this vertex'
    def get_key(self):
        return self.cheapest_edge_cost

    'get_adjacent_vertices: returns a list of all vertices connected to this one'
    def get_adjacent_vertices(self):
        adjacent_vertices = []

        for index in range(len(vertices)):
            if (graph[self.vertex_number][index] != 0):
                adjacent_vertices.append(index)

        return adjacent_vertices 

    def find_cheapest_edge(self):
        self.cheapest_edge_cost = 13
        return self.cheapest_edge_cost

'must include insert, minimum, extract-min, decrease-key'
class min_priority_queue:
    'Contains information and methods for dealing with B, our heap structure' 

    def __init__(self, size_of_heap):
        self.size = size_of_heap
        self.contents = [vertex(index) for index in range(self.size)]

    'pop: removes front element at index 0 which is lowest cost, highest priority'
    def get_minimum(self):
        popped_item = self.contents[0]
        self.contents.remove(popped_item)
        self.size = self.size - 1
        return popped_item

    'push: appends element to the back, lowest priority'

    'contains: checks B for existence of desired vertex'
    def contains(self, vertex):
        found = False 

        index = 0 
        while((found == False) and (index < self.size)):
            if (self.contents[index].name == vertices[vertex]):
                found = True
            index = index + 1

        return found


    

# Initialize T, an empty tree that will later become our MCST. 
tree = []

# pick the arbitrary root to use as our starting point 
# starting_node = random.randint(0, (len(vertices) - 1))
starting_node = 0 
print("Starting Prim's algorithm at arbitrary root", vertices[starting_node])

# create an array parents[] of size V and fill it with NULL
parents = [None for index in range(len(vertices))]

# create a min heap of size V. let the min heap be B[]
B = min_priority_queue(len(vertices))

while(B.size != 0):

    u = B.get_minimum() 

    adjacent_vertices = u.get_adjacent_vertices() 

    for index in range(len(adjacent_vertices)): 
        if B.contains(adjacent_vertices[index]):
            #if graph[u.vertex_number][index] != 0:
            print(graph[u.vertex_number][index])





"""




#           if v is in B:
#               update key value of v in B if weight of edge (u,v) is
#               smaller than current key value of v 
#               parent[v] = u 

"""

