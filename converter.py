from converter import binary, csv, json, hdf5, caffemodel, npy, npz, tfrecord

def convert_to_binary(source_format, source_file, target_file):
    if source_format == 'csv':
        data = csv.read_csv(source_file)
    elif source_format == 'json':
        data = json.read_json(source_file)
    elif source_format == 'hdf5':
        data = hdf5.read_hdf5(source_file)
    elif source_format == 'caffemodel':
        data = caffemodel.read_caffemodel(source_file)
    elif source_format == 'npy':
        data = npy.read_npy(source_file)
    elif source_format == 'npz':
        data = npz.read_npz(source_file)
    elif source_format == 'tfrecord':
        data = tfrecord.read_tfrecord(source_file)
    else:
        raise ValueError(f"Unsupported source format: {source_format}")

    binary.save_binary(target_file, data)

def convert_from_binary(target_format, source_file, target_file, dtype, shape):
    data = binary.load_binary(source_file, dtype, shape)

    if target_format == 'csv':
        csv.write_csv(target_file, data)
    elif target_format == 'json':
        json.write_json(target_file, data)
    elif target_format == 'hdf5':
        hdf5.write_hdf5(target_file, data)
    elif target_format == 'caffemodel':
        caffemodel.write_caffemodel(target_file, data)
    elif target_format == 'npy':
        npy.write_npy(target_file, data)
    elif target_format == 'npz':
        npz.write_npz(target_file, data)
    elif target_format == 'tfrecord':
        tfrecord.write_tfrecord(target_file, data)
    else:
        raise ValueError(f"Unsupported target format: {target_format}")
