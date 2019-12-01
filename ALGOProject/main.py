from NodeClass import node as nd
from DataCleaning import data_cleaning_script as dcs
from Algorithms import Prims_Helper, Kruskal_Helper, \
                        Dijkstra_Helper, BellmanFord_Helper, \
                        FloydWarshall_Helper, ClusteringCoefficient_Helper
from GUI import menu, plot

if __name__ == "__main__":
    menu.menu()
    # # Adding cleaned data into node class
    # returned_data = dcs.cleaned_data(0)
    # number = returned_data[0]["no_of_nodes"]
    # graph_nodes = []
    # for i in range(1, number+1):
    #     n1 = nd.node(node_name=i-1, x_axis=returned_data[i][i-1][0],
    #                     y_axis=returned_data[i][i-1][1], edge_cost=returned_data[i+number][i-1])
    #     graph_nodes.append(n1)
    
    # # starting node
    # n1 = nd.node(node_name=returned_data[-1]['starting_node'], x_axis=0, y_axis=0, edge_cost=[])
    # graph_nodes.append(n1)
    
    # for node in graph_nodes:
    #     print(node)

    # # Formatting data for initial graph
    # graph = []
    # # graph_nodes - 1,  beasuse initial/starting node stored at last index
    # vertices = len(graph_nodes) - 1
    # for i in range(vertices):
    #     length_edge = len(graph_nodes[i].get_edge())
    #     for j in range(length_edge):
    #         temp = []
    #         temp.append(graph_nodes[i].get_node_name())
    #         temp.append(graph_nodes[i].get_edge()[j])
    #         temp.append(graph_nodes[i].get_cost()[j])
    #         graph.append(temp)
    # # Adding 1 for consistency, beacuse in plotgraph we're iterating form 1 to n-1
    # graph.append(1)
    
    prims_graph = Prims_Helper.prims_helper(graph_nodes)
    kruskal_graph = Kruskal_Helper.kruskal_helper(graph_nodes)
    dijkstra_graph = Dijkstra_Helper.dijkstra_helper(graph_nodes)
    bellmanford_graph = BellmanFord_Helper.bellman_ford_helper(graph_nodes)
    floydwarshall_graph = FloydWarshall_Helper.floyd_warshall_helper(graph_nodes, dijkstra_graph)
    clustering_coefficient = ClusteringCoefficient_Helper.clustering_coefficient_helper(graph_nodes)


    # print(prims_graph[-1], kruskal_graph[-1], dijkstra_graph[-1], bellmanford_graph[-1], floydwarshall_graph[-1], clustering_coefficient)
    # print(prims_graph)
    # print(kruskal_graph)
    # print(dijkstra_graph)
    # print(bellmanford_graph)
    # print(floydwarshall_graph)
    # print(clustering_coefficient)
    

    # nodes_coordinates = []
    # for node in graph_nodes:
    #     nodes_coordinates.append(node.get_coordinate())
    # #poping last index because it is the starting node
    # nodes_coordinates.pop(-1)

    # plot.plotgraph(nodes_coordinates, graph)
    # networkx.average_clustering()
    # print(nodes_coordinates)
