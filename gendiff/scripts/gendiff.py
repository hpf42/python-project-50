import argparse


def main():
    print('HELLO')
    print('Let us go')
    parser = argparse.ArgumentParser()
    parser.parse_args()
    print('Finish')

if __name__ == '__main__':
    main()