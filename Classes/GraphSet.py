from Classes.Graph import Graph


class GraphSet:
    def __init__(self):
        self.graphs = []

    def add_graph(self, graph):
        self.graphs.append(graph)

    def get_graph(self, index):
        return self.graphs[index]

    def count(self):
        return len(self.graphs)

    def clear(self):
        self.graphs.clear()

    def prnt(self):
        for g in self.graphs:
            g.prnt()

    def set_label_of_all_graphs(self, label):
        for g in self.graphs:
            g.set_all_vertex_label(label)

    def prntIDs(self):
        for g in self.graphs:
            print(self.graphs.index(g))

    def get_Set_size(self):
        return len(self.graphs)

    def get_count_nodes(self):
        ret = 0
        for graph in self.graphs:
            ret += graph.get_size()
        return ret

