from NodeClass import node as nd
from DataCleaning import data_cleaning

if __name__ == "__main__":
    files_to_be_read = ["input10.txt", "input20.txt", "input30.txt",
                        "input40.txt", "input50.txt", "input60.txt",
                        "input70.txt", "input80.txt", "input90.txt",
                        "input100.txt",
                        ]
    returned_data = data_cleaning.clean_data(filename=files_to_be_read[0], is_write=False)
    number = returned_data[0]["no_of_nodes"]
    graph_nodes = []
    for i in range(1, number+1):
        n1 = nd.node(node_name=i-1, x_axis=returned_data[i][i-1][0],
                        y_axis=returned_data[i][i-1][1], edge_cost=returned_data[i+number][i-1])
        graph_nodes.append(n1)
    
    for node in graph_nodes:
        print(node)
    # print(nodes[0])
    # print(nodes[0].get_cost())
    # print(nodes[0].get_edge())