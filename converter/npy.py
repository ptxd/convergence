import numpy as np

def read_npy(file_path):
    return np.load(file_path)

def write_npy(file_path, data):
    np.save(file_path, data)