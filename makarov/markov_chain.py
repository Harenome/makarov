#!/usr/bin/python

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import math

class MarkovChain:
    """Markov chain.

    - __totals:
        Totals for a pair (key_1, key_2)
    - __counts:
        Occurence count for a pair (key_1, key_2)
    - __averages:
        __totals / __counts for a pair (key_1, key_2)

    - EPSILON:
        Threshold used in comparisons between Markov chains.
    """

    EPSILON = 0.5

    def __init__(self):
        """Initialize a chain."""
        self.__totals = dict()
        self.__counts = dict()
        self.__averages = dict()

    def __check_primary_key(self, key):
        """Check whether a primary key has already been used.
        - key:
            Key to check.
        """
        if not self.__totals.has_key(key):
            self.__totals[key] = dict()
            self.__counts[key] = dict()
            self.__averages[key] = dict()

    def __check_secondary_key(self, key_1, key_2):
        """Check whether a secondary key has already been used.
        - key_1:
            Level 1 key.
        - key_2:
            Key to check.
        """
        self.__check_primary_key(key_1)
        if not self.__totals[key_1].has_key(key_2):
            self.__totals[key_1][key_2] = 0
            self.__counts[key_1][key_2] = 0
            self.__averages[key_1][key_2] = 0

    def __add_value(self, key_1, key_2, value):
        """Add a value to (key_1, key_2).
        - key_1:
            Level 1 key.
        - key_2:
            Level 2 key.
        - value:
            Value to map to (key_1, key_2).
        """
        self.__totals[key_1][key_2] += value
        self.__counts[key_1][key_2] += 1

    def has_key_1(self, key_1):
        """Determine whether a primary key has values.
        - key_1:
            Key to check for values.
        """
        return self.__totals.has_key(key_1)

    def has_key_2(self, key_1, key_2):
        """Determine whether a secondary key has values.
        - key_1:
            Level 1 key.
        - key_2:
            Key to check for values.
        """
        return self.__totals[key_1].has_key(key_2)

    def get_average(self, key_1, key_2):
        """Get the value corresponding to the (key_1, key_2) pair.
        - key_1:
            Level 1 key.
        - key_2:
            Level 2 key.
        """
        return self.__averages[key_1][key_2]

    def add_value(self, key_1, key_2, value):
        """Add a value to (key_1, key_2).
        - key_1:
            Level 1 key.
        - key_2:
            Level 2 key.
        - value:
            Value to map to (key_1, key_2).
        """
        self.__check_primary_key(key_1)
        self.__check_secondary_key(key_1, key_2)
        self.__add_value(key_1, key_2, value)

    def compute_averages(self):
        """Compute averages."""
        for key_1 in self.__totals:
            for key_2 in self.__totals[key_1]:
                total = self.__totals[key_1][key_2]
                count = self.__counts[key_1][key_2]
                self.__averages[key_1][key_2] = total / count

    def display(self):
        """Display the chain."""
        print self.__totals

    def __difference(self, key_1, key_2, chain):
        """Compute the difference between the values of two chains.
        - key_1:
            Level 1 key.
        - key_2:
            Level 2 key.
        - chain:
            Other chain.
        """
        difference = self.__averages[key_1][key_2]
        difference -= chain.get_average(key_1, key_2)
        difference = math.fabs(difference)

        return difference


    def is_similiar(self, chain):
        """Determine whether two chains are similiar.
        - chain:
            Other chain.
        """
        result = False
        if isinstance(chain, MarkovChain):
            self.compute_averages()
            chain.compute_averages()
            count = 0
            error = 0
            for key_1 in self.__totals.keys():
                if chain.has_key_1(key_1):
                    for key_2 in self.__totals[key_1].keys():
                        if chain.has_key_2(key_1, key_2):
                            count += 1
                            error += self.__difference(key_1, key_2, chain)
            if count != 0:
                error /= count
                result = error <= MarkovChain.EPSILON
        return result

    def total(self):
        """Compute the total of the chain."""
        chain_sum = 0.0
        for key_1 in self.__totals:
            for key_2 in self.__totals[key_1]:
                chain_sum += self.__totals[key_1][key_2]
        return chain_sum


    @staticmethod
    def are_similiar(chain_1, chain_2):
        """Determine whether two chains are similiar.
        - chain_1:
            First chain.
        - chain_2:
            Second chain.
        """
        return chain_1.is_similiar(chain_2)

    @staticmethod
    def set_epsilon(epsilon):
        """Change MarkovChain.EPSILON.
        - epsilon:
            Epsilon.
        """
        MarkovChain.EPSILON = epsilon


# Stupid test.
if __name__ == "__main__":
    MARK_1 = MarkovChain()
    MARK_2 = MarkovChain()
    MARK_1.add_value('a', 'b', 0.1)
    MARK_1.add_value('a', 'b', 1.5)
    MARK_1.add_value('b', 'b', 0.1)
    MARK_1.add_value('b', 'b', 0.1)
    MARK_1.add_value('b', 'a', 0.1)
    MARK_1.add_value('c', 'b', 0.1)
    MARK_2.add_value('a', 'b', 0.1)
    MARK_2.add_value('a', 'b', 0.2)
    MARK_2.add_value('b', 'b', 0.1)
    MARK_2.add_value('b', 'b', 0.1)
    MARK_2.add_value('b', 'a', 0.1)
    MARK_2.add_value('c', 'b', 0.1)
    MARK_1.compute_averages()
    MARK_2.compute_averages()
    MARK_1.display()
    MARK_2.display()
    print MARK_1.is_similiar(MARK_1)
    print MARK_1.is_similiar(MARK_2)
