import networkx as nx
import matplotlib.pyplot as plt
import warnings
from NodeClass import PopulatingNode
from Algorithms import Prims_Helper, Kruskal_Helper, \
                        Dijkstra_Helper, BellmanFord_Helper, \
                        FloydWarshall_Helper, ClusteringCoefficient_Helper

def plot_it(coordinates, graph, message, cost):
    warnings.filterwarnings("ignore", category=UserWarning)
    G=nx.DiGraph()
    fig, ax = plt.subplots()
    for j in range(0,len(coordinates)):
        a = coordinates[j][0]
        b = coordinates[j][1]
        G.add_node(j,pos=(a,b))

    for i in range(0,len(graph)-1):
        x = graph[i][0]
        y = graph[i][1]
        z = graph[i][2]
        G.add_edge(x,y,weight=z)

    pos=nx.get_node_attributes(G,'pos')
    nx.draw_networkx(G, pos, ax=ax)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    ax.tick_params(left = True, bottom = True, labelleft = True, labelbottom = True)
    plt.get_current_fig_manager().window.showMaximized() # .window.state('zoomed') # .frame.Maximize(True)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    if message != "Initial Graph":
        message = message+str(cost)
        
    plt.title(message)
    plt.show()

def plotgraph(coordinates, graph, file, algo=0):
    graph_nodes = PopulatingNode.populate(file)
    if not algo:
        print(graph)
        print()
        plot_it(coordinates, graph, "Initial Graph", 0)
    elif algo == 1:
        prims_graph = Prims_Helper.prims_helper(graph_nodes)
        print(prims_graph)
        print()
        plot_it(coordinates, prims_graph, "Prim's Total Cost: ", prims_graph[-1])
    elif algo == 2:
        kruskal_graph = Kruskal_Helper.kruskal_helper(graph_nodes)
        print(kruskal_graph)
        print()
        plot_it(coordinates, kruskal_graph,  "Kruskal's Total Cost: ", kruskal_graph[-1])
    elif algo == 3:
        dijkstra_graph = Dijkstra_Helper.dijkstra_helper(graph_nodes)
        print(dijkstra_graph)
        print()
        plot_it(coordinates, dijkstra_graph,  "Dijkstra's Total Cost: ", dijkstra_graph[-1])
    elif algo == 4:
        bellmanford_graph = BellmanFord_Helper.bellman_ford_helper(graph_nodes)
        print(bellmanford_graph)
        print()
        plot_it(coordinates, bellmanford_graph,  "Bellman Ford's Total Cost: ", bellmanford_graph[-1])
    elif algo == 5:
        dijkstra_graph = Dijkstra_Helper.dijkstra_helper(graph_nodes)
        floydwarshall_graph = FloydWarshall_Helper.floyd_warshall_helper(graph_nodes, dijkstra_graph)
        print(floydwarshall_graph)
        print()
        plot_it(coordinates, floydwarshall_graph,  "Floyd Warshall's Total Cost: ", floydwarshall_graph[-1])
    elif algo == 6:
        clustering_coefficient = ClusteringCoefficient_Helper.clustering_coefficient_helper(graph_nodes)
        print(clustering_coefficient)
        print()
        plot_it(coordinates, graph,  "Clustering Coefficient: ", clustering_coefficient)
