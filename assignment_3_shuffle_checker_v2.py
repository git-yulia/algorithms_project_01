# Analysis of Algorithms
# Assignment 3: Shuffle Checker using Dynamic Programming
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca

try:
    U = input("Enter U: ")
except SyntaxError:
    U = ""
try:
    V = input("Enter V: ")
except SyntaxError:
    V = ""
try:
    W = input("Enter W: ")
except SyntaxError:
    W = ""

def check_shuffle(U, V, W):
    if len(W) != (len(U) + len(V)):
        print(W, "is not an interleaving of", U, "and", V, ".")
        return False

    graph = [[False for x in range(0, len(U) + 2)] for y in range(0, len(V) + 2)]
    graph[0][0] = True

    # the edges along the 'outside' of the graph have one parent each, so set them specially
    for i in range(1, len(V)):
        graph[0][i] = (graph[0][i - 1] and V[i] == W[i])
    for j in range(1, len(U)):
        graph[j][0] = (graph[j - 1][0] and U[j] == W[j])

    for i in range(0, len(U)):
        for j in range(0, len(V)):
            print("i: ", i, " j: ", j)
            graph[i][j] = (graph[i - 1][j] and U[i] == W[i + j]) or (
                graph[i][j - 1] and V[j] == W[i + j]
            )
            print("g[i][j]: ", graph[i][j])

    if graph[len(U) - 1][len(V) - 1] == True:
        print(W, "is an interleaving of ", U, " and ", V, ".")
        return True
    else:
        print(W, "is not an interleaving of ", U, " and ", V, ".")
        return False 

check_shuffle(U, V, W)