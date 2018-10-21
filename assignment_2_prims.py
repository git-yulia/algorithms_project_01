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

edge_names = [
    [0, "e1", "e2", 0, 0],
    ["e1", 0, 0, "e4", "e5"],
    ["e2", 0, 0, "e3", 0],
    [0, "e4", "e3", 0, "e6"],
    [0, "e5", 0, "e6", 0],
]


# Initialize V using all the vertices from the graph.
vertices = ["v1", "v2", "v3", "v4", "v5"]
edges    = ["e1", "e2", "e3", "e4", "e5", "e6", "e7"]

# by definition of MCST: 
required_number_of_edges = len(vertices) - 1

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

    "get_adjacent_vertices: returns a list of all vertices connected to this one"

    def get_adjacent_vertices(self):
        adjacent_vertices = []

        for index in range(len(vertices)):
            if graph[self.vertex_number][index] != 0:
                adjacent_vertices.append(index)

        return adjacent_vertices

    def get_adjacent_edges(self):
        adjacent_edges = []

        for index in range(len(vertices)):
            if graph[self.vertex_number][index] != 0:
                added_edge = edge(self.vertex_number, index, (graph[self.vertex_number][index]))
                #print("Added an edge to adjacents:", edge_names[added_edge.contents[0]][added_edge.contents[1]])
                adjacent_edges.append(added_edge)

        return adjacent_edges

class edge:
    def __init__(self, vertex_1, vertex_2, edge_weight):
        self.name = edge_names[vertex_1][vertex_2]
        self.contents = (vertex_1, vertex_2)
        self.edge_weight = edge_weight

class min_priority_queue:
    "Contains information and methods for dealing with B, our heap structure"
    def __init__(self, size_of_heap):
        self.size = size_of_heap
        self.contents = [] * required_number_of_edges

    "pop: removes front edge at index 0 which is lowest cost, highest priority"
    def get_minimum(self):
        popped_item = self.contents[0]
        self.contents.remove(popped_item)
        self.size = self.size - 1
        return popped_item

    "push: appends edges to B and then sorts all of them" 
    def push(self, edge):
        pass

    def heapsort(self):
        print("B before sorting:", B)
        print("B after sorting:", B)

# Initialize T, an empty tree that will later become our MCST.


class MCST: 
    def __init__(self):
        self.contents = [] 
        self.size = 0 

    def add_edge(self, edge):
        self.contents.append(edge)
        self.size = self.size + 1

    def does_not_contain(self, edge_name):
        contains_edge = False

        for index in range(len(self.contents)):
            print(self.contents[index].name)
            print(edge_name)

            if self.contents[index].name == edge_name:
                contains_edge = True

        return contains_edge

    def print_contents(self):
        for edge in self.contents:
            print(edge.name)

edge_example = edge(0,1,2)
T = MCST()


# create a min heap of size V. let the min heap be B[]
B = min_priority_queue(len(vertices))

T.add_edge(edge(0,1,2))

def main():
    stage = 0
    current_vertex = vertex(0)
    
    print("Starting Prim's algorithm at arbitrary root", vertices[current_vertex.vertex_number])

    while T.size < required_number_of_edges and stage < 5:

        # Find adjacent_vertices 
        adjacent_vertices = current_vertex.get_adjacent_edges() 
        
        #  push adjacent edges of current_vertex to B and SORT 
        index = 0 
        for edge in adjacent_vertices:
            print(edge.name)

            # only add the edge to B if it is not already in our MCST
            if T.does_not_contain(edge.name):
                print("gonna add this edge")    

            index = index + 1
        #  do not add edge if in T
        

        #  if size(B) == 0 (no edges), current_vertex = find_vertex_with_new_paths(), push those to B and SORT 

        #  pop top edge (cheapest) of B to T if T does not already contain e(i)

        #  set new current_vertex to T[]'s last element's tail 

        

        

        print("[ STAGE", stage, "]")
        print("B = ", B.contents)
        print("T = ", T.print_contents())
        print("current_vertex    = ", vertices[current_vertex.vertex_number])
        print("_________________________________________")
        stage = stage + 1

    print("T = ", T.print_contents())
        

main() 