#!/usr/bin/python

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import sys
from makarov.markov_time import compare_users

if __name__ == "__main__":
    epsilon = 0.1
    verbosity = False

    if len(sys.argv) > 2:
        sys.stderr.write("Too many arguments.\n")
        sys.exit(64)
    elif len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        verbosity = True

    compare_users(epsilon, verbosity)
