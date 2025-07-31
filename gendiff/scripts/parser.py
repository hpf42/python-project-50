import json


def get_file_path():
    path = input('Write path to file ')
    return path


def parse_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    print(data)


def main():
    path = get_file_path()
    parse_file(path)


if __name__ == "__main__":
    main()