from geom2d import Point, LineSegment

class TestLineSegment:
    def test_linesegment_creation(self):
        p1 = Point(2, 3)
        p2 = Point(4, 5)
        l = LineSegment(p1, p2)
        assert type(l) == LineSegment
        assert str(l) == 'LineSegment(Point(2, 3), Point(4, 5))'
