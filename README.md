# ImprovingGeneralisationWLSubtreeKernel

DOI: 10.5281/zenodo.11081253

Bachelor thesis on Improving the Generalisation Performance of the Weisfeiler-Lehman Subtree Kernel

The results that were computed are kept in the excel file "results"

To run with your own dataset or parameters:
- in main run: run_full_with_WL_with_progressbar(<wl algorithm you want to use>, <hyperparameters>)
- in parameter in the class Parameter, change self.dataset_list to ["<name of dataset>"]

Be aware, the code is not memory optimized, you will need a lot RAM to run the very large datasets. (the small/medium ones should not be an issue)
---------------------------------------------------------------------------------------------------
The datasets available in the project were made available by my tutor, Christopher Morris, from graphlearning.io :

@inproceedings{Morris+2020,
    title={TUDataset: A collection of benchmark datasets for learning with graphs},
    author={Christopher Morris and Nils M. Kriege and Franka Bause and Kristian Kersting and Petra Mutzel and Marion Neumann},
    booktitle={ICML 2020 Workshop on Graph Representation Learning and Beyond (GRL+ 2020)},
    archivePrefix={arXiv},
    eprint={2007.08663},
    url={www.graphlearning.io},
    year={2020}
}