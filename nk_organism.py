import mixins
from bitstring_organism import Organism as BOrg
import bitstring_organism


class Organism(BOrg):
    def __init__(self, value, nk_model):
        self.nk_model = nk_model
        super(Organism, self).__init__(value)

    @property
    def fitness(self):
        return self.nk_model.determine_fitness(self.value)

    def mutate(self):
        """
        the mutate method of an organism calls the module
        mutate and returns a new organism with the mutation
        note: original organism is unchanged
        """
        return Organism(self._mutate_value(), self.nk_model)