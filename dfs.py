import parameter
from Classes.Graph import Graph
from Classes.GraphSet import GraphSet
from Classes.CycleLabelAlphabet import CycleLabelAlphabet
from parameter import *

N = 1000000

# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]


# Function to mark the vertex with
# different colors for different cycles
def dfs_cycle(u, p, color: list, par: list):
    global cyclenumber

    # already (completely) visited vertex.
    if color[u] == 2:
        return

    # seen vertex, but was not
    # completely visited -> cycle detected.
    # backtrack based on parents to
    # find the complete cycle.
    if color[u] == 1:
        v = []
        cur = p
        v.append(cur)

        # backtrack the vertex which are
        # in the current cycle that's found
        while cur != u:
            cur = par[cur]
            v.append(cur)
        cycles[cyclenumber] = v
        cyclenumber += 1

        return

    par[u] = p

    # partially visited.
    color[u] = 1

    # simple dfs on graph
    #for v in graph.get_adjacent_vertices(u):
    for v in graph[u]:

        # if it has not been visited previously
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, par)

    # completely visited.
    color[u] = 2

# add the edges to the graph
def addEdge(u, v):
    graph[u].append(v)
    #graph[v].append(u)

# Function to print the cycles
def printCycles():
    if cyclenumber == 0:
        print("No cycles")
    # print all the vertex with same cycle
    for i in range(0, cyclenumber):

        # Print the i-th cycle
        print("Cycle Number %d:" % (i+1), end = " ")
        for x in cycles[i]:
            print(x, end = " ")
        print()

def convert_to_list(graph):
    graph_list = [[] for _ in range(1000000)]
    for vertex in graph.graph:
        if vertex in graph.graph:
            neighbors = graph.graph[vertex]["neighbors"]
            for neighbor in neighbors:
                graph_list[vertex].append(neighbor)
                graph_list[neighbor].append(vertex)
    return graph_list


def convert_set_to_list(graphset):
    graph_list = [[] for _ in range(1000000)]
    for graph in graphset.graphs:
        for vertex in graph.graph:
            if vertex in graph.graph:
                neighbors = graph.graph[vertex]["neighbors"]
                for neighbor in neighbors:
                    graph_list[vertex].append(neighbor)
                    graph_list[neighbor].append(vertex)
        return graph_list


def master_graph(A_file):
    with open(A_file, "r") as f:
        for line in f:
            node1, node2 = [int(x) for x in line.strip().split(",")]
            addEdge(node1, node2)


master_graph(parameter.current_A_file)

# arrays required to color the
# graph, store the parent of node
color = [0] * len(graph)
par = [0] * len(graph)

# store the numbers of cycle
cyclenumber = 0

# call DFS to mark the cycles
for i in range(1, N):
    dfs_cycle(i, 0, color, par)

#printCycles()

cycles = [lst for lst in cycles if lst]

# create an empty dictionary to store the lengths of the lsts
node_lengths = {key: [] for key in range(1, parameter.get_amount_of_nodes_total()+1)}

# loop over each list in the list of lists
for lst in cycles:
    # loop over each node ID in the current list
    for node_id in lst:
        # if the node ID is not in the dictionary, add it with an empty list
        if node_id not in node_lengths:
            node_lengths[node_id] = []
        # add the length of the current list to the list for the current node ID
        node_lengths[node_id].append(len(lst))

