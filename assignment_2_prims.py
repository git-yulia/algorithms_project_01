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
    [0, 9, 3, 0, 0],
    [9, 0, 0, 1, 8],
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
                added_edge = Edge(self.vertex_number, index, (graph[self.vertex_number][index]))
                #print("Added an edge to adjacents:", edge_names[added_edge.contents[0]][added_edge.contents[1]])
                adjacent_edges.append(added_edge)

        return adjacent_edges

class Edge:
    def __init__(self, vertex_1, vertex_2, edge_weight):
        self.name = edge_names[vertex_1][vertex_2]
        self.contents = (vertex_1, vertex_2)
        self.edge_weight = edge_weight

class min_priority_queue:
    "Contains information and methods for dealing with B, our heap structure"
    def __init__(self, size_of_heap):
        self.size = size_of_heap
        self.contents = []

    "pop: removes front edge at index 0 which is lowest cost, highest priority"
    def pop_minimum(self):
        popped_item = self.contents[0]
        self.contents.remove(popped_item)
        self.size = self.size - 1
        return popped_item

    "push: appends edges to B and then sorts all of them" 
    def push(self, edge):
        self.contents.append(edge)

    def flush(self):
        for edge in self.contents:
            self.contents.pop()
            self.size = self.size - 1

    def heapsort(self):
        heapSort(self.contents)

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i].edge_weight < arr[l].edge_weight: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest].edge_weight < arr[r].edge_weight: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

class MCST: 
    def __init__(self):
        self.contents = [] 
        self.size = 0 

    def add_edge(self, edge):
        self.contents.append(edge)
        self.size = self.size + 1

    def does_not_contain(self, edge_name):
        edge_not_here = True

        for index in range(len(self.contents)):
            if self.contents[index].name == edge_name:
                edge_not_here = False

        return edge_not_here

    def does_not_contain_vertex(self, vertex):
        vertex_not_here = True
        print("!! looking for", vertices[vertex])

        for index in range(len(self.contents)):
            print(">>>>>>> looking at ", vertices[self.contents[index].contents[1]])
            if vertices[self.contents[index].contents[1]] == vertices[vertex]: 
                print("found",  vertices[vertex])
                vertex_not_here = False

        return vertex_not_here

    def print_contents(self):
        for edge in self.contents:
            print(">", edge.name)


def main():
    
    # create a min heap of size V. let the min heap be B[]
    B = min_priority_queue(len(vertices))

    stage = 0
    current_vertex = vertex(0)
    element_in_T = -1

    T = MCST()

    print("Starting Prim's algorithm at arbitrary root", vertices[current_vertex.vertex_number])

    while T.size < required_number_of_edges and stage < 5:
        print("current_vertex =", vertices[current_vertex.vertex_number])


        # Find adjacent_vertices 
        adjacent_vertices = current_vertex.get_adjacent_edges() 
        
        #  push adjacent edges of current_vertex to B and SORT 
        for edge in adjacent_vertices:
            #print("Trying to add edge", edge.contents[0], edge.contents[1])

            # only add the edge to B if it is not already in our MCST
            if T.does_not_contain_vertex(edge.contents[1]):
                print("added ", edge.name)
                B.push(edge) 

        # SORT B 
        B.heapsort()

        #  if size(B) == 0 (no edges), current_vertex = find_vertex_with_new_paths(), push those to B and SORT 
        # subtract element_in_T until we get there
        """
        if B.size == 0: 
            looking_at_vertex = T.size - 1

            while B.size == 0: 
                current_vertex = vertex(T.contents[looking_at_vertex].contents[1])
                print("analyzing", current_vertex.name)
                adjacent_vertices = current_vertex.get_adjacent_edges() 

                 #  push adjacent edges of current_vertex to B and SORT 

                for edge in adjacent_vertices:
                    print("Trying to add edge", edge.name)
                    print("Does T contain", vertices[edge.contents[1]])

                    # only add the edge to B if it is not already in our MCST
                    if T.does_not_contain_vertex(edge.contents[1]):
                        print("Added to b", edge.name)
                        B.push(edge) 

                looking_at_vertex = looking_at_vertex - 1 # go back a node

                B.heapsort() 
        """


        #  pop top edge (cheapest) of B to T if T does not already contain e(i)
        T.add_edge(B.pop_minimum())

        #  set new current_vertex to T[]'s last element's tail 
        current_vertex = vertex(T.contents[element_in_T].contents[1])

        
        

        

        print("[ STAGE", stage, "]")
        print("\nB = {")
        for edge in B.contents: 
            print(">",edge.name, edge.edge_weight)
        print("}")
        print("\nT: {")
        for edge in T.contents: 
            print(">",edge.name, edge.edge_weight)
        print("}")
        print("_________________________________________")
        stage = stage + 1

        B.flush()


        

main() 