# http://math.hws.edu/eck/cs327_s04/chapter10.pdf reference 

try: 
    U = raw_input("Enter U: ")
except syntaxError: U = ""
try:
    V = raw_input("Enter V: ")
except syntaxError: V = ""
try:
    W = raw_input("Enter W: ")
except syntaxError:
    W = ""

print(len(U), len(V), len(W))
if len(W)!=(len(U)+len(V)):
    print(W,"is not an interleaving of",U,"and",V,"cuz length")
#    exit()
graph = [[0 for x in range(0, len(U)+2)] for y in range(0, len(V)+2)]

'''for x in range(0, len(U)+1):
    for y in range(0, len(V)+1):
        if x==0 and y==0:
            graph[x][y]=True
        elif (x == 0 and V[y-1]==W[y-1]):
            graph[x][y]=graph[x][y-1]
        elif (y == 0 and U[x-1]==W[x-1]):
            graph[x][y]=graph[x-1][y]
        elif (graph[x-1][y]==True and U[x-1]==W[x+y-1]) or (graph[x][y-1]==True and V[y-1]==W[x+y-1]):
            graph[x][y]=True
        else: graph[x][y]=False
        '''
#if graph[len(U)][len(V)] == True:
#if len(W)==0 and len(U)==0 and len(V)==0:
#print("The blank string W is an interleaving of the two blank strings U and V") else: print(W,"is an interleaving of",U,"and",V) else: print(W,"is not an interleaving of",U,"and",V)
graph[0][0] = True
# the edges along the 'outside' of the graph have one parent each, so set them specially
for i in range(1, len(U)):
    graph[0][i] = graph[0][i-1] and U[i] == W[i]
for j in range(1, len(U)):
    graph[j][0] = graph[j-1][0] and U[j] == W[j]
for i in range(0, len(U)-1):
    for j in range(0, len(V)-1):
        print("i: ", i, " j: ", j)
        graph[i+1][j+1] = (graph[i+1][j] and U[i] == W[i+j]) or (graph[i][j+1] and V[j] == W[i+j])
        #graph[i+1][j] = graph[i][j] && U[i] == W[i+j] # adapted to work without basecase
        #graph[i][j+1] = graph[i][j]
        #graph[i][j] = U[i-1] == W[i+j+1] and graph[i][j] == True
        #graph[i][j+1] = V[j+1] == W[i+j+1] and graph[i][j] == True
'''
while i + j < len(W):
    if (U[i+1] == W[x+y+1]):
        graph[i+1][j] = True
    if (V[j+1] == W[x+y+1]):
        graph[i][j+1] = True
   ''' 

print("v: ", len(V), " u: ", len(U))
if (graph[len(U)-1][len(V)-1] == True):
    print(W, " is an interleaving of ", U, " and ", V)
else:
    print("no")
