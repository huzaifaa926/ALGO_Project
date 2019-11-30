from collections import defaultdict

def bellman_ford(V, G, initial_node):
    # Initialize distances from initial_node to all other vertices as INFINITE 
    dist = [float("Inf")] * V 
    dist[initial_node] = 0
    pi = [[0 for x in range(3)] for y in range(V)]

    # Relax all edges |V| - 1 times. A simple shortest path from initial_node to any other vertex can have at-most |V| - 1 edges 
    for i in range(V - 1): 
        # Update dist value and parent index of the adjacent vertices of the picked vertex. Consider only those vertices which are still in queue
        for u, v, w in G: 
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                    dist[v] = dist[u] + w 
                    pi[v][0] = u
                    pi[v][1] = v
                    pi[v][2] = w

    # check for negative-weight cycles. The above step guarantees shortest distances if G doesn't contain negative weight cycle. If we get a shorter path, then there is a cycle.
    for u, v, w in G: 
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                    print("Graph contains negative weight cycle")
                    return
    pi.pop(initial_node)
    total_cost = 0			
    for i in range(len(pi)):
    	total_cost += dist[i]
    pi.append(round(total_cost,2))
    return pi