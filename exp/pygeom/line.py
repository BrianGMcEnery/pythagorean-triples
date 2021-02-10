from pygeom import Axes, Point, Line

# Create the cartesian axis
axes = Axes(xlim=(-1,7), ylim=(-1,7), figsize=(7,6))

# Points
p1 = Point(1, 1, color='red')
p2 = Point(5, 4, color='green')

l = Line(p1=p1, p2=p2)

axes.addMany([p1, p2, l])
axes.draw("line_demo.png")