

iteration1 = {1:1, 2:2, 3:2, 4:1, 5:2, 7:2, 6:10}
iteration2 = {1:5, 2:3, 3:5, 4:10, 5:3, 7:6}

identical_labels = []
ignore_iteration = 2

iterations = [iteration1,iteration2]

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
            if all(item in master for item in p_list):
                new_node_lists.append(p_list)
                break
    node_lists = new_node_lists

print(node_lists)

