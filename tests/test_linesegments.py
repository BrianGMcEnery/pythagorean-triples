from geom2d import Point, LineSegment

class TestLineSegment:
    def test_linesegment_creation(self):
        p1 = Point(2, 3)
        p2 = Point(4, 5)
        l = LineSegment(p1, p2)
        assert type(l) == LineSegment
        assert str(l) == 'LineSegment(Point(2, 3), Point(4, 5))'

    def test_linesegment_geometry(self):
        p1 = Point(2, 3)
        p2 = Point(4, 5)
        l = LineSegment(p1, p2)
        p = Point(3, 4)
        assert l.contains_point(p) == True

        # Try now for the reverse order of points

        p1 = Point(2, 3)
        p2 = Point(4, 5)
        l = LineSegment(p2, p1)
        p = Point(3, 4)
        assert l.contains_point(p) == True


