from converter import convert_from_binary

target_format = 'csv'  # or any other supported format: json, hdf5, caffemodel, npy, npz, tfrecord
source_file = 'path/to/source/file.bin'  # Path to the binary source file
target_file = 'path/to/target/file.csv'  # Path to the target file
dtype = 'float64'  # Data type of the elements in the binary file, e.g., float64, int32
shape = (100, 5)  # Shape of the data in the binary file, e.g., (100, 5) for 100 rows and 5 columns

convert_from_binary(target_format, source_file, target_file, dtype, shape)



from converter import convert_json, convert_to_json

source_file = 'path/to/source/file.json'
target_file = 'path/to/target/file.csv'
target_format = 'csv'  # or any other supported format: hdf5, caffemodel, npy, npz, tfrecord, binary

# Convert from JSON to the target format
convert_json(source_file, target_file, target_format)

source_file = 'path/to/source/file.csv'
source_format = 'csv'  # or any other supported format: hdf5, caffemodel, npy, npz, tfrecord, binary
target_file = 'path/to/target/file.json'

# Convert from the source format to JSON
convert_to_json(source_format, source_file, target_file)


from converter import convert_csv

source_file = 'path/to/source/file.csv'
target_file = 'path/to/target/file.h5'
target_format = 'hdf5'

convert_csv(source_file, target_file, target_format)

