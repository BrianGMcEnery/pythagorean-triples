from .agc import Agc
from .point import Point
from copy import deepcopy

class LineSegment(Agc):
    ''' Class to represent a 2-d linesegment.'''

    def __init__(self, p1, p2, color='blue'):
        '''Initialise a LineSegment object.'''
        self.p1 = p1
        self.p2 = p2
        self.set_color(color)

    def __str__(self):
        '''A string representation of a LineSegment object.'''
        return f'LineSegment({str(self.p1)}, {str(self.p2)})'

    def __repr__(self):
        '''A representation of a LineSegment object.'''
        return f'LineSegment({repr(self.p1)}, {repr(self.p2)})'

    def get(self):
        '''Return a tuple consisting of the end points.'''
        return (self.p1, self.p2)

    def length(self):
        '''Return the length of the line segment.'''
        (p1, p2) = self.get()
        return p1.dist(p2)

    def slope(self):
        ''' Return the slope of the line segment.'''
        (x1, y1) = self.p1.get()
        (x2, y2) = self.p2.get()
        return (y2 - y1)/(x2 - x1)

    def y_intercept(self):
        ''' Return the y intercept of the line segment'''
        (x1, y1) = self.p1.get()
        return Point(0, y1 - self.slope() * x1)

    def contains_point(self, p):
        '''Returns a boolean value of whether a LineSegment contains a Point.'''
        (x, y) = p.get()
        m = self.slope()
        (_, c) = self.y_intercept().get()
        return  y == m * x + c

    def orientation(self):
        '''Returns a dictionary indicating the orientation of the LineSegment'''
        (x1, y1) = self.p1.get()
        (x2, y2) = self.p2.get()
        return {'x':x1 <= x2, 'y':y1 <= y2}

    def rotate(self, theta):
        '''Rotate a linesegment anti-clockwise around the origin by theta degrees'''
        l = deepcopy(self)
        l.p1 = l.p1.rotate(theta)
        l.p2 = l.p2.rotate(theta)
        return l

    def translate(self, vec):
        """Translate a linesegment by vec."""
        l = deepcopy(self)
        l.p1 = l.p1.translate(vec)
        l.p2 = l.p2.translate(vec)
        return l

    def set_color(self, color):
        """Set the linesegment's color."""
        self.color = color
        for p in self.get():
            p.set_color(color)