import json
import os


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data(data):
    return json.loads(data)


def parse_data_from_file(file_path):
    data = read_file(file_path)
    return parse_data(data)