import random
import itertools
import operator
from structure_and_landscapes.organism.bitstring import organism as bitstring_organism
from structure_and_landscapes.organism.bitstring import bitstring
from structure_and_landscapes.organism.bitstring.nk_model import organism as nk_organism
from structure_and_landscapes.organism.bitstring.nk_model import nk_model
from structure_and_landscapes.organism.rna import organism as rna_organism


def all_possible_bitstrings(length):
    tuples = itertools.product([False, True], repeat=length)
    return (bitstring.Bitstring(bool_tuple) for bool_tuple in tuples)

def orgs_ordered_by_fitness(orgs):
    return sorted(orgs, key=operator.attrgetter("fitness"), reverse=True)

def nk_organism_mutation_map(organism, nk):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of tuples where each tuple is a nk_organism and its
    corresponding fitness.
    """

    bitstring_value = organism.value
    nk_organism_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = nk_organism.Organism(perturbed_bitstring, nk_model=nk)
        nk_organism_mutation_map.append((
            perturbed_bitstring, perturbed_organism.fitness))

    return nk_organism_mutation_map


def bitstring_organism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of tuples where each pair is a bitstring_organism and its
    corresponding fitness.
    """
    bitstring_value = organism.value
    bitstring_org_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = bitstring_organism.Organism(perturbed_bitstring)
        bitstring_org_mutation_map.append((
            perturbed_bitstring, perturbed_organism.fitness))
    return bitstring_org_mutation_map


def rna_organism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of lists of tuples where each tuple is an rna_organism and its
    corresponding fitness.
    """
    rna_seq = organism.value
    rna_organism_mutation_map = []
    for i in range(len(rna_seq)):
        perturbed_org_list = organism.change_base(i)
        for org in perturbed_org_list:
            rna_organism_mutation_map.append((org, org.fitness))

    return rna_organism_mutation_map


if __name__ == "__main__":

    length_of_desired_genome = 15
    k_total = 8
    bit = "0" * length_of_desired_genome
    nk_model_type = nk_model.NKModelFactory()
    use_model = nk_model_type.non_consecutive_dependencies(n=length_of_desired_genome, k=k_total)
    nk_org = nk_organism.Organism(bitstring.Bitstring(bit), nk_model=use_model)
    print nk_organism_mutation_map(nk_org, use_model)


    #bit = bitstring.Bitstring('0000')
    #bit_org = bitstring_organism.Organism(bit)
    #print bitstring_organism_mutation_map(bit_org)


    #rna_org = rna_organism.random_organism()
    #print rna_organism_mutation_map(rna_org)
