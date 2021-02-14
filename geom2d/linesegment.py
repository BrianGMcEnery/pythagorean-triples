from .agc import Agc
from .point import Point

class LineSegment(Agc):
    ''' Class to represent a 2-d linesegment.'''

    def __init__(self, p1, p2):
        '''Initialise a LineSegment object'''
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        '''A string representation of a LineSegment object'''
        return f'LineSegment({str(self.p1)}, {str(self.p2)})'

    def __repr__(self):
        '''A representation of a LineSegment object'''
        return f'LineSegment({repr(self.p1)}, {repr(self.p2)})'
