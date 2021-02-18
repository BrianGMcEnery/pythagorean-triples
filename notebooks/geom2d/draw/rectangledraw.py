import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from .adc import Adc

class RectangleDraw(Adc):
    '''Class to draw triangles.'''

    def __init__(self, p1, p2, p3, p4, color='#4ca3dd', fill=True, alpha=0.2):
        '''Initialise the attributes.'''

        self.p1     = p1
        self.p2     = p2
        self.p3     = p3
        self.p4     = p4
        self.color  = color
        self.fill   = fill
        self.alpha  = alpha

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

    def draw(self, ax):
        '''Draw a triangle.'''
        (p1, p2, p3, p4) = self.get()
        p1.draw()
        p2.draw()
        p3.draw()
        p4.draw()
        array = np.array([
            [p1.x, p1.y],
            [p2.x, p2.y],
            [p3.x, p3.y],
            [p4.x, p4.y]
        ])

        rectangle = patches.Polygon(
            array, 
            color   = self.color, 
            fill    = self.fill, 
            alpha   = self.alpha
        )
        return ax.add_patch(rectangle)