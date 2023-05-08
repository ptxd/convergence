import numpy as np

def save_binary(file_path, data):
    with open(file_path, 'wb') as binary_file:
        for item in data:
            binary_file.write(item.tobytes())

def load_binary(file_path, dtype, shape):
    data = np.fromfile(file_path, dtype=dtype)
    return data.reshape(shape)

