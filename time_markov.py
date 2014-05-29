#!/usr/bin/python

import time
import sys
import markov
from getch import getch

def read_times():
    """Read times between keystrokes and save them in a Markov chain."""
    chain = markov.Markov()
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

# Run.
if __name__ == "__main__":
    USER_1 = "Bro 1"
    USER_2 = "Bro 2"
    COMPARISON = " != "

    markov.Markov.set_epsilon = 0.1

    print USER_1
    chain_1 = read_times()
    print USER_2
    chain_2 = read_times()
    if markov.Markov.are_similiar(chain_1, chain_2):
        COMPARISON = " == "

    print USER_1 + COMPARISON + USER_2 + "\n"
    print USER_1 + ":"
    chain_1.display()
    print USER_2 + ":"
    chain_2.display()
