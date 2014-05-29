#!/usr/bin/python

import math

class Markov:
    """Markov chain.

    EPSILON:
        Threshold used in comparisons between Markov chains.
    """

    EPSILON = 0.05

    def __init__(self):
        """Initialize a chain."""
        self.__totals = dict()
        self.__counts = dict()
        self.__averages = dict()

    def __check_primary_key(self, key):
        """Check whether a primary key has already been used."""
        if not self.__totals.has_key(key):
            self.__totals[key] = dict()
            self.__counts[key] = dict()
            self.__averages[key] = dict()

    def __check_secondary_key(self, key_1, key_2):
        """Check whether a secondary key has already been used."""
        self.__check_primary_key(key_1)
        if not self.__totals[key_1].has_key(key_2):
            self.__totals[key_1][key_2] = 0
            self.__counts[key_1][key_2] = 0
            self.__averages[key_1][key_2] = 0

    def __add_value(self, key_1, key_2, value):
        """Add a value to (key_1, key_2)."""
        self.__totals[key_1][key_2] += value
        self.__counts[key_1][key_2] += 1

    def has_key_1(self, key_1):
        """Determine whether a primary key has values."""
        return self.__totals.has_key(key_1)

    def has_key_2(self, key_1, key_2):
        """Determine whether a secondary key has values."""
        return self.__totals[key_1].has_key(key_2)

    def get_average(self, key_1, key_2):
        """Get the value corresponding to the (key_1, key_2) pair."""
        return self.__averages[key_1][key_2]

    def add_value(self, key_1, key_2, value):
        """add_value."""
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
        """Compute the difference between the values of two chains."""
        difference = self.__averages[key_1][key_2]
        difference -= chain.get_average(key_1, key_2)
        difference = math.fabs(difference)

        return difference


    def is_similiar(self, chain):
        """Determine whether two chains are similiar."""
        result = False
        self.compute_averages()
        chain.compute_averages()
        if isinstance(chain, Markov):
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
                result = error <= Markov.EPSILON
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
        """Determine whether two chains are similiar."""
        return chain_1.is_similiar(chain_2)

    @staticmethod
    def set_epsilon(epsilon):
        Markov.EPSILON = epsilon


# Stupid test.
if __name__ == "__main__":
    MARK_1 = Markov()
    MARK_2 = Markov()
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
