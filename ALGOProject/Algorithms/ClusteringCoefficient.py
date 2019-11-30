import copy

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

def clustering_coefficient(V, G, initial_node):
    graph = createAdjMatrix(V, G)
    connected_nodes = []
    Kv = []
    Nv = []
    coefficient = []
    # Extracting nodes data, e.g connected_nodes[1] contains all nodes that are connected to 1
    for k in range(V):
        temp = []
        for i in range(V):
            for j in range(V):
                if j == k and graph[i][j]!=0:
                    temp.append(i)
        connected_nodes.append(temp)

    # Calculate Kv
    for i in range(V):
        Kv.append(len(connected_nodes[i]))


    # Calculating Nv
    for l in range(V):
        Nv_sum = 0
        temp_list = []
        # connected_nodes[1] = 0,4,7, below code will check
        # that 0 is connected to 4,7 ?
        # 4 is connected to 0,7 ? //[Also it will discard the repeated node 4->0 (used tuples)]
        # 7 is connected to 4,7 ?
        for i in range(len(connected_nodes[l])):
            temp = copy.deepcopy(connected_nodes[l])
            temp.remove(temp[i])
            for j in range(len(temp)):
                for k in range(len(connected_nodes[connected_nodes[l][i]])):
                    flag = 0
                    t1 = temp[j]
                    t2 = connected_nodes[connected_nodes[l][i]][k]
                    if (t1 == t2 and (t1, connected_nodes[l][i]) not in temp_list):
                        Nv_sum += 1
                        temp_tuple1 = (connected_nodes[l][i], t1)
                        temp_tuple2 = (t1, connected_nodes[l][i])
                        temp_list.append(temp_tuple1)
                        temp_list.append(temp_tuple2)
        Nv.append(Nv_sum)
    
    # Calculating Clustering Coefficient
    for i in range(V):
        coefficient.append(round((2*Nv[i])/(Kv[i]*(Kv[i]-1)), 2))

    # Average Clustering Coefficient
    return sum(coefficient)/V 
