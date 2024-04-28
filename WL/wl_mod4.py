from parameter import *
import numpy as np
import generate_graphs


def wl_mod4(graphset, min_iteration=2, ignore_iteration=2):

    #for graph in graphset.graphs:
    #    for nodid in graph.graph:
    #        graph.append_history(graph.get_vertex_label(nodid))

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

            if iteration+1 >= min_iteration + ignore_iteration:

                iterations = graph.get_latest_x_hisory_iterations(ignore_iteration)
                label_nodes = {}
                for nodeid, label in iterations[0].items():
                    if label not in label_nodes:
                        label_nodes[label] = []
                    label_nodes[label].append(nodeid)
                node_lists = [lst for lst in label_nodes.values() if len(lst) > 1]

                for iter in iterations[1:]:
                    iter_label_nodes = {}
                    for nodeid, label in iter.items():
                        if label not in iter_label_nodes:
                            iter_label_nodes[label] = []
                        iter_label_nodes[label].append(nodeid)
                    iter_node_lists = [lst for lst in iter_label_nodes.values() if len(lst) > 1]

                    new_node_lists = []
                    for p_list in iter_node_lists:
                        for master in node_lists:
                            #if all(item in master for item in p_list):
                            if len(list(set(p_list).intersection(master))) > 0:
                                new_node_lists.append(list(set(p_list).intersection(master)))
                                break
                    node_lists = new_node_lists

                for plist in node_lists:
                    for nodeid in plist:
                        if nodeid not in graph.nodeids_marked_unimportant:
                            graph.add_nodeids_marked_unimportant(nodeid)

                #for node_id in graph.nodeids_marked_unimportant:
                #    if node_id in graph.graph:
                #        graph.set_vertex_label(node_id, "999")

        for graph in graphset.graphs:
            graph.new_history_iteration()
            for node_id in graph.graph:
                node_label = graph.get_vertex_label(node_id)
                graph.append_history(node_label)
                graph.add_to_latest_history_iteration(node_id, node_label)

#WL with info reruns
    list_unimportant_nodes = []
    for graph in graphset.graphs:
        for nid in graph.nodeids_marked_unimportant:
            list_unimportant_nodes.append(nid)

    graphset = generate_graphs.generate_graphs(parameter.current_graph_indicator_file, parameter.current_A_file, parameter.current_node_labels_file)
    for graph in graphset.graphs:
        for nodid in graph.graph:
            graph.append_history(graph.get_vertex_label(nodid))

    for iteration in range(max_iterations):
        for graph in graphset.graphs:

            for node_id in graph.graph:
                if iteration+1 < min_iteration:
                    graph.set_vertex_next_label_to_full_label(node_id)
                if node_id not in list_unimportant_nodes and iteration+1 >= min_iteration:
                    graph.set_vertex_next_label_to_full_label(node_id)

            for node_id in graph.graph:
                if iteration+1 < min_iteration:
                    graph.set_vertex_label_to_next_label(node_id)
                if node_id not in list_unimportant_nodes and iteration+1 >= min_iteration:
                    graph.set_vertex_label_to_next_label(node_id)

            for node_id in graph.graph:
                if iteration+1 < min_iteration:
                    graph.set_vertex_next_label(node_id, parameter.alphabet.get_label(iteration, graph.get_vertex_label(node_id)))
                if node_id not in list_unimportant_nodes and iteration+1 >= min_iteration:
                    graph.set_vertex_next_label(node_id, parameter.alphabet.get_label(iteration, graph.get_vertex_label(node_id)))

            for node_id in graph.graph:
                if iteration+1 < min_iteration:
                    graph.set_vertex_label_to_next_label(node_id)
                if node_id not in list_unimportant_nodes and iteration+1 >= min_iteration:
                    graph.set_vertex_label_to_next_label(node_id)
                elif node_id in list_unimportant_nodes and iteration+1 >= min_iteration:
                    graph.set_vertex_label(node_id, "999")

        for graph in graphset.graphs:
            for node_id in graph.graph:
                graph.append_history(graph.get_vertex_label(node_id))

    output = []
    for iteration in range(max_iterations):
        iter_output = []
        for graph in graphset.graphs:
            graph_iter_out = graph.count_label_occurences_in_graph_history(parameter.alphabet.inverted_alphabet, iteration+1)
            iter_output.append(graph_iter_out)
        iter_feature_vector = np.array(iter_output)
        iter_grammatrix = np.dot(iter_feature_vector, iter_feature_vector.transpose())
        output.append(iter_grammatrix)
    return output


