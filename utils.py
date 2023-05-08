import os
import json

def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def create_directory_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def check_supported_extensions(file_path, supported_extensions):
    _, file_extension = os.path.splitext(file_path)
    if file_extension not in supported_extensions:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: {supported_extensions}")
