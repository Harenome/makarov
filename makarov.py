#!/usr/bin/python

import sys
from makarov.markov_time import compare_users

if __name__ == "__main__":
    verbosity = False

    if len(sys.argv) > 2:
        sys.stderr.write("Too many arguments.\n")
        sys.exit(64)
    elif len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        verbosity = True

    compare_users(verbosity)
