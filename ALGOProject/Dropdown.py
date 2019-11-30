from tkinter import *
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

def plotgraph(vertex, arr):
    G=nx.DiGraph()
    fig, ax = plt.subplots()
    for j in range(0,len(vertex)):
        a = vertex[j][0]
        b = vertex[j][1]
        G.add_node(j,pos=(a,b))
    for i in range(0,len(arr)):
        x = arr[i][0]
        y = arr[i][1]
        z = arr[i][2]
        G.add_edge(x,y,weight=z)
    pos=nx.get_node_attributes(G,'pos')
    nx.draw_networkx(G, pos, ax=ax)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    ax.tick_params(left = True, bottom = True, labelleft = True, labelbottom = True)
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

def selectfile(val):
    print("Huzu bhai file", val, "ko use karo xD")


master = Tk()
master.title("Play With Graphs")
master.state('zoomed')
w = Label(master, text='Select your file and then press OK.')
w.place(relx = 0.5, rely = 0.35, anchor = CENTER)
var = StringVar(master)

option = OptionMenu(master, var, "input10", "input20", "input30", "input40", "input50", "input60", "input70", "input80", "input90", "input100")
option.place(relx = 0.5, rely = 0.4, anchor = CENTER)

#
# test stuff

def ok():
    value = var.get()
    if value == "input10":
        selectfile(1)
    elif value == "input20":
        selectfile(2)
    elif value == "input30":
        selectfile(3)
    elif value == "input40":
        selectfile(4)
    elif value == "input50":
        selectfile(5)
    elif value == "input60":
        selectfile(6)
    elif value == "input70":
        selectfile(7)
    elif value == "input80":
        selectfile(8)
    elif value == "input90":
        selectfile(9)
    elif value == "input100":
        selectfile(10)
    else:
        err = Label(master, text='No file Chosen!', foreground = 'red')
        err.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        return

    master.destroy()

    m = tk.Tk()
    m.title('Play With Graphs')
    m.state('zoomed')
    initial = tk.Button(m, text='Plot Initial Graph', bd=5, width=40, height=2, command=m.destroy)
    initial.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    mst = tk.Label(m, text = 'Minimum Spanning Tree Algorithms')
    mst.place(relx = 0.5, rely = 0.35, anchor = CENTER)
    pr = tk.Button(m, text='Prims', bd=5, width=40, height=2, command=m.destroy)
    pr.place(relx = 0.39, rely = 0.4, anchor = CENTER)
    kr = tk.Button(m, text='Kruskal', bd=5, width=40, height=2, command=m.destroy)
    kr.place(relx = 0.61, rely = 0.4, anchor = CENTER)
    SP = tk.Label(m, text = 'Shortest Path Algorithms')
    SP.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    dij = tk.Button(m, text='Dijkstra', bd=5, width=40, height=2, command=m.destroy)
    dij.place(relx = 0.28, rely = 0.6, anchor = CENTER)
    bell = tk.Button(m, text='Bellman Ford', bd=5, width=40, height=2, command=m.destroy)
    bell.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    fl = tk.Button(m, text='Floyd Warshall', bd=5, width=40, height=2, command=m.destroy)
    fl.place(relx = 0.72, rely = 0.6, anchor = CENTER)
    lc = tk.Label(m, text = 'Clustering Coefficient Algorithm')
    lc.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    local = tk.Button(m, text='Local Clustering', bd=5, width=40, height=2, command=m.destroy)
    local.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    m.mainloop()

button = Button(master, text="OK", command=ok)
button.place(relx = 0.5, rely = 0.45, anchor = CENTER)

mainloop()
