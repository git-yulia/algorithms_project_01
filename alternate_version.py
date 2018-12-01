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

print(len(U), len(V), len(W))
if len(W) != (len(U) + len(V)):
    print(W, "is NOT an interleaving of", U, "and", V)

graph = [[0 for x in range(0, len(U) + 2)] for y in range(0, len(V) + 2)]
graph[0][0] = True

# the edges along the 'outside' of the graph have one parent each, so set them specially
for i in range(1, len(U)):
    graph[0][i] = graph[0][i - 1] and U[i] == W[i]
for j in range(1, len(V)):
    graph[j][0] = graph[j - 1][0] and V[j] == W[j]

    
for i in range(0, len(U) - 1):
    for j in range(0, len(V) - 1):
        print("i: ", i, " j: ", j)
        graph[i + 1][j + 1] = (graph[i + 1][j] and U[i] == W[i + j]) or (
            graph[i][j + 1] and V[j] == W[i + j]
        )


print("v: ", len(V), " u: ", len(U))
if graph[len(U) - 1][len(V) - 1] == True:
    print(W, " is an interleaving of ", U, " and ", V)
else:
    print(W, " is NOT an interleaving of ", U, " and ", V)
