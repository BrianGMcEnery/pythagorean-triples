from pygeom import Axes, Point, Polygon

# Create the cartesian axis
axes = Axes(xlim=(-1,10), ylim=(-1,10), figsize=(12,10))

# Points
p1 = Point(1, 1, color='red')
p2 = Point(1, 2, color='green')
p3 = Point(4, 7, color='red')
p4 = Point(9, 1, color='green')


shape = Polygon([p1, p2, p3, p4], alpha=0.5)

axes.addMany([p1, p2, p3, p4])
axes.add(shape)
axes.draw()