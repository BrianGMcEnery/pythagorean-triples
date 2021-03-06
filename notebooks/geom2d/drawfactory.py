from .circle import Circle
from .draw import CircleDraw
from .ellipse import Ellipse
from .draw import EllipseDraw
from .linesegment import LineSegment
from .draw import LineSegmentDraw
from .line import Line
from .draw import LineDraw
from .point import Point
from .draw import PointDraw
from .polygon import Polygon
from .draw import PolygonDraw
from .triangle import Triangle
from .draw import TriangleDraw
from .rectangle import Rectangle
from .draw import RectangleDraw

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
            elif type(g_object) == Rectangle:
                draw_objects.append(self.make_rectangledraw(g_object))
            elif type(g_object) == Circle:
                draw_objects.append(self.make_circledraw(g_object))
            elif type(g_object) == Polygon:
                draw_objects.append(self.make_polygondraw(g_object))
            elif type(g_object) == Ellipse:
                draw_objects.append(self.make_ellipsedraw(g_object))
            elif type(g_object) == Line:
               draw_objects.append(self.make_linedraw(g_object))
            else:
                raise ValueError(str(g_object), " incorrect type. ")
        return draw_objects


    def make_pointdraw(self, p):
        '''Make a PointDraw object.'''
        (x, y) = p.get()
        color = p.color
        return PointDraw(x, y, color=color)

    def make_linesegmentdraw(self, l):
        '''Make a LineSegmentDraw object.'''
        (p1, p2) = l.get()
        (p1, p2) = (self.make_pointdraw(p1), self.make_pointdraw(p2))
        color = l.color
        return LineSegmentDraw(p1, p2, color = color)

    def make_linedraw(self, l):
        '''Make a LineDraw object.'''
        (p1, p2) = l.get()
        (p1, p2) = (self.make_pointdraw(p1), self.make_pointdraw(p2))
        color = l.color
        return LineDraw(p1, p2, color = color)

    def make_triangledraw(self, t):
        '''Make a TriangleDraw object.'''
        (p1, p2, p3) = t.get()
        (p1, p2, p3) = (self.make_pointdraw(p1), self.make_pointdraw(p2), 
        self.make_pointdraw(p3))
        color = t.color
        return TriangleDraw(p1, p2, p3, color=color)

    def make_rectangledraw(self, r):
        '''Make a RectangleDraw object.'''
        (p1, p2, p3, p4) = r.get()
        (p1, p2, p3, p4) = (self.make_pointdraw(p1), self.make_pointdraw(p2), 
        self.make_pointdraw(p3), self.make_pointdraw(p4))
        color = r.color
        return RectangleDraw(p1, p2, p3, p4, color=color)

    def make_circledraw(self, c):
        '''Make a CircleDraw object.'''
        (origin, radius) = c.get()
        origin = self.make_pointdraw(origin)
        color = c.color
        return CircleDraw(origin, radius, color=color)

    def make_polygondraw(self, poly):
        '''Make a PolygonDraw object.'''
        vs = poly.get()
        vs = list(map(lambda p: self.make_pointdraw(p), vs))
        color = poly.color
        return PolygonDraw(vs, color=color)

    def make_ellipsedraw(self, e):
        '''Make a EllipseDraw object.'''
        (o, w, h, a) = e.get()
        o = self.make_pointdraw(o)
        color = e.color
        return EllipseDraw(o, w, h, a, color=color)