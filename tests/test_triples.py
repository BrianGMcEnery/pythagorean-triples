from phytrip import Triple, utils
from math import sqrt, cos, sin, tan, pi, isclose
import pytest

class TestTriples:

    def test_pythagorean(self):
        assert utils.is_pythagorean_triple(3, 4, 5) == True
        assert utils.is_pythagorean_triple(1, 1, sqrt(2)) == True

    def test_triple_creation(self):
        a = Triple(3, 4, 5)
        assert type(a) == Triple

        a = Triple(1, 1, sqrt(2))
        assert type(a) == Triple

        # Test to ensure that incorrect triple raises ValueError
        with pytest.raises(ValueError):
            a = Triple(3, 4, 4)

        a = Triple(4, 3, 5)
        assert a.get() == (4, 3, 5)

        a = Triple(20, 15, 25)
        assert a.scale_common().get() == (4, 3, 5)

        a = Triple(20.0, 15.0, 25.0)
        assert a.scale_common().get() == (4, 3, 5)

        a = Triple(1.0, 1.0, sqrt(2))
        assert a.scale_common().get() == (1.0, 1.0, sqrt(2))



    def test_triple_arithmetic(self):
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

        # Example 20. Triples pp. 17
        a = Triple(7, 24, 25)
    
        assert a.half().get() == (32, 24, 40)
    
    
    def test_quadrant_triples(self):
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


    def test_special_triples(self):
        assert Triple.special_angle(30).get() == (sqrt(3), 1, 2)
        assert Triple.special_angle(45).get() == (1, 1, sqrt(2))
        assert Triple.special_angle(60).get() == (1, sqrt(3), 2)
    
        # Test to ensure that incorrect quadrant angle raises ValueError
        with pytest.raises(ValueError):
            Triple.special_angle(35)

        # Example 17. Triples pp. 16
        a = Triple.special_angle(30)
        b = Triple.special_angle(45)

        assert a.add(b).get() == (sqrt(3) - 1, 1 + sqrt(3), 2 * sqrt(2))

        # Example 19. Triples pp. 17
        a = Triple.special_angle(45)
        b = Triple(12, 5, 13)

        assert a.add(b).get() == (7, 17, 13 * sqrt(2))

    def test_triple_trigonometry(self):
        # Get two special angle triples
        a = Triple.special_angle(45)
        b = Triple.special_angle(60)

        # Reduce them to unit triples
        a = a.unit()
        b = b.unit()

        # Assert that their sum and difference are unit triples
        (_, _, r) = a.add(b).get()
        assert r == 1

        (_, _, r) = a.sub(b).get()
        assert r == 1

        # Checkout trigonometric functions for 60
        angle = pi/3
        a = Triple.special_angle(60)

        assert isclose(cos(angle), a.cos())
        assert isclose(sin(angle), a.sin())
        assert isclose(tan(angle), a.tan())

        assert isclose(1 / a.tan(), a.cot())
        assert isclose(1 / a.cos(), a.sec())
        assert isclose(1 / a.sin(), a.cosec())

