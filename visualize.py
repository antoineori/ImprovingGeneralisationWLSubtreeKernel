import os
from parameter import parameter
import math
from generate_graphs import generate_graphs, generate_graphs_with_cycle_labeling
import networkx as nx
import matplotlib.pyplot as plt


def read_graph_indicator_file(graph_label_file):
    graph_labels = []
    with open(graph_label_file, "r") as f:
        for line in f:
            graph_labels.append(int(line.strip()))
    print(graph_labels)
    return graph_labels

def visualize_graphs(graphset, graph_label_file="DataSets/"+parameter.dataset_name+"/"+parameter.dataset_name+"_graph_labels.txt", output_directory="graphs"):
    graph_labels = read_graph_indicator_file(graph_label_file)
    graph_id = 0
    for graph in graphset.graphs:
        graph_id += 1
        graph_label = graph_labels[graph_id-1]
        graph_output_directory = os.path.join(output_directory, str(graph_label))


        # Create a NetworkX graph
        G = nx.Graph()

        # Add nodes and edges
        for vertex in graph.vertices:
            G.add_node(vertex, label=graph.get_vertex_label(vertex))

        for vertex in graph.vertices:
            neighbors = graph.get_adjacent_vertices(vertex)
            for neighbor in neighbors:
                if vertex < neighbor:
                    G.add_edge(vertex, neighbor)

        # Draw the graph
        plt.figure()
        pos = nx.spring_layout(G, seed=42)  # Spring layout
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10)
        nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, 'weight'))
        plt.title(f"Graph {graph_id}")
        #plt.show()
        plt.savefig(f"{graph_label}/graph_{graph_id}.png", format="PNG")
        print(f"{graph_label} id: {graph_id}")

        plt.close()



graphset = generate_graphs(parameter.current_graph_indicator_file, parameter.current_A_file, parameter.current_node_labels_file)
visualize_graphs(graphset)
