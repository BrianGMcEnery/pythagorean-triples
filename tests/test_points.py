from geom2d import Point
from math import sqrt

class TestPoint:
    def test_point_creation(self):
        p = Point(2, 3)
        assert type(p) == Point
        assert str(p) == 'Point(2, 3)'

        assert p.get() == (2, 3)

    def test_point_geometry(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        d = p1.dist(p2)

        assert d == sqrt(2)
        
        # For completeness try another orientation
        p1 = Point(1, -1)
        p2 = Point(2, -2)
        d = p1.dist(p2)

        assert d == sqrt(2)