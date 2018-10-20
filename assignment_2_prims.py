# Analysis of Algorithms
# Assignment 2: Prim's Algorithm
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018

import sys
import random
import math

HIGHEST_PRIORITY = 0
INFINITY = math.inf 

# Prim's algorithm for constructing MCSTs grows trees in a natural way,
# starting from an arbitrary root.
# At each stage, it adds a new branch to the already-constructed tree T.
# The algorithm stops when all nodes have been reached.

graph = [
    #A  B  C  D  E  F  G 
    [0, 2, 3, 0, 0, 0, 0], # A
    [2, 0, 1, 1, 4, 0, 0], # B
    [3, 1, 0, 0, 0, 5, 0], # C
    [0, 1, 0, 0, 1, 0, 0], # D
    [0, 4, 0, 1, 0, 1, 0], # E
    [0, 0, 5, 0, 1, 0, 1], # F
    [0, 0, 0, 0, 0, 1, 0]  # G
]

# Initialize V using all the vertices from the graph.
vertices = ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]


class vertex:
    "Contains vertex and information about cheapest edges connected to it"

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.name = vertices[vertex_number]
        self.key = INFINITY

    def get_name(self):
        return self.name

    "get_key: returns the cost of the cheapest edge connected to this vertex"
    def get_key(self):
        return self.key

    def set_key(self, value):
        self.key = value

    "get_adjacent_vertices: returns a list of all vertices connected to this one "
    "automatically updates the key value"
    def get_adjacent_vertices(self):
        adjacent_vertices = []

        key = INFINITY

        for index in range(len(vertices)):
            if graph[self.vertex_number][index] != 0:
                adjacent_vertices.append(index)

        return adjacent_vertices

class min_priority_queue:
    "Contains information and methods for dealing with B, our heap structure"

    def __init__(self, size_of_heap):
        self.size = size_of_heap
        self.contents = [vertex(index) for index in range(self.size)]

    "pop: removes front element at index 0 which is lowest cost, highest priority"

    def pop_minimum(self):
        popped_item = self.contents[0]
        self.contents.remove(popped_item)
        self.size = self.size - 1
        return popped_item

    "push: appends element to the back, lowest priority"

    "contains: checks B for existence of desired vertex"

    def contains(self, vertex):
        found = False

        index = 0
        while (found == False) and (index < self.size):
            if self.contents[index].name == vertices[vertex]:
                found = True
            index = index + 1

        return found

    def update_key(self, vertex_number, new_key_value):
        print("Trying to set key for ", vertex_number, "to", new_key_value)
        self.contents[vertex_number].set_key(new_key_value)


# Initialize T, an empty tree that will later become our MCST.
T = []

# pick the arbitrary root to use as our starting point
# starting_node = random.randint(0, (len(vertices) - 1))
starting_node = 0
print("Starting Prim's algorithm at arbitrary root", vertices[starting_node])

# create an array parents[] of size V and fill it with NULL
parents = [(-1) for index in range(len(vertices))]

# create a min heap of size V. let the min heap be B[]
B = min_priority_queue(len(vertices))

# make starting vertex's key 0 for now
B.contents[0].set_key(0)

#___________________________________________________________________________________________________________

# For this assignment we will be calling u the current_vertex and v the next_vertex to not get them confused. 

# while not B.isEmpty():
while B.size != 0:
    current_vertex = B.pop_minimum()
    print("current_vertex = ", vertices[current_vertex.vertex_number])
    
    for next_vertex in current_vertex.get_adjacent_vertices():
        new_cost = current_vertex.get_weight(next_vertex)



"""
        for nextVert in currentVert.getConnections():
          newCost = currentVert.getWeight(nextVert)
          if nextVert in B and newCost<nextVert.getDistance():
              nextVert.setPred(currentVert)
              nextVert.setDistance(newCost)
              B.decreaseKey(nextVert,newCost)
"""