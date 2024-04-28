Introduction
Graphs have become a ubiquitous way of representing data and relations, ranging from social networks and web pages with hyperlinks to the structure of chemical components and bioinformatics. Developing competent tools to work and use said graph structured data is therefore considered highly beneficial. One scientific approach that has proven not only powerful but also extremely effective in numerous fields is machine learning.

To create machine learning models capable of efficiently working with graphs, new techniques need to be invented. Graph kernels and graph neural networks are some of the distinguished methods for machine learning graphs. Among these methods, the Weisfeiler-Lehman algorithm is one popular approach for applying machine learning to graphs.

To address this use case with a different angle, this paper will explore several modifications to the Weisfeiler-Lehman algorithm. These modifications aim to improve to generalization performance of the Weisfeiler-Lehman algorithm, while keeping or even improving the efficiency compared to the original Weisfeiler-Lehman. The modifications include:


- Fuzzy Label Compression, which introduces a tunable tolerance for label similarity using the Levenshtein distance.

- Neighborhood Pruning, which selectively removes less important neighbors from the graph to improve computational efficiency.

- Degree Ratio-based Importance, which generalizes node labels by identifying less important neighbors and representing them with a common label.

- Unchanging Node Group Pruning, which identifies and prunes groups of nodes with unchanging labels over multiple iterations.

- Cycle Labeling, which enhances the node labeling process by incorporating cycle information into the labels.


By building on the strengths of the Weisfeiler-Lehman algorithm and by trying to improve it's generalization, these modifications have the potential to significantly improve the accuracy and scalability of graph analysis tasks. Different techniques for label compression, neighborhood pruning and cycle labeling will be used to determine the most effective approach. The performance of the modified algorithm with and without the removal of small, unimportant neighbors will be evaluated to determine its effectiveness in reducing the complexity of a graph without loosing its core structure. The combination of different modifications will also be considered, as it might find a good balance of the algorithm for given tasks. Overall, these modifications aim to lower the expressiveness of more complex graph kernels while keeping or improving the efficiency of the original Weisfeiler-Lehman algorithm.


Author: Antoine Origer - ORCID ID 0009-0006-7102-8571