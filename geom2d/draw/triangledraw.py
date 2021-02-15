import matplotlib.pyplot as plt
from .adc import Adc

class TriangleDraw(Adc):
    '''Class to draw triangles.'''

    def __init__(self, p1, p2, p3, color='#4ca3dd', fill=True, alpha=0.2):
        '''Initialise the attributes.'''

        self.p1     = p1
        self.p2     = p2
        self.p3     = p3
        self.color  = color
        self.fill   = fill
        self.alpha  = alpha

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

    def draw(self):
        pass


