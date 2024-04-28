README for data set SF-295

=== Usage ===

This folder contains the following comma separated text files 
(replace DS by the name of the dataset):

n = total number of nodes
m = total number of edges
N = number of graphs

(1) 	DS_A.txt (m lines) 
	sparse (block diagonal) adjacency matrix for all graphs,
	each line corresponds to (row, col) resp. (node_id, node_id)

(2) 	DS_graph_indicator.txt (n lines)
	column vector of graph identifiers for all nodes of all graphs,
	the value in the i-th line is the graph_id of the node with node_id i

(3) 	DS_graph_labels.txt (N lines) 
	class labels for all graphs in the dataset,
	the value in the i-th line is the class label of the graph with graph_id i

(4) 	DS_node_labels.txt (n lines)
	column vector of node labels,
	the value in the i-th line corresponds to the node with node_id i

There are OPTIONAL files if the respective information is available:

(5) 	DS_edge_labels.txt (m lines; same size as DS_A_sparse.txt)
	labels for the edges in DS_A_sparse.txt 

(6) 	DS_edge_attributes.txt (m lines; same size as DS_A.txt)
	attributes for the edges in DS_A.txt 

(7) 	DS_node_attributes.txt (n lines) 
	matrix of node attributes,
	the comma seperated values in the i-th line is the attribute vector of the node with node_id i

(8) 	DS_graph_attributes.txt (N lines) 
	regression values for all graphs in the dataset,
	the value in the i-th line is the attribute of the graph with graph_id i


=== Node Label Conversion === 
Node labels were converted to integer values using this map:

Component 0:
O 0
N 1
C 2
S 3
Cl 4
P 5
F 6
Na 7
Pt 8
Ni 9
Zn 10
Mn 11
Sn 12
Br 13
Cu 14
Co 15
Se 16
Au 17
K 18
Pb 19
Ge 20
Nd 21
I 22
Si 23
B 24
Pd 25
La 26
Ce 27
Ru 28
Fe 29
Cr 30
Ga 31
Ac 32
Y 33
Ti 34
Eu 35
Tl 36
Zr 37
Hf 38
In 39
Sm 40
Gd 41
Dy 42
U 43
Ir 44
Re 45
Li 46
As 47
Sb 48
Bi 49
W 50
Hg 51
Mg 52
Rh 53
Os 54
Th 55
Mo 56
Nb 57
Ta 58
Ag 59
Cd 60
Er 61
V 62
Te 63
Al 64



Edge labels were converted to integer values using this map:

Component 0:
	0	1
	1	2
	2	3

=== References ===
Source: https://sites.cs.ucsb.edu/~xyan/dataset.htm

PubChem website (http://pubchem.ncbi.nlm.nih.gov).  PubChem provides information on the biological activities of small molecules, containing the bioassay records for anti-cancer screen tests with different cancer cell lines. Each dataset belongs to a certain type of cancer screen with the outcome active or inactive. From these screen tests, we collected 11 graph datasets with active and inactive labels.

Name 	Assay  ID 	Size 	Tumor Description
MCF-7 	83 	27770 	Breast
MOLT-4 	123 	39765 	Leukemia
NCI-H23 	1 	40353 	Non-Small Cell Lung
OVCAR-8 	109 	40516 	 Ovarian
P388 	330 	41472 	Leukemia
PC-3 	41 	27509 	Prostate
SF-295 	47 	40271 	Central Nerv Sys
SW-620 	81 	40532 	Colon
SN12C 	145 	40004 	Renal
UACC-257 	33 	39988 	Melanoma
Yeast 167 	167 	79601 	Yeast anticancer


