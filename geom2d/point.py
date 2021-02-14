from .agc import Agc

class Point(Agc):
    ''' Class to represent a 2-d point.'''

    def __init__(self, x=0, y=0):
        '''Initialise a Point object'''
        self.x = x
        self.y = y

    def __str__(self):
        '''A string representation of a Point object'''
        return f'Point({self.x}, {self.y})'

    def __repr__(self):
        '''A representation of a Point object'''
        return f'Point({self.x}, {self.y})'

    def get(self):
        '''Return (x, y) as a tuple'''
        return (self.x, self.y)