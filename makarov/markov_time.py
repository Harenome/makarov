#!/usr/bin/python

import time
import sys
from markov_chain import MarkovChain
from getch import getch

class MarkovTimeReader:
    """Class to read times between keystrokes and return a Markov chain."""
    def __init__(self):
        """Init."""
        self.__chain = MarkovChain()
        self.__text = list()
        self.__times = list()

    def __read_character(self):
        """Read a character and return it along with a time."""
        start = time.time()
        input_char = getch()
        end = time.time()
        t = end - start

        return input_char, t

    def __backspace(self):
        """When the input character is a backspace."""
        if self.__text:
            sys.stdout.write('\b \b')
            if len(self.__text) > 1:
                previous = self.__text.pop()
                ante_previous = self.__text[-1]
                old_time = self.__times.pop()
                self.__chain.add_value(ante_previous, previous, - old_time)

    def __normal_character(self, input_character, interval):
        """When the input character is a normal character."""
        if self.__text:
            previous = self.__text[-1]
            self.__chain.add_value(previous, input_character, interval)
            self.__times.append(interval)

    def read(self):
        """Read. The object is reset."""
        # Reset the object.
        self.__init__()

        go_on = True
        while go_on:
            input_character, interval = self.__read_character()
            go_on = input_character != '\r'
            if go_on:
                if input_character == '\x7f':
                    self.__backspace()
                else:
                    self.__normal_character(input_character, interval)
                    self.__text.append(input_character)
                    sys.stdout.write(input_character)

        sys.stdout.write('\n')

        return self.__chain

def compare_users(verbose):
    """Compare two users."""
    USER_1 = "Bro 1"
    USER_2 = "Bro 2"
    COMPARISON = " != "

    MarkovChain.set_epsilon = 0.3

    reader = MarkovTimeReader()
    print USER_1
    chain_1 = reader.read()
    print USER_2
    chain_2 = reader.read()
    if MarkovChain.are_similiar(chain_1, chain_2):
        COMPARISON = " == "

    print "\n" + USER_1 + COMPARISON + USER_2

    if verbose:
        print "\nMarkov chains:"
        print USER_1 + ":"
        chain_1.display()
        print USER_2 + ":"
        chain_2.display()

# Run.
if __name__ == "__main__":
    verbosity = False
    if len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        verbosity = True
    compare_users(verbosity)
