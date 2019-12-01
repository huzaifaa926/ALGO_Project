import networkx as nx
import matplotlib.pyplot as plt
import warnings

def plotgraph(coordinates, graph):
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
    plt.show()