import parameter
from generate_graphs import generate_graphs, generate_graphs_with_cycle_labeling
from parameter import *
from WL.wl_mod1 import wl_mod1
from WL.wl_mod_cycle import wl_mod_cycle
from WL.wl_og import wl_og
from WL.wl_mod3 import wl_mod3
from WL.wl_mod4 import wl_mod4
from WL.wl_mod2 import wl_mod2
from kernel_evaluation import kernel_svm_evaluation
import aux_functions
import numpy as np
from tqdm import tqdm


def run_full_with_WL_with_progressbar(wl_mod, p1=None, p2=None):

    with tqdm(total=4, desc="Starting " + parameter.dataset_name + " process with %s" % wl_mod.__name__) as pbar:
        if wl_mod == wl_mod_cycle:
            graphset = generate_graphs_with_cycle_labeling(parameter.current_graph_indicator_file, parameter.current_A_file, parameter.current_node_labels_file)
        else:
            graphset = generate_graphs(parameter.current_graph_indicator_file, parameter.current_A_file, parameter.current_node_labels_file)
        pbar.update()
        if p1 is None:
            all_matrices = wl_mod(graphset)
        elif p2 is not None:
            all_matrices = wl_mod(graphset, p1, p2)
        else:
            all_matrices = wl_mod(graphset, p1)
        pbar.update()

        norm_all_matrices = aux_functions.normalize_list_of_gram_matrix2(all_matrices)
        pbar.update()

        classes = np.array(parameter.get_classes())
        num_reps = 5
        acc, s_1, s_2 = kernel_svm_evaluation(norm_all_matrices, classes, num_repetitions=num_reps, all_std=True)
        pbar.update()
    if p1 is None:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    elif p2 is not None:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + "parameters: " + str(p1) + " " + str(p2) + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    else:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + "parameters: " + str(p1) + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    return ret

def run_full_with_WL_with_cyclelabeling(wl_mod, p1=None, p2=None):

    with tqdm(total=4, desc="Starting " + parameter.dataset_name + " process with %s" % wl_mod.__name__) as pbar:

        graphset = generate_graphs_with_cycle_labeling(parameter.current_graph_indicator_file, parameter.current_A_file, parameter.current_node_labels_file)

        pbar.update()
        if p1 is None:
            all_matrices = wl_mod(graphset)
        elif p2 is not None:
            all_matrices = wl_mod(graphset, p1, p2)
        else:
            all_matrices = wl_mod(graphset, p1)
        pbar.update()

        norm_all_matrices = aux_functions.normalize_list_of_gram_matrix2(all_matrices)
        pbar.update()

        classes = np.array(parameter.get_classes())
        num_reps = 5
        acc, s_1, s_2 = kernel_svm_evaluation(norm_all_matrices, classes, num_repetitions=num_reps, all_std=True)
        pbar.update()
    if p1 is None:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    elif p2 is not None:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + "parameters: " + str(p1) + " " + str(p2) + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    else:
        ret = str(parameter.dataset_name + " using " + wl_mod.__name__ + "parameters: " + str(p1) + ": " + str(acc) + " " + str(s_1) + " " + str(s_2))
    return ret


def run_all_mods():
    param = "Dataset: " + parameter.dataset_name + " - Iterations: " + str(max_iterations)
    data_og = run_full_with_WL_with_progressbar(wl_og)
    data_mod1 = "0.9 " + run_full_with_WL_with_progressbar(wl_mod1, 90)
    data_mod12 = "0.85 " + run_full_with_WL_with_progressbar(wl_mod1, 85)
    data_mod13 = "0.8 " + run_full_with_WL_with_progressbar(wl_mod1, 80)
    data_mod2 = "0.25 " + run_full_with_WL_with_progressbar(wl_mod2, 0.25)
    data_mod22 = "0.2 " + run_full_with_WL_with_progressbar(wl_mod2, 0.2)
    data_mod23 = "0.15 " + run_full_with_WL_with_progressbar(wl_mod2, 0.15)
    data_mod3 = "0.25 " + run_full_with_WL_with_progressbar(wl_mod3, 0.25)
    data_mod32 = "0.2 " + run_full_with_WL_with_progressbar(wl_mod3, 0.2)
    data_mod33 = "0.15 " + run_full_with_WL_with_progressbar(wl_mod3, 0.15)
    data_mod4 = "1 2 " + run_full_with_WL_with_progressbar(wl_mod4, 1, 2)
    data_mod42 = "1 3 " + run_full_with_WL_with_progressbar(wl_mod4, 1, 3)
    data_mod43 = "2 2 " + run_full_with_WL_with_progressbar(wl_mod4, 2, 2)
    #data_mod44 = "2 3 " + run_full_with_WL_with_progressbar(wl_mod4, 2, 3)
    data_mod_cycle = run_full_with_WL_with_progressbar(wl_mod_cycle)
    data = [param
            , data_og
            , data_mod1
            , data_mod12
            , data_mod13
            , data_mod23
            , data_mod22
            , data_mod2
            , data_mod33
            , data_mod32
            , data_mod3
            , data_mod4
            , data_mod42
            , data_mod43
            , data_mod_cycle
        , "----------------------------------------"]

    resultdatafile = "Result_Data/data"+str(max_iterations)+".txt"
    testingdatafile = "Result_Data/data_testing.txt"
    with open(testingdatafile, mode="a") as text_file:
        for line in data:
            text_file.write(line + "\n")


#for i in range(len(parameter.dataset_list)):
 #   run_all_mods()
  #  parameter.next_dataset_parameter()


print(run_full_with_WL_with_progressbar(wl_mod_cycle))

