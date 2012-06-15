"""
Organisms with genomes represented as bitstrings.

Immutable class.
"""
import random
from mutate import mutate_value
import bitstring
from bitstring import Bitstring


class Organism(object):
    def __init__(self, value):
        assert(isinstance(value, Bitstring))
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.value)

    def mutate(self):
        mutated_value = mutate_value(self.value)
        return Organism(mutated_value)

    @property
    def fitness(self):
        all_zeroes = Bitstring(False for _ in self.value)
        return float(all_zeroes.hamming_distance(self.value))

default_organism = Organism(Bitstring(False for _ in range(10)))