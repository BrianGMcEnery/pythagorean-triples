from geom2d.draw import PointDraw

class TestPointDraw:
    def test_pointdraw_creation(self):
        p = PointDraw(2, 3)
        assert type(p) == PointDraw
        assert str(p) == 'Point(2, 3)'