from .agc import Agc
from .point import Point
from .linesegment import LineSegment
from copy import deepcopy

class Rectangle(Agc):
    '''Class to represent a rectangle.'''

    def __init__(self, bottom_left, top_right, color='blue'):
        '''Initialise a Rectangle instance'''
        self.p1 = bottom_left
        self.p3 = top_right
        self.p2 = Point(self.p3.x, self.p1.y)
        self.p4 = Point(self.p1.x, self.p3.y)
        self.set_color(color)

    def __str__(self):
        '''A string representation of a Rectangle.'''
        (p1, p2, p3, p4) = self.get()
        return f'Rectangle({str(p1)}, {str(p2)}, {str(p3)}, {str(p4)})'

    def __repr__(self):
        '''A representation of a Rectangle.'''
        (p1, p2, p3, p4) = self.get()
        return f'Rectangle({str(p1)}, {str(p2)}, {str(p3)}, {str(p4)})'

    def get(self):
        '''Return a tuple of the points.'''
        return (self.p1, self.p2, self.p3, self.p4)

    def sides(self):
        '''Return a tuple of the sides as LineSegments'''
        (p1, p2, p3, p4) = self.get()
        return (LineSegment(p1, p2), LineSegment(p2, p3), 
        LineSegment(p3, p4), LineSegment(p4, p1))


    def rotate(self, theta):
        '''Rotate a rectangle anti-clockwise around the origin by theta degrees'''
        t = deepcopy(self)
        t.p1 = t.p1.rotate(theta)
        t.p2 = t.p2.rotate(theta)
        t.p3 = t.p3.rotate(theta)
        t.p4 = t.p4.rotate(theta)
        return t

    def translate(self, vec):
        """Translate a rectangle by vec."""
        t = deepcopy(self)
        t.p1 = t.p1.translate(vec)
        t.p2 = t.p2.translate(vec)
        t.p3 = t.p3.translate(vec)
        t.p4 = t.p4.translate(vec)
        return t

    def set_color(self, color):
        """Set the rectangles's color."""
        self.color = color
        for p in self.get():
            p.set_color(color)
