#!/usr/bin/python

import sys
from makarov.markov_time import compare_users

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.stderr.write("Too many arguments.\n")
        sys.exit(64)
    compare_users()
