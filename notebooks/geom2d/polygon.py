from .agc import Agc
from .point import Point
from .linesegment import LineSegment
from copy import deepcopy

class Polygon(Agc):
    '''Class to represent a polygon.'''

    def __init__(self, vertices, color='blue'):
        '''Initialise a Polygon instance'''
        self.vertices = vertices
        
        self.set_color(color)

    def __str__(self):
        '''A string representation of a Polygon.'''
        return f'Polygon({self.vertices})'

    def __repr__(self):
        '''A string representation of a Polygon.'''
        return f'Polygon({self.vertices})'

    def length(self):
        return len(self.vertices)

    def get(self):
        '''Return the vertices.'''
        return self.vertices

    def sides(self):
        '''Return a tuple of the sides as LineSegments'''
        vs = self.get()

        # The following is to zip together the list of vertices as follows
        #
        #   vs[0] vs[1] vs[2] ...
        #     |     |     |  
        #   vs[1] vs[2] vs[3]
        #
        #   to produce a list of the form
        #
        #   [(vs[0], vs[1]), (vs[1], vs[2]), ...] 
        #

        ps = list(zip(vs, (vs + [vs[0]])[1:]))

        ls = map ((lambda p: LineSegment(p[0], p[1])), ps)

        return tuple(ls)

    def rotate(self, theta):
        '''Rotate a polygon anti-clockwise around the origin by theta degrees'''
        t = deepcopy(self)
        vs = t.get()
        vs = list(map((lambda p: p.rotate(theta)), vs))
        t.vertices = vs
        return t

    def translate(self, vec):
        """Translate a polygon by vec."""
        t = deepcopy(self)
        vs = t.get()
        vs = list(map((lambda p: p.translate(vec)), vs))
        t.vertices = vs
        return t

    def set_color(self, color):
        """Set the polygon's color."""
        self.color = color
        for p in self.get():
            p.set_color(color)
