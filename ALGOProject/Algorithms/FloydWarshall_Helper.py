from .FloydWarshall import floyd_warshall

def floyd_warshall_helper(graph_nodes, prev_graph):
    # Formatting data for floyd warshall algorithm
    graph = []
    # graph_nodes - 1,  beasuse initial/starting node stored at last index
    vertices = len(graph_nodes) - 1
    for i in range(vertices):
        length_edge = len(graph_nodes[i].get_edge())
        for j in range(length_edge):
            temp = []
            temp.append(graph_nodes[i].get_node_name())
            temp.append(graph_nodes[i].get_edge()[j])
            temp.append(graph_nodes[i].get_cost()[j])
            graph.append(temp)
            
    prev_graph[-1] = floyd_warshall(vertices, graph,  graph_nodes[-1].get_node_name())
    return prev_graph