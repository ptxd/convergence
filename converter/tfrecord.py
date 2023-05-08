import tensorflow as tf
import numpy as np

def read_tfrecord(file_path):
    dataset = tf.data.TFRecordDataset(file_path)
    data = []
    for record in dataset:
        example = tf.train.Example()
        example.ParseFromString(record.numpy())
        feature = example.features.feature
        data.append(feature)
    return np.array(data)

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def write_tfrecord(file_path, data):
    with tf.io.TFRecordWriter(file_path) as writer:
        for row in data:
            feature = _bytes_feature(row.tobytes())
            example = tf.train.Example(features=tf.train.Features(feature={'data': feature}))
            writer.write(example.SerializeToString())