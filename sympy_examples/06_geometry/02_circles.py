"""
SymPy for Circles
==================
Demonstrates circle equations, tangent lines, intersections,
and circular geometry properties.

Relevant domain: Geometry > Plane Geometry > Circles
"""

from sympy.geometry import Point, Circle, Line, Triangle
from sympy import pi, sqrt, Rational, simplify, symbols, N

# ---------------------------------------------------------------------------
# Example 1: Circle Basics
# ---------------------------------------------------------------------------

print("=== Circle Basics ===")
c = Circle(Point(0, 0), 5)

print(f"Center: {c.center}")
print(f"Radius: {c.radius}")
print(f"Area: {c.area}")
print(f"Circumference: {c.circumference}")
print(f"Equation: {c.equation()}")

# Circle from 3 points
c2 = Circle(Point(0, 0), Point(1, 1), Point(2, 0))
print(f"\nCircle through (0,0), (1,1), (2,0):")
print(f"  Center: {c2.center}")
print(f"  Radius: {c2.radius}")

# ---------------------------------------------------------------------------
# Example 2: Point and Circle Relationships
# ---------------------------------------------------------------------------

print("\n=== Point and Circle Relationships ===")
c = Circle(Point(0, 0), 5)

points = [Point(3, 4), Point(0, 0), Point(6, 0), Point(2, 1)]
for p in points:
    dist = p.distance(c.center)
    if dist < c.radius:
        relation = "INSIDE"
    elif dist == c.radius:
        relation = "ON"
    else:
        relation = "OUTSIDE"
    print(f"  {p}: distance = {dist}, {relation} the circle")

# ---------------------------------------------------------------------------
# Example 3: Tangent Lines
# ---------------------------------------------------------------------------

print("\n=== Tangent Lines ===")
c = Circle(Point(0, 0), 3)

# Tangent lines from external point
ext_point = Point(5, 0)
tangents = c.tangent_lines(ext_point)
print(f"Tangent lines to circle (r=3) from (5,0):")
for t in tangents:
    print(f"  {t.equation()}")

# ---------------------------------------------------------------------------
# Example 4: Circle-Line Intersection
# ---------------------------------------------------------------------------

print("\n=== Circle-Line Intersection ===")
c = Circle(Point(0, 0), 5)
l = Line(Point(0, 0), Point(1, 1))

intersections = c.intersection(l)
print(f"Circle x²+y²=25 ∩ line y=x:")
for pt in intersections:
    print(f"  {pt}")

# Secant line
l2 = Line(Point(-6, 3), Point(6, 3))
intersections2 = c.intersection(l2)
print(f"\nCircle x²+y²=25 ∩ line y=3:")
for pt in intersections2:
    print(f"  {pt}")

# ---------------------------------------------------------------------------
# Example 5: Circle-Circle Intersection
# ---------------------------------------------------------------------------

print("\n=== Circle-Circle Intersection ===")
c1 = Circle(Point(0, 0), 3)
c2 = Circle(Point(4, 0), 3)

inter = c1.intersection(c2)
print(f"Circle 1 (center=origin, r=3) ∩ Circle 2 (center=(4,0), r=3):")
for pt in inter:
    print(f"  {pt}")

# ---------------------------------------------------------------------------
# Example 6: Inscribed and Circumscribed Circles of a Triangle
# ---------------------------------------------------------------------------

print("\n=== Triangle: Inscribed and Circumscribed Circles ===")
T = Triangle(Point(0, 0), Point(6, 0), Point(3, 4))

incircle = T.incircle
circumcircle = T.circumcircle

print(f"Triangle vertices: {T.vertices}")
print(f"Incircle center (incenter): {incircle.center}")
print(f"Incircle radius (inradius): {simplify(incircle.radius)}")
print(f"Circumcircle center: {circumcircle.center}")
print(f"Circumcircle radius: {simplify(circumcircle.radius)}")

# ---------------------------------------------------------------------------
# Example 7: Arc Length and Sector Area
# ---------------------------------------------------------------------------

print("\n=== Arc Length and Sector Area (computed symbolically) ===")
r, theta = symbols('r theta', positive=True)

arc_length = r * theta
sector_area = Rational(1, 2) * r**2 * theta

print(f"Arc length = r·θ = {arc_length}")
print(f"Sector area = ½r²θ = {sector_area}")

# Specific example: r=10, θ=π/3
print(f"\nFor r=10, θ=π/3:")
print(f"  Arc length = {arc_length.subs([(r, 10), (theta, pi/3)])}")
print(f"  Sector area = {sector_area.subs([(r, 10), (theta, pi/3)])}")
