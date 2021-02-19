from .agc import Agc
from .point import Point
from copy import deepcopy

class Circle(Agc):
    '''Class to represent a circle.'''

    def __init__(self, origin, radius, color='blue'):
        '''Initialise a Circle instance'''
        self.origin = origin
        self.radius = radius
        self.set_color(color)

    def __str__(self):
        '''A string representation of a Circle.'''
        (origin, radius) = self.get()
        return f'Circle({str(origin)}, {str(radius)})'

    def __repr__(self):
        '''A representation of a Circle.'''
        (origin, radius) = self.get()
        return f'Circle({str(origin)}, {str(radius)})'

    def get(self):
        '''Return a tuple of the origin and radius.'''
        return (self.origin, self.radius)

    def rotate(self, theta):
        '''Rotate a circle anti-clockwise around the origin by theta degrees'''
        t = deepcopy(self)
        t.origin = t.origin.rotate(theta)
        return t

    def translate(self, vec):
        """Translate a circle by vec."""
        t = deepcopy(self)
        t.origin = t.origin.translate(vec)
        return t

    def set_color(self, color):
        """Set the circle's color."""
        self.color = color
        self.origin.set_color(color)
