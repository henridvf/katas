import pytest
import katas.dnatorna as kt 


def test_dna_to_rna_1():
    assert kt.dna_to_rna("TTTT") == "UUUU"
    assert kt.dna_to_rna("GCAT") == "GCAU"
    assert kt.dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"