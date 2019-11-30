import sys 

def createAdjMatrix(V, G):
    adjMatrix = []

    # create N x N matrix filled with 0 edge weights between all vertices
    for i in range(0, V):
        adjMatrix.append([])
        for j in range(0, V):
            adjMatrix[i].append(0)

    # populate adjacency matrix with correct edge weights
    for i in range(0, len(G)):
        adjMatrix[G[i][0]][G[i][1]] = G[i][2]
        adjMatrix[G[i][1]][G[i][0]] = G[i][2]

    return adjMatrix

def minDistance(dist, sptSet, V):
    # A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
    min = sys.maxsize 
    for v in range(V):
        if dist[v] < min and sptSet[v] == False: 
            min = dist[v] 
            min_index = v 
    return min_index 

def dijkstra(V, G, initial_node):
    graph = createAdjMatrix(V, G)
    dist = [sys.maxsize] * V 
    dist[initial_node] = 0
    sptSet = [False] * V 
    pi = [[0 for x in range(3)] for y in range(V)]

    for cout in range(V): 
        u = minDistance(dist, sptSet, V) 
        sptSet[u] = True
        for v in range(V): 
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]: 
                    dist[v] = dist[u] + graph[u][v]
                    pi[v][0] = u
                    pi[v][1] = v
                    pi[v][2] = graph[u][v]
    pi.pop(initial_node)
    total_cost = 0			
    for i in range(len(pi)):
    	total_cost += dist[i]
    pi.append(round(total_cost,2))

    return pi