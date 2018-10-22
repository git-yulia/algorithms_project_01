# Analysis of Algorithms
# Assignment 2: Prim's Algorithm
# Team members: Julia Maliauka, Yevhen Voitiuk, Michael Petracca
# Due October 24, 2018

import sys 
import math

INFINITY = math.inf 
  
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    # prints the MCST stored in T
    def printMCST(self, T): 
        print("Edge \tWeight")
        for i in range(1,self.V): 
            print(T[i],"-",i,"\t",self.graph[i][T[i]])
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def find_cheapest_edge(self, key, mstSet): 
        min = INFINITY
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
  
        #Key values used to pick minimum weight edge in cut 
        B = [INFINITY] * self.V 

        # Stores MCST as we construct it over time 
        T = [None] * self.V 

        # Pick some arbitrary vertex first 
        B[0] = 0 
        mstSet = [False] * self.V 
  
        T[0] = -1 # First node is always the root of 
  
        for vertex in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.find_cheapest_edge(B, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and B[v] > self.graph[u][v]: 
                        B[v] = self.graph[u][v] 
                        T[v] = u 
  
        self.printMCST(T) 
  
g = Graph(5) 
g.graph = [
    [0, 2, 3, 0, 0],
    [2, 0, 0, 1, 8],
    [3, 0, 0, 1, 0],
    [0, 1, 1, 0, 2],
    [0, 8, 0, 2, 0],
]
  
g.primMST(); 
  