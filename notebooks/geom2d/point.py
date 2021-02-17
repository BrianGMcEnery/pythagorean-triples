from .agc import Agc
from math import sqrt, cos, sin, radians
from copy import deepcopy

class Point(Agc):
    ''' Class to represent a 2-d point.'''

    def __init__(self, x=0, y=0, color='blue'):
        '''Initialise a Point object'''
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        '''A string representation of a Point object'''
        return f'Point({self.x}, {self.y})'

    def __repr__(self):
        '''A representation of a Point object'''
        return f'Point({self.x}, {self.y})'

    def get(self):
        '''Return (x, y) as a tuple'''
        return (self.x, self.y)

    def dist(self, p):
        '''Return the distance between two points'''
        (x, y) = self.get()
        (xp, yp) = p.get()
        return sqrt((x - xp) ** 2 + (y - yp) ** 2)

    def rotate(self, theta):
        '''Rotate a point anti-clockwise around the origin by theta degrees'''
        def rotate_origin_only(xy, radians):
            """Only rotate a point around the origin (0, 0)."""
            x, y = xy
            xx = x * cos(-radians) + y * sin(-radians)
            yy = -x * sin(-radians) + y * cos(-radians)
            return xx, yy

        p = deepcopy(self)
        (p.x, p.y) = rotate_origin_only((p.x, p.y), radians(theta))
        return p

    def translate(self, vec):
        """Translate a point by vec."""
        def translate_by_vec(xy, v_xy):
            """Translate a point by a vector v"""
            x, y = xy
            v_x, v_y = v_xy
            return x + v_x, y + v_y

        p = deepcopy(self)
        
        (p.x, p.y) = translate_by_vec((p.x, p.y), vec.get())
        return p