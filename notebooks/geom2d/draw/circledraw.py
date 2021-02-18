import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from .adc import Adc

class CircleDraw(Adc):
    '''Class to draw circles.'''

    def __init__(self, origin, radius, color='#4ca3dd', fill=True, alpha=0.2):
        '''Initialise the attributes.'''

        self.origin = origin
        self.radius = radius
        self.color  = color
        self.fill   = fill
        self.alpha  = alpha

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

    def draw(self, ax):
        '''Draw a circle.'''
        (origin, radius) = self.get()

        origin.draw()
        
        circle = patches.Circle(
            [origin.x, origin.y], 
            radius,
            color   = self.color, 
            fill    = self.fill, 
            alpha   = self.alpha
        )
        return ax.add_patch(circle)

        


