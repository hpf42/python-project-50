import argparse

from gendiff.scripts import generate_diff


def parser_function():
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
    return args 


def main():
    args = parser_function()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format
    result = generate_diff(first_file, second_file, format)
    print(result)


if __name__ == '__main__':
    main()