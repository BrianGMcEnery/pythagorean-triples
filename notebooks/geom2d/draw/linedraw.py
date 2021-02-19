import matplotlib.pyplot as plt
from .adc import Adc

class LineDraw(Adc):
    '''Class to draw line.'''

    def __init__(self, p1, p2, color='#696969', linewidth=1, linestyle='-'):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.linewidth = linewidth
        self.linestyle = linestyle

    def __str__(self):
        '''A string representation of a LineDraw object.'''
        (p1, p2) = self.get()
        return f'LineDraw({str(p1)}, {str(p2)})'

    def __repr__(self):
        '''A representation of a LineDraw object.'''
        (p1, p2) = self.get()
        return f'LineDraw({repr(p1)}, {repr(p2)})'

    def get(self):
        '''Return a tuple consisting of the points.'''
        return (self.p1, self.p2)

    def draw(self, ax):
        ''' Draw a line.'''
        (p1, p2) = self.get()
        p1.draw()
        p2.draw()

        m = (p2.y - p1.y)/(p2.x - p1.x)
        c = p1.y - m * p1.x

        def y(x):
            y = m * x + c
            return y

        x_values = list(ax.get_xlim())
        y_values = [y(x) for x in x_values]
        plt.plot(
            x_values,
            y_values,
            color=self.color,
            linewidth=self.linewidth,
            linestyle=self.linestyle
        )