import json
import os
import yaml


def get_file_format(file_path):
    format = os.path.splitext(file_path)[1:]
    return format


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data(data, format):
    if format == 'json':
        return json.loads(data)
    elif format == 'yaml':
        return yaml.loads(data)
    else:
        print('Cannot read the file!')


def parse_data_from_file(file_path):
    data = read_file(file_path)
    return parse_data(data)