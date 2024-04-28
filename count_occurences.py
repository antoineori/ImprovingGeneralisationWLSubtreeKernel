from parameter import *
from collections import Counter


count_zeros = True


def count_label_occurences_in_graph(graph, p_iteration):
    output = []
    labels = []
    for node_id in graph.graph:
        labels.append(int(parameter.alphabet.get_label(p_iteration, graph.get_vertex_label(node_id))))
    for alpha in parameter.alphabet.inverted_alphabet:
        c = labels.count(alpha)
        if count_zeros:
            output.append(labels.count(alpha))
        elif c != 0:
            output.append(labels.count(alpha))

    return output


def count_label_occurences_in_graph_v2(graph, p_iteration, zeros):
    output = []
    for i in range(zeros):
        output.append(0)
    labels = []
    for node_id in graph.graph:
        labels.append(int(parameter.alphabet.get_label(p_iteration, graph.get_vertex_label(node_id))))
    for alpha in parameter.alphabet.inverted_alphabet:
        c = labels.count(alpha)
        if count_zeros:
            output.append(labels.count(alpha))
        elif c != 0:
            output.append(labels.count(alpha))

    return output


def count_label_occurences_in_graph_history(graph):
    output = []
    for alpha in parameter.alphabet.inverted_alphabet:

        c = graph.count_in_history(alpha)
        if count_zeros:
            output.append(c)
        elif c != 0:
            output.append(c)
    return output
