import dfs2
from parameter import *
from Classes.Graph import Graph
from Classes.GraphSet import GraphSet
import os


def generate_graphs(graph_indicator_file, A_file, labels_file):
    graph_indicator = []
    with open(graph_indicator_file, "r") as f:
        for line in f:
            graph_indicator.append(int(line.strip()))

    labels = []
    if os.path.exists(labels_file):
        with open(labels_file, "r") as f:
            for line in f:
                labels.append(int(line.strip()))
    else:
        labels = None

    graph_set = GraphSet()
    graphs = {}
    with open(A_file, "r") as f:
        for line in f:
            node1, node2 = [int(x) for x in line.strip().split(",")]
            graph_id = graph_indicator[node1-1]
            if graph_id not in graphs:
                graphs[graph_id] = Graph(parameter.cyclealphabet)
                graph_set.add_graph(graphs[graph_id])

            if labels is not None:
                graphs[graph_id].add_vertex(node1, str(labels[node1-1]))
                graphs[graph_id].add_vertex(node2, str(labels[node2-1]))
            else:
                graphs[graph_id].add_vertex(node1, "0")
                graphs[graph_id].add_vertex(node2, "0")

            graphs[graph_id].add_edge(node1, node2)

    return graph_set


def generate_graphs_with_cycle_labeling(graph_indicator_file, A_file, labels_file):
    graph_indicator = []

    with open(graph_indicator_file, "r") as f:
        for line in f:
            graph_indicator.append(int(line.strip()))

    labels = []
    if os.path.exists(labels_file):
        with open(labels_file, "r") as f:
            for line in f:
                labels.append(int(line.strip()))
    else:
        labels = None

    graph_set = GraphSet()
    graphs = {}
    with open(A_file, "r") as f:
        for line in f:
            node1, node2 = [int(x) for x in line.strip().split(",")]
            graph_id = graph_indicator[node1-1]
            if graph_id not in graphs:
                graphs[graph_id] = Graph(parameter.cyclealphabet)
                graph_set.add_graph(graphs[graph_id])

            if labels is not None:
                graphs[graph_id].add_vertex(node1, str(labels[node1-1]))
                graphs[graph_id].add_vertex(node2, str(labels[node2-1]))
            else:
                graphs[graph_id].add_vertex(node1, "0")
                graphs[graph_id].add_vertex(node2, "0")

            graphs[graph_id].add_edge(node1, node2)

    for graph in graph_set.graphs:
        node_cycle_lengths = dfs2.run_dfs_on_graph(graph)
        if labels is not None:
            for nodeid in node_cycle_lengths:
                graph.set_vertex_next_label(nodeid, parameter.cyclealphabet.get_cycle_label(node_cycle_lengths[nodeid]))
                graph.set_vertex_next_label_to_full_label(nodeid)
                graph.set_vertex_next_label(nodeid, parameter.alphabet.get_label(0, graph.get_vertex_label(nodeid)))
                graph.set_vertex_label_to_next_label(nodeid)
        else:
            for nodeid in graph.graph:
                graph.set_vertex_label(nodeid,"0")

    return graph_set


def generate_graphs_with_cycle_labeling_overwrite(graph_indicator_file, A_file, labels_file):
    graph_indicator = []

    with open(graph_indicator_file, "r") as f:
        for line in f:
            graph_indicator.append(int(line.strip()))

    labels = []
    with open(labels_file, "r") as f:
        for line in f:
            labels.append(int(line.strip()))

    graph_set = GraphSet()
    graphs = {}
    with open(A_file, "r") as f:
        for line in f:
            node1, node2 = [int(x) for x in line.strip().split(",")]
            graph_id = graph_indicator[node1-1]
            if graph_id not in graphs:
                graphs[graph_id] = Graph(parameter.cyclealphabet)
                graph_set.add_graph(graphs[graph_id])

            graphs[graph_id].add_vertex(node1, str(labels[node1-1]))
            graphs[graph_id].add_vertex(node2, str(labels[node2-1]))

            graphs[graph_id].add_edge(node1, node2)

    for graph in graph_set.graphs:
        node_cycle_lengths = dfs2.run_dfs_on_graph(graph)
        for nodeid in node_cycle_lengths:
            overwrite_label = parameter.cyclealphabet.get_cycle_label(node_cycle_lengths[nodeid])
            if overwrite_label != 'c0':
                graph.set_vertex_label(nodeid, overwrite_label)

    return graph_set



def generate_master_graph(A_file):
    master_graph = Graph(parameter.cyclealphabet)

    with open(A_file, "r") as f:
        for line in f:
            node1, node2 = [int(x) for x in line.strip().split(",")]
            master_graph.add_vertex(node1, node1)
            master_graph.add_vertex(node2, node2)
            master_graph.add_edge(node1, node2)

    return master_graph


def delete_nodes(graph_set, degree_ratio):
    new_graph_set = GraphSet()
    for graph in graph_set.graphs:
        nodes_to_ignore = set()
        num_large_nodes = int(round(len(graph.vertices) * 0.25))
        large_degrees = sorted(graph.graph, key=lambda node: len(graph.graph[node]["neighbors"]), reverse=True)[:num_large_nodes]

        if degree_ratio != 0:
            for large_node in large_degrees:
                for neighbor in graph.graph[large_node]["neighbors"]:
                    neighbor_degree = len(graph.graph[neighbor]["neighbors"])
                    if neighbor_degree <= len(graph.graph[large_node]["neighbors"]) * degree_ratio:
                        nodes_to_ignore.add(neighbor)

        new_graph = Graph(parameter.cyclealphabet)
        for node in graph.vertices - nodes_to_ignore:
            new_graph.add_vertex(node, graph.get_vertex_label(node))
        for node in graph.vertices - nodes_to_ignore:
            for neighbor in graph.graph[node]["neighbors"]:
                if neighbor not in nodes_to_ignore:
                    new_graph.add_edge(node, neighbor)
        new_graph_set.add_graph(new_graph)

    return new_graph_set

