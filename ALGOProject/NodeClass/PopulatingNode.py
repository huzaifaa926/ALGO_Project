from NodeClass import node as nd
from DataCleaning import data_cleaning_script as dcs

def populate(val):
    # Adding cleaned data into node class
    returned_data = dcs.cleaned_data(val)
    number = returned_data[0]["no_of_nodes"]
    graph_nodes = []
    for i in range(1, number+1):
        n1 = nd.node(node_name=i-1, x_axis=returned_data[i][i-1][0],
                        y_axis=returned_data[i][i-1][1], edge_cost=returned_data[i+number][i-1])
        graph_nodes.append(n1)
    
    # starting node
    n1 = nd.node(node_name=returned_data[-1]['starting_node'], x_axis=0, y_axis=0, edge_cost=[])
    graph_nodes.append(n1)

    return graph_nodes