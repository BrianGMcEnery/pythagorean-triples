from pygeom import Axes, Point, Triangle, Vector

# Create the cartesian axis
axes = Axes(xlim=(-1,6), ylim=(-1,6), figsize=(8,6))

# Points
p1 = Point(0, 0, color='grey')
p2 = Point(3, 0, color='grey')
p3 = Point(3, 4, color='grey')
p4 = Point(1.5, 3)

tr = Triangle(p1, p2, p3, alpha=0.5)
v = Vector(p1, p4)

axes.addMany([p1, p2, p3])
axes.add(tr)
axes.add(v)
axes.draw()