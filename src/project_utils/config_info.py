#!/usr/bin/env python
import os
import sys
# from pprint import pprint


def print_environment():
    # We made an iterable stream of environment variables filtered by filtertuple
    # Only vars with a key that contain any of the fragments in filtertuple are included
    filtertuple = ("CONDA", "SPARK", "PYTHON", "JAVA", "PATH", "IBAN", "ROOT_DIR")
    stream = (item for item in os.environ.items() if any(fragment in item[0] for fragment in filtertuple))
    # print(stream)
    # pprint(f"All environment variables whose names contain any of these fragments: {filtertuple}")
    print(f"All environment variables whose names contain any of these fragments: {filtertuple}")
    for k, v in iter(stream):
        print(f'{k}={v}')


def check_path():
    try:
        conda_prefix = os.environ['CONDA_PREFIX']
        user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        user_paths = []

    print(f"CONDA_PREFIX: {conda_prefix}")
    print(f"PYTHONPATH: {user_paths}")
    print("sys.path: ")
    for path in sys.path:
        print(path)


# def main(args):
#     if len(args) > 0:
#         print(f"args = {args}")
#     print_environment()
#     check_path()
#
#
# if __name__ == '__main__':
#     print(f"__name__=={__name__}")
#     main(sys.argv[1:])

