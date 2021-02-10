from pygeom import Axes, Point

# Create the cartesian axis
axes = Axes(xlim=(-1,8), ylim=(-1,18), figsize=(9,7))

# Create two points
p1 = Point(2,  5, color='#ffa500')
p2 = Point(7, 17, color='#0000ff')

axes.addMany([p1, p2])
axes.draw()