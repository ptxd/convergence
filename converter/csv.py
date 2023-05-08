import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path).values

def write_csv(file_path, data):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

# Keep the existing read_csv function

