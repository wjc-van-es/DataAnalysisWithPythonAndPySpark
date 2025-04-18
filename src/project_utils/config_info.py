#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


def load_env_file_when_present(file_name: str):
    print(f"file_name = {file_name}")

    # tries to find the .env file with the file_name starting in the same directory
    # as the source file and moving up from there to subsequent parent dirs
    env_file = find_dotenv(file_name)
    print(f"env_file = {env_file}, type(env_file) = {type(env_file)}")
    print(f"Path(env_file).is_file(): {Path(env_file).is_file()}")
    if Path(env_file).is_file():
        load_dotenv(env_file)
    else:
        print(f"env_file = {env_file}, does not exist and therefore could not be loaded")


def print_environment():
    # We made an iterable stream of environment variables filtered by filtertuple
    # Only vars with a key that contain any of the fragments in filtertuple are included
    filtertuple = ("CONDA", "SPARK", "PYTHON", "JAVA", "PATH", "IBAN", "ROOT_DIR", "_PW")
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

