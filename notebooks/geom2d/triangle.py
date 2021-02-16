from .agc import Agc
from .point import Point
from .linesegment import LineSegment

class Triangle(Agc):
    '''Class to represent a 2-d triangle.'''

    def __init__(self, p1, p2, p3):
        '''Initialise a Triangle instance'''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        '''A string representation of a Triangle.'''
        (p1, p2, p3) = self.get()
        return f'Triangle({str(p1)}, {str(p2)}, {str(p3)})'

    def __repr__(self):
        '''A representation of a Triangle.'''
        (p1, p2, p3) = self.get()
        return f'Triangle({str(p1)}, {str(p2)}, {str(p3)})'

    def get(self):
        '''Return a tuple of the points.'''
        return (self.p1, self.p2, self.p3)

    def sides(self):
        '''Return a tuple of the sides as LineSegments'''
        (p1, p2, p3) = self.get()
        return (LineSegment(p1, p2), LineSegment(p2, p3), LineSegment(p3, p1))