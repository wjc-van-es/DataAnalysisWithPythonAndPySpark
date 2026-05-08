import os
import sys

from scipy.stats import binom

import project_utils.config_info as ci

def binomial_test():
    n = 10
    p = 0.9
    for k in range(n + 1):
        probability = binom.pmf(k, n, p)
        print(f"the probability for {k} results is {probability}")

def main(args):
    print(f"os.path.abspath('.')={os.path.abspath('.')}")
    ci.load_env_file_when_present('project.env')
    ci.print_environment()
    ci.check_path()
    if len(args) > 0:
        print(f"args = {args}")
    binomial_test()


if __name__ == '__main__':
    print(f"__name__=={__name__}")
    print(f"sys.argv={sys.argv}")
    main(sys.argv[1:])
