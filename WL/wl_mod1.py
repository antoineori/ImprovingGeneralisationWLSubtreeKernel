from parameter import *
import numpy as np

#Mod1 is compairing the new labels in a fuzzy way so that similar labels get regrouped: b,bbb = b,bbbb

#how_fuzzy = 90 #parameter in percent of similarity accepted, 1 is identicals only, 0 is everything is the same

def wl_mod1(graphset, how_fuzzy=90):

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
                graph.set_vertex_next_label(node_id, parameter.alphabet.get_fuzzy_label(iteration, graph.get_vertex_label(node_id), how_fuzzy))

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




"""    output = []
    for graph in graphset.graphs:
        
        temp_out = count_label_occurences_in_graph_history(graph)
        output.append(temp_out)

    feature_vector = np.array(output)
    grammatrix = np.dot(feature_vector, feature_vector.transpose())



    return grammatrix"""