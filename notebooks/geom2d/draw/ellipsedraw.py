import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from .adc import Adc

class EllipseDraw(Adc):
    '''Class to draw ellipses.'''

    def __init__(self, origin, width, height, angle, color='#4ca3dd', fill=True, alpha=0.2):
        '''Initialise the attributes.'''

        self.origin = origin
        self.width = width
        self.height = height
        self.angle = angle

        self.color  = color
        self.fill   = fill
        self.alpha  = alpha

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

    def draw(self, ax):
        '''Draw an ellipse.'''
        (o, w, h, a) = self.get()

        o.draw()
        
        ellipse = patches.Ellipse(
            [o.x, o.y], 
            w, h, a,
            color   = self.color, 
            fill    = self.fill, 
            alpha   = self.alpha
        )
        return ax.add_patch(ellipse)

        


