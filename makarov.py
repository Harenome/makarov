#!/usr/bin/python

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import sys
from makarov.markov_time import compare_users

version_major = 1
version_minor = 0
version_patch = 2

def print_version():
    print "Makarov, version " + str(version_major) + "." + str(version_minor) + "." + str(version_patch)
    print "Written by MEYER Jeremy, RAZANAJATO RANAIVOARIVONY Harenome and WHILHELM Stan."

if __name__ == "__main__":
    epsilon = 0.1
    verbosity = False

    if len(sys.argv) > 2:
        sys.stderr.write("Too many arguments.\n")
        sys.exit(64)
    elif len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        verbosity = True
    elif len(sys.argv) > 1 and sys.argv[1] == "--version":
        print_version()
        sys.exit(0)

    print "Welcome to Makarov."
    compare_users(epsilon, verbosity)
