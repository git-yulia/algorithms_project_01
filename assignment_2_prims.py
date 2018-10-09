# Analysis of Algorithms
# Assignment 2: Prim's Algorithm 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca
# Due October 24, 2018 

# Prim's algorithm for constructing MCSTs grows trees in a natural way, 
# starting from an arbitrary root. 
# At each stage, it adds a new branch to the already-constructed tree T. 
# The algorithm stops when all nodes have been reached. 

# Initialize T, an empty tree that will later become our MCST. 

# Initialize V using all the vertices from the graph. 

# Initialize B using v, an arbitrary vertex of V (all the vertices). 

# While B != V: 

# find cheapest e = (v1, v2) such that v1 in B, v2 in V - B

# T = T union {e}
# B = B union {v2}
