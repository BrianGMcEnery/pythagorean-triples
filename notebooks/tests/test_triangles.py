from geom2d import LineSegment, Point, Triangle

class TestTriangle:
    def test_triangle_creation(self):
        p1 = Point(1, 1)
        p2 = Point(4, 1)
        p3 = Point(4, 5)

        t = Triangle(p1, p2, p3)
        
        assert type(t) == Triangle
        assert str(t) == 'Triangle(Point(1, 1), Point(4, 1), Point(4, 5))'

        assert str(t.get()) == str((Point(1, 1), Point(4, 1), Point(4, 5)))
        sides = t.sides()
        assert str(sides[0]) == str(LineSegment(Point(1, 1), Point(4, 1)))
        assert str(sides[1]) == str(LineSegment(Point(4, 1), Point(4, 5)))
        assert str(sides[2]) == str(LineSegment(Point(4, 5), Point(1, 1)))