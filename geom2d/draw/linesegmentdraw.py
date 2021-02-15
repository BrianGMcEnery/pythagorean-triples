import matplotlib.pyplot as plt
from .adc import Adc

class LineSegmentDraw(Adc):
    '''Class to draw linesegments.'''

    def __init__(self, p1, p2, color='#696969', linewidth=1, linestyle='-'):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.linewidth = linewidth
        self.linestyle = linestyle

    def __str__(self):
        '''A string representation of a LineSegment object.'''
        (p1, p2) = self.get()
        return f'LineSegment({str(p1)}, {str(p2)})'

    def __repr__(self):
        '''A representation of a LineSegment object.'''
        (p1, p2) = self.get()
        return f'LineSegment({repr(p1)}, {repr(p2)})'

    def get(self):
        '''Return a tuple consisting of the end points.'''
        return (self.p1, self.p2)

    def draw(self):
        ''' Draw a linesegment.'''
        (p1, p2) = self.get()
        plt.plot(
            [p1.x, p2.x],
            [p1.y, p2.y],
            color=self.color,
            linewidth=self.linewidth,
            linestyle=self.linestyle
        )