from Classes.alphabet import Alphabet
from Classes.CycleLabelAlphabet import CycleLabelAlphabet


#list_dataset_names = ["COIL-DEL", "COX2", "COX2_MD", "dblp_ct1", "dblp_ct2", "DD", "DHFR",
#                      "DHFR_MD", "ER_MD", "facebook_ct1", "facebook_ct2", "Fingerprint", "FRANKENSTEIN",
#                      "highschool_ct1", "highschool_ct2", "Letter-high", "Letter-low", "Letter-med", "MUTAG",
#                      "Mutagenicit", "NCI1", "NCI109", "PROTEINS", "PTC_FM", "PTC_FR", "PTC_MM", "PTC_MR",
#                      "REDDIT-BINARY", "SYNTHETICnew", "Synthie"]
#dataset_name = "AIDS"
#current_A_file = "DataSets/"+dataset_name+"/"+dataset_name+"_A.txt"
#current_graph_indicator_file = "DataSets/"+dataset_name+"/"+dataset_name+"_graph_indicator.txt"
#
#alphabet = Alphabet()
#cyclealphabet = CycleLabelAlphabet()

max_iterations = 3
max_nodes_per_graph = 100


class Parameter:
    def __init__(self, max_cycle_length=8):
        self.i = 0
        self.dataset_list = ["NCI1"]
        self.dataset_name = self.dataset_list[self.i]
        self.current_A_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_A.txt"
        self.current_graph_indicator_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_graph_indicator.txt"
        self.current_node_labels_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_node_labels.txt"
        self.alphabet = Alphabet()
        self.cyclealphabet = CycleLabelAlphabet(max_cycle_length)

    def next_dataset_parameter(self):
        self.i += 1
        if self.i < len(self.dataset_list):
            self.dataset_name = self.dataset_list[self.i]
            self.current_A_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_A.txt"
            self.current_graph_indicator_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_graph_indicator.txt"
            self.current_node_labels_file = "DataSets/"+self.dataset_name+"/"+self.dataset_name+"_node_labels.txt"
            self.alphabet = Alphabet()
            self.cyclealphabet = CycleLabelAlphabet()

    def get_amount_of_nodes_total(self):
        count = 0
        with open(self.current_graph_indicator_file, 'r') as f:
            for line in f:
                if line.strip():
                    count += 1
        return count

    def get_classes(self):
        clases = []
        with open("DataSets/"+self.dataset_name+"/"+self.dataset_name+"_graph_labels.txt", "r") as f:
            for line in f:
                clases.append(int(line))
        return clases


parameter = Parameter()


def count_nonempty_lines(file_path):
    count = 0
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                count += 1
    return count

#amount_of_nodes_total = count_nonempty_lines(current_graph_indicator_file)



"""
List of datasets used: ["AIDS","PROTEINS","MUTAG","COIL-DEL","NCI1","COLLAB","IMDB-BINARY","SYNTHETICnew","Mutagenicity"]
"""


"""
["AIDS", "BZR", "BZR_MD", "COX2", "COX2_MD", "dblp_ct1", "dblp_ct2", "DD", "DHFR",
                      "DHFR_MD", "ER_MD", "facebook_ct1", "facebook_ct2", "Fingerprint", "FRANKENSTEIN",
                      "highschool_ct1", "highschool_ct2", "Letter-high", "Letter-low", "Letter-med", "MUTAG",
                      "Mutagenicit", "NCI1", "NCI109", "PROTEINS", "PTC_FM", "PTC_FR", "PTC_MM", "PTC_MR",
                      "REDDIT-BINARY", "SYNTHETICnew", "Synthie"]
"""

"""
["AIDS", "BZR", "BZR_MD", "COX2", "COX2_MD","DHFR_MD", "MUTAG", "PROTEINS", "PTC_FM", "PTC_MM"]
"""