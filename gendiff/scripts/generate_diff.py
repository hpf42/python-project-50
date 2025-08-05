from gendiff.formatters.format_identifier import format_identifier
from gendiff.scripts.find_diff import find_diff
from gendiff.scripts.parser import parse_data_from_file


def generate_diff(file_path_1, file_path_2, formatter='stylish'):
    first_file = parse_data_from_file(file_path_1)
    second_file = parse_data_from_file(file_path_2)
    diff = find_diff(first_file, second_file)
    return format_identifier(diff, formatter)