from .agc import Agc
from .point import Point
from copy import deepcopy

class Line(Agc):
    ''' Class to represent a 2-d line.'''

    def __init__(self, p1=None, p2=None, p=None, slope=None, color='blue'):
        '''Initialise a Line object.'''
        if p1 is not None and p2 is not None:
            self.p1 = p1
            self.p2 = p2
        elif p is not None and slope is not None:
            self.p1 = p
            self.slope = slope
            self.p2 = self.y_intercept()

        self.set_color(color)
        self._set_slope_intercept()

        

    def __str__(self):
        '''A string representation of a Line object.'''
        return f'Line({str(self.p1)}, {str(self.p2)})'

    def __repr__(self):
        '''A representation of a Line object.'''
        return f'Line({repr(self.p1)}, {repr(self.p2)})'

    def get(self):
        '''Return a tuple consisting of the end points.'''
        return (self.p1, self.p2)

    def y_intercept(self):
        ''' Return the y intercept of the line.'''
        (x1, y1) = self.p1.get()
        return Point(0, y1 - self.slope * x1)

    def _set_slope_intercept(self):
        (x1, y1) = self.p1.get()
        (x2, y2) = self.p2.get()
        self.slope = (y2 -y1)/(x2 - x1)
        self.intercept = self.y_intercept()


    def contains_point(self, p):
        '''Returns a boolean value of whether a Line contains a Point.'''
        (x, y) = p.get()
        m = self.slope
        (_, c) = self.y_intercept().get()
        return  y == m * x + c

    def rotate(self, theta):
        '''Rotate a line anti-clockwise around the origin by theta degrees'''
        l = deepcopy(self)
        l.p1 = l.p1.rotate(theta)
        l.p2 = l.p2.rotate(theta)
        return l

    def translate(self, vec):
        """Translate a line by vec."""
        l = deepcopy(self)
        l.p1 = l.p1.translate(vec)
        l.p2 = l.p2.translate(vec)
        return l

    def set_color(self, color):
        """Set the linesegment's color."""
        self.color = color
        for p in self.get():
            p.set_color(color)