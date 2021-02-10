from pygeom import Axes, Point, Rectangle

# Create the cartesian axis
axes = Axes(xlim=(-1,7), ylim=(-1,7), figsize=(12,10))

# Points
bottomLeft = Point(1, 1, color='red')
topRight = Point(5, 4, color='green')

shape = Rectangle(bottomLeft, topRight, alpha=0.5)

axes.addMany([bottomLeft, topRight])
axes.add(shape)
axes.draw()