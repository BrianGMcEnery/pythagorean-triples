from geom2d import Point

class TestPoint:
    def test_point_creation(self):
        p = Point(2, 3)
        assert type(p) == Point
        assert str(p) == 'Point(2, 3)'