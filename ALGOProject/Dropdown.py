from tkinter import *
import tkinter as tk

def selectfile(val):
    print(val)
    return val


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
        selectfile(0)
    elif value == "input20":
        selectfile(1)
    elif value == "input30":
        selectfile(2)
    elif value == "input40":
        selectfile(3)
    elif value == "input50":
        selectfile(4)
    elif value == "input60":
        selectfile(5)
    elif value == "input70":
        selectfile(6)
    elif value == "input80":
        selectfile(7)
    elif value == "input90":
        selectfile(8)
    elif value == "input100":
        selectfile(9)
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
