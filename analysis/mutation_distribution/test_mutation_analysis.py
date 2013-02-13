from unittest import TestCase as TC

import mutation_analysis
from structure_and_landscapes.organism.bitstring.bitstring import Bitstring
from structure_and_landscapes.organism.integer.organism import Organism as IntOrganism

class TestModule(TC):

    def test_all_possible_bitstrings(self):
        bit1 = mutation_analysis.all_possible_bitstrings(1)
        self.assertEqual(set(bit1), set([Bitstring("0"), Bitstring("1")]))

        bit4 = list(mutation_analysis.all_possible_bitstrings(4))
        self.assertIn(Bitstring("0000"), bit4)
        self.assertIn(Bitstring("1111"), bit4)
        self.assertEqual(len(bit4), 2**4)

    def test_orgs_ordered_by_fitness(self):
        orgs = [IntOrganism(1),
                IntOrganism(3),
                IntOrganism(5),
                IntOrganism(2),
                IntOrganism(4)]
        orgs_sorted = mutation_analysis.orgs_ordered_by_fitness(orgs)
        self.assertEqual(orgs_sorted, [
            IntOrganism(5),
            IntOrganism(4),
            IntOrganism(3),
            IntOrganism(2),
            IntOrganism(1)])


