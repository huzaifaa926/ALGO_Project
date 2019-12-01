from NodeClass import PopulatingNode
from tkinter import *
import tkinter as tk
from . import plot

graph_nodes = []
nodes_coordinates = []
graph = []
val = 0

def selectfile(val):
    graph_nodes = PopulatingNode.populate(val)    
    # Formatting data for initial graph
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
    # Adding 1 for consistency, beacuse in plotgraph we're iterating form 1 to n-1
    graph.append(1)

    for node in graph_nodes:
        nodes_coordinates.append(node.get_coordinate())
    #poping last index because it is the starting node
    nodes_coordinates.pop(-1)


def menu():
    master = Tk()
    master.title("Play With Graphs")
    master.state('zoomed')
    w = Label(master, text='Select your file and then press OK.')
    w.place(relx = 0.5, rely = 0.35, anchor = CENTER)
    var = StringVar(master)

    option = OptionMenu(master, var, "input10", "input20", "input30", "input40", "input50", "input60", "input70", "input80", "input90", "input100")
    option.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    def ok():
        value = var.get()
        if value == "input10":
            val = 0
            selectfile(0)
        elif value == "input20":
            val = 1
            selectfile(1)
        elif value == "input30":
            val = 2
            selectfile(2)
        elif value == "input40":
            val = 3
            selectfile(3)
        elif value == "input50":
            val = 4
            selectfile(4)
        elif value == "input60":
            val = 5
            selectfile(5)
        elif value == "input70":
            val = 6
            selectfile(6)
        elif value == "input80":
            val = 7
            selectfile(7)
        elif value == "input90":
            val = 8
            selectfile(8)
        elif value == "input100":
            val = 9
            selectfile(9)
        else:
            err = Label(master, text='No file Chosen!', foreground = 'red')
            err.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            return

        master.destroy()

        m = tk.Tk()
        m.title('Play With Graphs')
        m.state('zoomed')
        initial = tk.Button(m, text='Plot Initial Graph', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph, file=val))
        initial.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        mst = tk.Label(m, text = 'Minimum Spanning Tree Algorithms')
        mst.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        pr = tk.Button(m, text='Prims', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph_nodes, algo=1, file=val))
        pr.place(relx = 0.39, rely = 0.4, anchor = CENTER)
        kr = tk.Button(m, text='Kruskal', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph_nodes, algo=2, file=val))
        kr.place(relx = 0.61, rely = 0.4, anchor = CENTER)
        SP = tk.Label(m, text = 'Shortest Path Algorithms')
        SP.place(relx = 0.5, rely = 0.55, anchor = CENTER)
        dij = tk.Button(m, text='Dijkstra', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph_nodes, algo=3, file=val))
        dij.place(relx = 0.28, rely = 0.6, anchor = CENTER)
        bell = tk.Button(m, text='Bellman Ford', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph_nodes, algo=4, file=val))
        bell.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        fl = tk.Button(m, text='Floyd Warshall', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph_nodes, algo=5, file=val))
        fl.place(relx = 0.72, rely = 0.6, anchor = CENTER)
        lc = tk.Label(m, text = 'Clustering Coefficient Algorithm')
        lc.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        local = tk.Button(m, text='Local Clustering', bd=5, width=40, height=2, command= lambda: plot.plotgraph(nodes_coordinates, graph, algo=6, file=val))
        local.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        m.mainloop()

    button = Button(master, text="OK", command=ok)
    button.place(relx = 0.5, rely = 0.45, anchor = CENTER)

    mainloop()