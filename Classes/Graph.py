from collections import defaultdict
from parameter import *
from typing import List


class Graph:
    def __init__(self, cyclelabel_alphabet):
        self.graph = {}
        self.vertices = set()
        self.occ_counter = []
        self.occ_array = []
        self.label_history = []
        self.iterational_history = []
        self.cyclelabel_alphabet = cyclelabel_alphabet
        self.nodes_to_ignore = []
        self.cycles = []
        self.nodeids_marked_unimportant = []

    def get_labels(self):
        return [(vertex, self.graph[vertex]["label"]) for vertex in self.vertices]

    def add_vertex(self, vertex, label=""):
        # Adds a new vertex with a label if it is not already in the graph
        self.vertices.add(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = {"label": label, "neighbors": [], "next_label": label}

    def add_edge(self, vertex1, vertex2):
        # Adds an undirected edge between two vertices
        self.graph[vertex1]["neighbors"].append(vertex2)
        self.graph[vertex2]["neighbors"].append(vertex1)

    def get_size(self):
        return len(self.graph)

    def get_vertex_label(self, vertex):
        return self.graph[vertex]["label"]

    def set_vertex_label(self, vertex, label):
        self.graph[vertex]["label"] = label

    def set_vertex_next_label_to_full_label(self, vertex):
        self.graph[vertex]["next_label"] = self.get_vertex_complete_label(vertex)

    def set_vertex_next_label(self, vertex, n_label):
        self.graph[vertex]["next_label"] = n_label

    def set_all_vertex_label(self, label):
        for v in self.graph:
            self.graph[v]["label"] = label

    def set_vertex_label_to_next_label(self, vertex):
        self.graph[vertex]["label"] = self.graph[vertex]["next_label"]

    def get_vertex_complete_label(self, vertex):
        # Returns a string that combines the label of a given vertex with the labels of its neighbors
        label = self.graph[vertex]["label"]
        neighbors = self.graph[vertex]["neighbors"]
        labels_from_neighbors = [self.graph[n]["label"] for n in neighbors]
        labels_from_neighbors.sort()
        lfn = ""
        for lbl in labels_from_neighbors:
            lfn += str(lbl)
        return f"{label},{lfn}"

    def get_adjacent_vertices(self, vertex):
        return self.graph[vertex]["neighbors"]

    def get_num_vertices(self):
        return len(self.graph.keys())

    def prnt(self):
        print(self.graph)

    def get_degree_of_vertex(self, vertex):
        return len(self.graph[vertex]["neighbors"])

    def update_occ_counter(self, list):
        self.occ_counter.extend(list)

    def update_occ_array(self, list):
        self.occ_array.append(list)

    def get_last_from_array(self):
        return self.occ_array[-1]

    def get_history(self):
        return self.label_history

    def append_history(self, label):
        self.label_history.append(int(label))

    def count_in_history(self, alpha):
        return self.label_history.count(alpha)

    def count_label_occurences_in_graph_history(self, inverted_alphabet, p_max_iteration):
        label_history_p_max_iteration = self.label_history[:p_max_iteration*self.get_size()]
        output = []
        for alpha in inverted_alphabet:
            c = label_history_p_max_iteration.count(alpha)
            output.append(c)
        return output

    def new_history_iteration(self):
        self.iterational_history.append({})

    def get_hisory_iteration(self, iteration):
        return self.iterational_history[iteration-1]

    def add_to_latest_history_iteration(self, nodeid, label):
        self.iterational_history[-1][nodeid] = label

    def get_latest_x_hisory_iterations(self, iters):
        return self.iterational_history[-iters:]

    def add_nodeids_marked_unimportant(self, nodeid):
        self.nodeids_marked_unimportant.append(nodeid)



testgraph = Graph(parameter.cyclealphabet)

testgraph.add_vertex(1, 0)
testgraph.add_vertex(2, 0)
testgraph.add_vertex(3, 0)
testgraph.add_vertex(4, 0)
testgraph.add_vertex(5, 0)
testgraph.add_vertex(6, 0)

testgraph.add_edge(2,3)
testgraph.add_edge(2,4)
testgraph.add_edge(1,3)
testgraph.add_edge(1,2)
testgraph.add_edge(4,5)
testgraph.add_edge(5,1)
testgraph.add_edge(2,6)



