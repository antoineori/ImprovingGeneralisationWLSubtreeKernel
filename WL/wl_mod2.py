from parameter import *
from count_occurences import count_label_occurences_in_graph_history
import numpy as np
from generate_graphs import delete_nodes

#Mod 2 deletes nodes that are considered not important to the graph

def wl_mod2(full_graphset, p_ratio=0.20):
    graphset = delete_nodes(full_graphset, p_ratio)

    for graph in graphset.graphs:
        for nodid in graph.graph:
            graph.append_history(graph.get_vertex_label(nodid))

    for iteration in range(max_iterations):
        for graph in graphset.graphs:
            for node_id in graph.graph:
                graph.set_vertex_next_label_to_full_label(node_id)

            for node_id in graph.graph:
                graph.set_vertex_label_to_next_label(node_id)

            for node_id in graph.graph:
                graph.set_vertex_next_label(node_id, parameter.alphabet.get_label(iteration, graph.get_vertex_label(node_id)))

            for node_id in graph.graph:
                graph.set_vertex_label_to_next_label(node_id)

        for graph in graphset.graphs:
            for node_id in graph.graph:
                graph.append_history(graph.get_vertex_label(node_id))

    output = []
    for iteration in range(max_iterations):
        iter_output =[]
        for graph in graphset.graphs:
            graph_iter_out = graph.count_label_occurences_in_graph_history(parameter.alphabet.inverted_alphabet, iteration+1)
            iter_output.append(graph_iter_out)
        iter_feature_vector = np.array(iter_output)
        iter_grammatrix = np.dot(iter_feature_vector, iter_feature_vector.transpose())
        output.append(iter_grammatrix)
    return output
