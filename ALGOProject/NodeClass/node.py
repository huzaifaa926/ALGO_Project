class node:
    _x_axis = 0
    _y_axis = 0
    _node_name = 0
    _edge_cost = []
    def __init__(self, node_name, x_axis, y_axis, edge_cost):
        self._x_axis = x_axis
        self._y_axis = y_axis
        self._node_name = node_name
        self._edge_cost = edge_cost

    def get_cost(self):
        cost = []
        for i in self._edge_cost:
            cost.append(i[1])
        return cost

    def get_edge(self):
        edge = []
        for i in self._edge_cost:
            edge.append(i[0])
        return edge

    def get_edge_cost(self):
        return self._edge_cost

    def get_node_name(self):
        return self._node_name

    def get_coordinate(self):
        return (self._x_axis, self._y_axis)

    def get_x_axis(self):
        return self._x_axis

    def get_y_axis(self):
        return self._y_axis
    
    def __str__(self):
        return '{\n\tnode name: ' + str(self.get_node_name()) + \
                '\n\tx: ' + str(self.get_x_axis()) + '\n\ty: ' + str(self.get_y_axis()) + \
                '\n\tedges: ' + str(self.get_edge()) + '\n\tcosts: ' + str(self.get_cost()) + \
                '\n\t(edge, cost): ' + str(self.get_edge_cost()) + '\n}\n'