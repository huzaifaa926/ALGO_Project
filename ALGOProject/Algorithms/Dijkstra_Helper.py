from .Dijkstra import dijkstra

def dijkstra_helper(graph_nodes):
    # Formatting data for dijkstra algorithm
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

    return dijkstra(vertices, graph,  graph_nodes[-1].get_node_name())