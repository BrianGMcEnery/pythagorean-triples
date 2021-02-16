import matplotlib.pyplot as plt
from .adc import Adc

class PointDraw(Adc):
    ''' Class to draw a point.'''
    
    def __init__(self, x, y, color = '#4ca3dd', size = 50, zorder=10):
        '''Initialise attributes of this class'''
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.zorder = zorder

    def __str__(self):
        (x, y) = (self.x, self.y)
        return f'Point({x}, {y})'

    def __repr__(self):
        (x, y) = (self.x, self.y)
        return f'Point({x}, {y})'

    def draw(self):
        plt.scatter([self.x], [self.y], color=self.color, 
                    s=self.size, zorder=self.zorder)
