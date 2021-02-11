from phytrip import Triple, utils
from math import sqrt
import pytest

def test_pythagorean():
    assert utils.is_pythagorean_triple(3, 4, 5) == True
    assert utils.is_pythagorean_triple(1, 1, sqrt(2)) == True

def test_triple_creation():
    a = Triple(3, 4, 5)
    assert type(a) == Triple

    a = Triple(1, 1, sqrt(2))
    assert type(a) == Triple

    # Test to ensure that incorrect triple raises ValueError
    with pytest.raises(ValueError):
        a = Triple(3, 4, 4)

    a = Triple(4, 3, 5)
    assert a.get() == (4, 3, 5)

def test_triple_arithmetic():
    # Example 1. Triples pp. 7
    a = Triple(4, 3, 5)
    b = Triple(15, 8, 17)

    assert a.add(b).get() == (36, 77, 85)

    # Example 2. Triples pp. 9
    a = Triple(12, 5, 13)
    b = Triple(3, 4, 5)

    assert a.add(b).get() == (16, 63, 65)
    
    # Example 5. Triples pp. 9
    a = Triple(12, 5, 13)

    assert a.double().get() == (119, 120, 169)
    
    # Example 6. Triples pp. 10
    a = Triple(3, 4, 5)

    assert a.double().get() == (-7, 24, 25)
    
    # Example 7. Triples pp. 10
    a = Triple(4, 3, 5)
    b = Triple(15, 8, 17)

    assert a.sub(b).get() == (84, 13, 85)

    # Example 9. Triples pp. 11
    a = Triple(4, 3, 5)
    b = Triple(3, 4, 5)

    assert a.sub(b).get() == (24, -7, 25)
    
def test_quadrant_triples():
    assert Triple.quadrant_angle(0).get() == (1, 0, 1)
    assert Triple.quadrant_angle(90).get() == (0, 1, 1)
    assert Triple.quadrant_angle(180).get() == (-1, 0, 1)
    assert Triple.quadrant_angle(270).get() == (0, -1, 1)
    assert Triple.quadrant_angle(360).get() == (1, 0, 1)

    # Test to ensure that incorrect quadrant angle raises ValueError
    with pytest.raises(ValueError):
        Triple.quadrant_angle(67)

    # Example 12. Triples pp. 14
    a = Triple(4, 3, 5)
    b = Triple.quadrant_angle(90)

    assert a.add(b).get() == (-3, 4, 5)

    # Example 14. Triples pp. 14
    a = Triple(4, 3, 5)
    b = Triple.quadrant_angle(180)

    assert a.add(b).get() == (-4, -3, 5)

    # Example 15. Triples pp. 15
    a = Triple.quadrant_angle(0)
    b = Triple(-2, -3, sqrt(13))

    assert a.sub(b).get() == (-2, 3, sqrt(13))


    
    
