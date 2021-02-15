import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import SubplotZero
from .drawfactory import DrawFactory

class Drawing:
    '''Main class to represent a drawing.'''

    def __init__(self, xlim=(-5, 5), ylim=(-5, 5), figsize=(10, 5)):
        self.xlim = xlim
        self.ylim = ylim
        self.figsize = figsize
        
        self.ax = None
        self.drawfactory = DrawFactory()

        self.shapes = {
            "Point": [],
            "LineSegment": [],
            "Triangle": [],
        }

    def draw(self):
        self.fig = plt.figure(figsize=self.figsize)

        self.ax = SubplotZero(self.fig, 1, 1, 1)
        self.fig.add_subplot(self.ax)

        for shape in ["Point", "LineSegment"]:
            drawshapes = self.drawfactory.make_draw_objects(
                self.shapes[shape]
            )
            for s in drawshapes:
                s.draw()

        for shape in ["Triangle"]:
            drawshapes = self.drawfactory.make_draw_objects(
                self.shapes[shape]
            )
            for s in drawshapes:
                s.draw(self.ax)

        

    def addMany(self, shapes):
        for shape in shapes:
            self.add(shape)

    def add(self, shape):
        classname = type(shape).__name__
        self.shapes[classname].append(shape)