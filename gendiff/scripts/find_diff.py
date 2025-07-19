mport json
import os

import yaml


def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data(data, format):
    if format == 'json':
        return json.loads(data)
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    raise ValueError(f'Unsupported file format: {format}')


def parse_data_from_file(file_path):
    data = read_file(file_path)
    format = get_file_format(file_path)
    return parse_data(data, format)




    def item_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def item_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def items_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def items_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def items_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': find_diff(value1, value2)
    }


def find_diff(data1, data2):
    keys_union = data1.keys() | data2.keys()
    keys_added = data2.keys() - data1.keys()
    keys_deleted = data1.keys() - data2.keys()

    diff = []

    for key in keys_union:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in keys_added:
            diff.append(item_add(key, value2))
        elif key in keys_deleted:
            diff.append(item_delete(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(items_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(items_modified(key, value1, value2))
        else:
            diff.append(items_unchanged(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff