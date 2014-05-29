#!/usr/bin/python

import time
import sys
from markov_chain import MarkovChain
from getch import getch

def __read_times():
    """Read times between keystrokes and save them in a Markov chain."""
    chain = MarkovChain()
    a = getch()
    sys.stdout.write(a)
    while a != '\r':
        start = time.time()
        b = getch()
        end = time.time()
        t = end - start
        chain.add_value(a, b, t)
        a = b
        sys.stdout.write(a)
    sys.stdout.write('\n')

    return chain

def compare_users():
    """Compare two users."""
    USER_1 = "Bro 1"
    USER_2 = "Bro 2"
    COMPARISON = " != "

    MarkovChain.set_epsilon = 0.1

    print USER_1
    chain_1 = __read_times()
    print USER_2
    chain_2 = __read_times()
    if MarkovChain.are_similiar(chain_1, chain_2):
        COMPARISON = " == "

    print "\n" + USER_1 + COMPARISON + USER_2
    print USER_1 + ":"
    chain_1.display()
    print USER_2 + ":"
    chain_2.display()

# Run.
if __name__ == "__main__":
    compare_users()
