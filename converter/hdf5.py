import h5py
import numpy as np

def read_hdf5(file_path):
    with h5py.File(file_path, 'r') as file:
        keys = list(file.keys())
        data = np.array(file[keys[0]])
    return data

def write_hdf5(file_path, data):
    with h5py.File(file_path, 'w') as file:
        file.create_dataset('data', data=data)

# Keep the existing read_hdf5 function
