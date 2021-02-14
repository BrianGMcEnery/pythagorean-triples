from .agc import Agc
from .point import Point

class LineSegment(Agc):
    ''' Class to represent a 2-d linesegment.'''

    def __init__(self, p1, p2):
        '''Initialise a LineSegment object.'''
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        '''A string representation of a LineSegment object.'''
        return f'LineSegment({str(self.p1)}, {str(self.p2)})'

    def __repr__(self):
        '''A representation of a LineSegment object.'''
        return f'LineSegment({repr(self.p1)}, {repr(self.p2)})'

    def contains_point(self, p):
        '''Returns a boolean value of whether a LineSegment contains a Point.'''
        (x, y) = p.get()
        (x1, y1) = self.p1.get()
        (x2, y2) = self.p2.get()
        xcon = ((x1 <= x <= x2) or (x2 <= x <= x1))
        ycon = ((y1 <= y <= y2) or (y2 <= y <= y1))
        return  xcon and ycon
