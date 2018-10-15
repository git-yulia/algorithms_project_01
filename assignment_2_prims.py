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

# Initialize our graph using our edge weights
graph = [
    [0, 2, 3, 0, 0],
    [2, 0, 0, 1, 8],
    [3, 0, 0, 1, 0],
    [0, 1, 1, 0, 2],
    [0, 8, 0, 2, 0],
]

# Initialize V using all the vertices from the graph.
vertices = ["v1", "v2", "v3", "v4", "v5"]


class vertex:
    "Contains vertex and information about cheapest edges connected to it"

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.name = vertices[vertex_number]
        self.cheapest_edge_cost = INFINITY

    def get_name(self):
        return self.name

    "get_key: returns the cost of the cheapest edge connected to this vertex"

    def get_key(self):
        return self.cheapest_edge_cost

    def set_key(self, value):
        self.cheapest_edge_cost = value

    "get_adjacent_vertices: returns a list of all vertices connected to this one"

    def get_adjacent_vertices(self):
        adjacent_vertices = []

        for index in range(len(vertices)):
            if graph[self.vertex_number][index] != 0:
                adjacent_vertices.append(index)

        return adjacent_vertices

    def find_cheapest_edge(self):
        self.cheapest_edge_cost = 13
        return self.cheapest_edge_cost


"must include insert, minimum, extract-min, decrease-key"


class min_priority_queue:
    "Contains information and methods for dealing with B, our heap structure"

    def __init__(self, size_of_heap):
        self.size = size_of_heap
        self.contents = [vertex(index) for index in range(self.size)]

    "pop: removes front element at index 0 which is lowest cost, highest priority"

    def get_minimum(self):
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

    def update_key(self, vertex, new_key_value):
        for index in range(len(self.contents)):
            self.contents[index].set_key(new_key_value)


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

iterations = 0
while B.size != 0:

    #                          updates
    #_____________________________________________________________________________
    iterations = iterations + 1
    print("After", iterations, "iterations, here's what we have: \n")
    print("B: ", )

    for index in range(len(B.contents)):
        print("[", index, "]: ", B.contents[index].name)

    print("\nT: ")
    for index in range(len(T)):
        if (T[index] != INFINITY): print("[", index, "]: ", vertices[T[index]])


    print("\nparents[] : ")
    for index in range(len(parents)):
        if (parents[index] != -1): print("[", vertices[index], "]: ", parents[index].name)

    print(".....................................")
    #_____________________________________________________________________________

    u = B.get_minimum()

    adjacent_vertices = u.get_adjacent_vertices()

    #__________________________MORE TESTING EWWW___________________________________________________
    print("\nadjacent vertices to u: ( u is", u.name,")")
    for index in range(len(adjacent_vertices)):
        print(">", vertices[adjacent_vertices[index]])
    #_____________________________________________________________________________

    for index in range(len(adjacent_vertices)):
        if B.contains(adjacent_vertices[index]):
            edge_cost = graph[u.vertex_number][index]

            # update key value of v in B if weight of edge (u,v) is
            # smaller than current key value of v
            if edge_cost < u.cheapest_edge_cost and edge_cost != 0:
                B.update_key(u.vertex_number, 42)

                # parent[v] = u
                parents[index] = u



