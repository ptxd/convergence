import numpy as np
from caffe.proto import caffe_pb2
import google.protobuf.text_format as txtf

def read_caffemodel(file_path):
    model = caffe_pb2.NetParameter()
    with open(file_path, 'r') as file:
        txtf.Merge(file.read(), model)
    return np.array(model)

def write_caffemodel(file_path, data):
    model = caffe_pb2.NetParameter()
    txtf.Merge(str(data), model)
    with open(file_path, 'w') as file:
        file.write(txtf.MessageToString(model))

# Keep the existing read_caffemodel function

