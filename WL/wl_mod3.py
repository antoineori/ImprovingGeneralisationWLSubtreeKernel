from parameter import *
from count_occurences import count_label_occurences_in_graph_history
import numpy as np

#Mod 3 labels the non important nodes, by degree ration, as such, instead of deleting them like mod 2, this makes fir more common relabeling

def wl_mod3(graphset, degree_ratio=0.25):
    min_iteration = 2

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

        # Loop to label non-important nodes
            if iteration+1 >= min_iteration:
                for graph in graphset.graphs:
                    num_large_nodes = int(round(len(graph.vertices) * 0.35))
                    large_degrees = sorted(graph.graph, key=lambda node: len(graph.graph[node]["neighbors"]), reverse=True)[:num_large_nodes]
                    for node_id in large_degrees:
                        neighbors = graph.graph[node_id]["neighbors"]
                        degree = graph.get_degree_of_vertex(node_id)
                        for neighbor in neighbors:
                            if graph.get_degree_of_vertex(neighbor) < degree * degree_ratio:
                                graph.set_vertex_label(neighbor, parameter.alphabet.get_label(iteration, "999"))

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
