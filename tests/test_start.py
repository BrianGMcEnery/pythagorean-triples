from phytrip import Triple, utils
from math import sqrt

def test_pythagorean():
    assert utils.is_pythagorean_triple(3, 4, 5) == True
    assert utils.is_pythagorean_triple(1, 1, sqrt(2.0)) == True

def test_triple():
    a = Triple(3, 4, 5)
    assert type(a) == Triple

    a = Triple(1, 1, sqrt(2))
    assert type(a) == Triple