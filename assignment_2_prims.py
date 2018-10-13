# Analysis of Algorithms
# Assignment 2: Prim's Algorithm 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018 

# Prim's algorithm for constructing MCSTs grows trees in a natural way, 
# starting from an arbitrary root. 
# At each stage, it adds a new branch to the already-constructed tree T. 
# The algorithm stops when all nodes have been reached. 

# Initialize our graph 
# CURRENTLY USING EXAMPLE GRAPH 1 - see the .png in Git repo 
graph = { "e1" : ["v1", "v2"],  
          "e2" : ["v1", "v3"],  
          "e3" : ["v3", "v4"],  
          "e4" : ["v2", "v4"],  
          "e5" : ["v2", "v5"],
          "e6" : ["v4", "v5"]
        } 

# Initialize V using all the vertices from the graph. 
# (vertices are all currently set to a cost of 1.)
vertices = ["v1","v2","v3","v4","v5"]
edges    = ["e1", "e2", "e3", "e4", "e5", "e6"]  

# Initialize T, an empty tree that will later become our MCST. 
tree = []

# Initialize B using v, an arbitrary vertex of V (all the vertices). 
B = ["v1"]

# While B != V: 
index = 1
while len(B) < len(vertices): 
    # find cheapest e = (v1, v2) such that v1 in B, v2 in V - B
    

    # T = T union {e}

    index = index + 1


