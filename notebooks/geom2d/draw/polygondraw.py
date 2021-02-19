import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from .adc import Adc

class PolygonDraw(Adc):
    '''Class to draw polygons.'''

    def __init__(self, vertices, color='#4ca3dd', fill=True, alpha=0.2):
        '''Initialise the attributes.'''

        self.vertices = vertices
        self.color  = color
        self.fill   = fill
        self.alpha  = alpha

    def __str__(self):
        '''A string representation of a Polygon.'''
        return f'Polygon([{self.get()}])'

    def __repr__(self):
        '''A representation of a Polygon.'''
        return f'Polygon([{self.get()}])'

    def get(self):
        '''Return a tuple of the points.'''
        return self.vertices

    def draw(self, ax):
        '''Draw a polygon.'''
        vs = self.get()
        for p in vs:
            p.draw()

        ps = [[p.x, p.y] for p in vs]

        array = np.array(ps)

        polygon = patches.Polygon(
            array, 
            color   = self.color, 
            fill    = self.fill, 
            alpha   = self.alpha
        )
        return ax.add_patch(polygon)