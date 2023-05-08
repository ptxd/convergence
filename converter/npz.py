import numpy as np

def read_npz(file_path):
    with np.load(file_path) as data:
        return data['arr_0']

def write_npz(file_path, data):
    np.savez(file_path, data)
