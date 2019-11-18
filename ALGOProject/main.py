from NodeClass import node as nd
from DataCleaning import data_cleaning_script as dcs
from Algorithms import Prims_Helper

if __name__ == "__main__":
    returned_data = dcs.cleaned_data(0)
    number = returned_data[0]["no_of_nodes"]
    graph_nodes = []
    for i in range(1, number+1):
        n1 = nd.node(node_name=i-1, x_axis=returned_data[i][i-1][0],
                        y_axis=returned_data[i][i-1][1], edge_cost=returned_data[i+number][i-1])
        graph_nodes.append(n1)
    
    for node in graph_nodes:
        print(node)
    
    Prims_Helper.prims_helper(graph_nodes)
    # print(nodes[0])
    # print(nodes[0].get_cost())
    # print(nodes[0].get_edge())