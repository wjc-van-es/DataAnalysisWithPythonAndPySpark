#!/usr/bin/env python

import os
import sys

from project_utils.config_info import load_env_file_when_present, check_path, print_environment


def main(args):
    if len(args) > 0:
        print(f"args = {args}")
    print(f"os.path.abspath('.')={os.path.abspath('.')}")
    load_env_file_when_present('project.env')
    print_environment()
    check_path()


if __name__ == '__main__':
    print(f"__name__=={__name__}")
    main(sys.argv[1:])