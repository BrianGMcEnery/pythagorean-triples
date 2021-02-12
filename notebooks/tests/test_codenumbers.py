from phytrip import Triple, CodeNumber
from phytrip import common

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
        a = Triple(21, 20, 29)
        assert common.codenumber(a).get() == CodeNumber(5, 2).get()



