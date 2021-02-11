from .utils import is_pythagorean_triple
from math import sqrt

class Triple:
    '''
    Class representing a pythagorean triple.
    '''

    def __init__(self, x, y, r):
        '''
        Instantiate a Triple object
        '''

        if is_pythagorean_triple(x, y, r):
            self.x, self.y, self.r = x, y, r
        else:
            raise ValueError(f'{x, y, r} is not a valid triple.')

    def get(self):
        '''
        Returns a tuple of (x, y, r).
        '''
        return self.x, self.y, self.r

    def complement(self):
        '''
        Complementary angle triple.
        '''
        x, y, r = self.get()
        return Triple(y, x, r)

    def supplement(self):
        '''
        Supplementary angle triple. If a is the original angle, 
        180 - a is the supplementary angle.
        '''
        x, y, r = self.get()
        return Triple(-x, y, r)

    def add(self, t):
        # Triples pp. 8
        '''
        Returns a new triple which is the sum of two triples.
        '''
        (x, y, r) = self.get()
        (xt, yt, rt) = t.get()
        return Triple(x * xt - y * yt, y * xt + x * yt, r * rt)

    def sub(self, t):
        # Triples pp. 10
        '''
        Returns a new triple which is the difference of two triples.
        '''
        (x, y, r) = self.get()
        (xt, yt, rt) = t.get()
        return Triple(x * xt + y * yt, y * xt - x * yt, r * rt)

    def double(self):
        # Triples pp. 8
        '''
        Returns a new triple corresponding to the double angle.
        '''
        (x, y, r) = self.get()
        return Triple(x * x - y * y, 2 * x * y, r * r)

    def half(self):
        # Triples pp. 17
        '''
        Returns a new triple corresponding to the half angle.
        '''
        (x, y, r) = self.get()
        (x, y) = (x + r, y)
        r = sqrt(x * x + y * y)
        return Triple(x, y, r)

    @staticmethod
    def quadrant_angle(value):
        # Triples pp. 13, 14
        '''
        Returns a new triple corresponding to the quadrant angles,
        [0, 90, 180, 270, 360].
        '''
        quadrant_triples = {
            0: Triple(1, 0, 1),
            90: Triple(0, 1, 1),
            180: Triple(-1, 0, 1),
            270: Triple(0, -1, 1),
            360: Triple(1, 0, 1),
        }
        if value not in quadrant_triples.keys():
            raise ValueError(f'{value} is not a quadrant angle.')
        else:
            return quadrant_triples[value]

    @staticmethod
    def special_angle(value):
        # Triples pp. 16
        '''
        Returns a new triple corresponding to the special angles,
        [30, 45, 60].
        '''
        special_triples = {
            30: Triple(sqrt(3), 1, 2),
            45: Triple(1, 1, sqrt(2)),
            60: Triple(1, sqrt(3), 2),
        }
        if value not in special_triples.keys():
            raise ValueError(f'{value} is not a special angle.')
        else:
            return special_triples[value]

