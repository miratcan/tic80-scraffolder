import argparse


def main(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    # create the top-level parser
    parser = argparse.ArgumentParser()

    sub_parsers = parser.add_subparsers()

    list_parser = sub_parsers.add_parser('list')
    create_parser = sub_parsers.add_parser('create')
    create_parser.add_argument('library', '+')

    args = parser.parse_args()

    main(args)


