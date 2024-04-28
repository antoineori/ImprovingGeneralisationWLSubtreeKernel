

def dfs_cycle(u, p, color: list, par: list, p_graph, p_cycles, cyclenumber):

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
        # in the current cycle thats found
        while cur != u:
            cur = par[cur]
            v.append(cur)
        p_cycles[cyclenumber] = v
        cyclenumber += 1

        return

    par[u] = p

    # partially visited.
    color[u] = 1

    # simple dfs on graph
    for v in p_graph[u]:

        # if it has not been visited previously
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, par, p_graph, p_cycles, cyclenumber)

    # completely visited.
    color[u] = 2

    return p_cycles

def addEdge(u, v, p_graph):
    p_graph[u].append(v)

def convert_to_p_graph(graph):
    p_graph = [[]]
    id_mapping = {}

    # Assign new ids to the vertices
    for i, vertex in enumerate(sorted(graph.vertices), start=1):
        id_mapping[i] = vertex
        p_graph.append([])

    # Add edges to the p_graph using the new ids
    for vertex in graph.vertices:
        new_id = list(id_mapping.keys())[list(id_mapping.values()).index(vertex)]
        for neighbor in graph.graph[vertex]["neighbors"]:
            new_neighbor_id = list(id_mapping.keys())[list(id_mapping.values()).index(neighbor)]
            addEdge(new_id, new_neighbor_id, p_graph)

    return p_graph, id_mapping


def run_dfs_on_graph(p_graph):
    graph, mapping = convert_to_p_graph(p_graph)
    color = [0] * len(graph)
    par = [0] * len(graph)
    cycles = [[] for i in range(len(graph))]
    cyclenumber = 0
    cycles = dfs_cycle(1, 0, color, par, graph, cycles, cyclenumber)
    cycles = [lst for lst in cycles if lst]

    node_lengths = {mapping[key]: [] for key in range(1, len(graph))}

    for lst in cycles:
        for node_id in lst:
            original_node_id = mapping[node_id]
            node_lengths[original_node_id].append(len(lst))

    return node_lengths

