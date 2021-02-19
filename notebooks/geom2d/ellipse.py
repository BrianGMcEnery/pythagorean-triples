from .agc import Agc
from .point import Point
from copy import deepcopy

class Ellipse(Agc):
    '''Class to represent an ellipse.'''

    def __init__(self, origin, width, height, angle = 0, color='blue'):
        '''Initialise an Ellipse instance'''
        self.origin = origin
        self.width = width
        self.height = height
        self.angle = angle
        self.set_color(color)

    def __str__(self):
        '''A string representation of an Ellipse.'''
        (o, w, h, a) = self.get()
        return f'Ellipse({str(o)}, {str(w)}, {str(h)}, {str(a)})'

    def __repr__(self):
        '''A representation of an Ellipse.'''
        (o, w, h, a) = self.get()
        return f'Ellipse({str(o)}, {str(w)}, {str(h)}, {str(a)})'

    def get(self):
        '''Return a tuple of the attributes.'''
        return (self.origin, self.width, self.height, self.angle)

    def rotate(self, theta):
        '''Rotate an ellipse anti-clockwise around the origin by theta degrees'''
        t = deepcopy(self)
        t.origin = t.origin.rotate(theta)
        t.angle += theta
        return t

    def translate(self, vec):
        """Translate an ellipse by vec."""
        t = deepcopy(self)
        t.origin = t.origin.translate(vec)
        return t

    def set_color(self, color):
        """Set the circle's color."""
        self.color = color
        self.origin.set_color(color)
