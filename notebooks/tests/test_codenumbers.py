from phytrip import Triple, CodeNumber, common
import pytest
from math import sqrt

class TestCodeNumbers:

    def test_codenumber_creation(self):
        a = CodeNumber(10, 3)
        assert type(a) == CodeNumber
        assert str(a) == 'CodeNumber(10, 3)'
        assert a.get() == (10, 3)

        # Triples Example 5. pp. 67
        assert common.triple(a).get() == Triple(91, 60, 109).get()

        # Triples Example 6. pp. 68
        cn = CodeNumber(6, 1)
        assert common.triple(cn).get() == Triple(35, 12, 37).get()

        # Triples Example 7. pp. 68
        # Note that we need to use scale_common below
        cn = CodeNumber(-6, -4)
        assert common.triple(cn).scale_common().get() == Triple(5, 12, 13).get()
        
        # Triples Example 8, 9. pp. 68
        # Again we need to use scale_common
        a = Triple(21, 20, 29)
        assert common.codenumber(a).scale_common().get() == CodeNumber(5, 2).get()

    def test_codenumber_arithmetic(self):
        # Triples Example 10. pp. 69
        a = CodeNumber(5, 2)
        b = CodeNumber(3, 1)

        assert a.add(b).get() == CodeNumber(13, 11).get()

        # Triples Example 11. pp. 70
        # Note the use of scale_common below
        a = CodeNumber(5, 3)
        b = CodeNumber(9, 2)

        assert a.sub(b).scale_common().get() == CodeNumber(3, 1).get()

        # Triples Example 14. pp. 71
        a = CodeNumber(20, 9)

        assert a.complement().get() == CodeNumber(29, 11).get()

        # Triples Example 17. pp. 72
        a = CodeNumber(20, 9)

        assert a.supplement().get() == CodeNumber(9, 20).get()

    def test_quadrant_codenumbers(self):
        assert CodeNumber.quadrant_angle(0).get() == (1, 0)
        assert CodeNumber.quadrant_angle(90).get() == (1, 1)
        assert CodeNumber.quadrant_angle(180).get() == (0, 1)
        assert CodeNumber.quadrant_angle(270).get() == (1, -1)
        assert CodeNumber.quadrant_angle(360).get() == (1, 0)

        # Test to ensure that incorrect quadrant angle raises ValueError
        with pytest.raises(ValueError):
            CodeNumber.quadrant_angle(67)

    def test_special_codenumbers(self):
        assert CodeNumber.special_angle(30).get() == (sqrt(3) + 2, 1)
        assert CodeNumber.special_angle(45).get() == (1 + sqrt(2), 1)
        assert CodeNumber.special_angle(60).get() == (sqrt(3), 1)
    
        # Test to ensure that incorrect quadrant angle raises ValueError
        with pytest.raises(ValueError):
            CodeNumber.special_angle(35)





