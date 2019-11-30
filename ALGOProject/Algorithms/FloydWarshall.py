import sys

INF = sys.maxsize
def createAdjMatrix(V, G):
    adjMatrix = []

    # create N x N matrix filled with INF edge weights between all vertices
    for i in range(0, V):
        adjMatrix.append([])
        for j in range(0, V):
            if i == j:
                adjMatrix[i].append(0)    
            else:
                adjMatrix[i].append(INF)

    # populate adjacency matrix with correct edge weights
    for i in range(0, len(G)):
        adjMatrix[G[i][0]][G[i][1]] = G[i][2]
        adjMatrix[G[i][1]][G[i][0]] = G[i][2]

    return adjMatrix

def floyd_warshall(V, G, initial_node):
	graph = createAdjMatrix(V, G)
	# calculating all pair shortest path
	for k in range(0, V):
		for i in range(0, V):
			for j in range(0, V):
				# relax the distance from i to j by allowing vertex k as intermediate vertex
				# consider which one is better, going through vertex k or the previous value
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
	dist = graph[initial_node]
	total_cost = 0			
	for i in range(len(dist)):
		total_cost += dist[i]
	total_cost = round(total_cost,2)
	return total_cost
	