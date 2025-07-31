import argparse

from gendiff.scripts.file_parser import parse_data_from_file
from gendiff.scripts.find_diff import find_diff


def generate_diff(file_1, file_2, formatter='stylish') -> str:
    parsed_file_1 = parse_data_from_file(file_1)
    parsed_file_2 = parse_data_from_file(file_2)
    final_diff = find_diff(parsed_file_1, parsed_file_2)
    return f"{final_diff}, {formatter}"


def main():
    print('Start')
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    print(
        f'Comparing: {args.first_file} \
            vs {args.second_file}, \
            format: {args.format}')
    print('Finish')


if __name__ == '__main__':
    main()