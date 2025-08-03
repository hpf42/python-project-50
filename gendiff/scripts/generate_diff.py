from gendiff.formatters.get_format import get_format
from gendiff.scripts.file_parser import parse_data_from_file
from gendiff.scripts.find_diff import find_diff


def generate_diff(file_1, file_2, formatter='stylish'):
    parsed_file_1 = parse_data_from_file(file_1)
    parsed_file_2 = parse_data_from_file(file_2)
    final_diff = find_diff(parsed_file_1, parsed_file_2)
    return get_format(final_diff, formatter)