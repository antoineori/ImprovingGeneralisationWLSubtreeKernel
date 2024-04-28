import numpy as np
from scipy import sparse as sp
import math as m

def correct_occ_array_single(p_array):
    #maxlen = len(p_array[-1])
    maxlen = 600
    out_array = []
    for l in p_array:
        temp_l = l
        diff = maxlen - len(l)
        if diff > 0:
            for i in range(diff):
                temp_l.append(0)
        out_array.append(temp_l)
    return out_array


def correct_occ_array(full_array):
    out = []
    for arr in full_array:
        out.append(correct_occ_array_single(arr))
    return out


def normalize_list_of_gram_matrix(list_gram_matrix):
    output = []
    for gm in list_gram_matrix:
        output.append(normalize_gram_matrix(gm))
    return output


#Von Christopher Morris:
# Cosine normalization for a gram matrix.
def normalize_gram_matrix(gram_matrix):
    n = gram_matrix.shape[0]
    gram_matrix_norm = np.zeros([n, n], dtype=np.float64)

    for i in range(0, n):
        for j in range(i, n):
            if not (gram_matrix[i][i] == 0.0 or gram_matrix[j][j] == 0.0):
                g = gram_matrix[i][j] / m.sqrt(gram_matrix[i][i] * gram_matrix[j][j])
                gram_matrix_norm[i][j] = g
                gram_matrix_norm[j][i] = g

    return gram_matrix_norm


# Cosine normalization for sparse feature vectors, i.e., \ell_2 normalization.
def normalize_feature_vector(feature_vectors):
    n = feature_vectors.shape[0]

    for i in range(0, n):
        norm = sp.linalg.norm(feature_vectors[i])
        feature_vectors[i] = feature_vectors[i] / norm

    return feature_vectors





def normalize_list_of_gram_matrix2(list_gram_matrix):
    output = []
    for gm in list_gram_matrix:
        output.append(normalize_gram_matrix2(gm))
    return output

def normalize_gram_matrix2(gram_matrix):
    n = gram_matrix.shape[0]
    gram_matrix_norm = np.zeros([n, n], dtype=np.float64)
    epsilon = 1e-10  # Small value to avoid math domain error

    for i in range(0, n):
        for j in range(i, n):
            if not (gram_matrix[i][i] == 0.0 or gram_matrix[j][j] == 0.0):
                g = gram_matrix[i][j] / m.sqrt((gram_matrix[i][i] + epsilon) * (gram_matrix[j][j] + epsilon))
                gram_matrix_norm[i][j] = g
                gram_matrix_norm[j][i] = g

    return gram_matrix_norm

