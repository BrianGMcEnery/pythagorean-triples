from .linesegment import LineSegment
from .draw import LineSegmentDraw
from .point import Point
from .draw import PointDraw
from .triangle import Triangle
from .draw import TriangleDraw

class DrawFactory():
    '''A factory class for creating draw objects.'''

    def __init__(self):
        '''Instantiate objects of factory class'''
        pass

    def make_draw_objects(self, g_objects):
        '''Make a list of draw objects.'''
        draw_objects = []
        for g_object in g_objects:
            if type(g_object) == Point:
                draw_objects.append(self.make_pointdraw(g_object))
            elif type(g_object) == LineSegment:
                draw_objects.append(self.make_linesegmentdraw(g_object))
            elif type(g_object) == Triangle:
                draw_objects.append(self.make_triangledraw(g_object))
            else:
                raise ValueError(str(g_object), " incorrect type. ")

        return draw_objects


    def make_pointdraw(self, p):
        '''Make a PointDraw object.'''
        (x, y) = p.get()
        return PointDraw(x, y)

    def make_linesegmentdraw(self, l):
        '''Make a LineSegmentDraw object.'''
        (p1, p2) = l.get()
        (p1, p2) = (self.make_pointdraw(p1), self.make_pointdraw(p2))
        return LineSegmentDraw(p1, p2)

    def make_triangledraw(self, t):
        '''Make a TriangleDraw object.'''
        (p1, p2, p3) = t.get()
        (p1, p2, p3) = (self.make_pointdraw(p1), self.make_pointdraw(p2), 
        self.make_pointdraw(p3))
        return TriangleDraw(p1, p2, p3)