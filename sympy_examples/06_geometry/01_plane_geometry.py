"""
SymPy for Plane Geometry (Polygons, Angles, Area, Perimeter)
==============================================================
Demonstrates geometric objects, area/perimeter calculations,
angle measurement, and polygon properties.

Relevant domain: Geometry > Plane Geometry > Polygons, Angles, Area, Perimeter
"""

from sympy.geometry import (Point, Line, Segment, Triangle, RegularPolygon,
                             Polygon, Circle, Ray)
from sympy import pi, sqrt, Rational, simplify, N, symbols, cos, sin

# ---------------------------------------------------------------------------
# Example 1: Points and Distances
# ---------------------------------------------------------------------------

print("=== Points and Distances ===")
A = Point(0, 0)
B = Point(3, 4)
C = Point(6, 0)

print(f"A = {A}, B = {B}, C = {C}")
print(f"Distance A to B: {A.distance(B)}")
print(f"Distance B to C: {B.distance(C)}")
print(f"Midpoint of AB: {Segment(A, B).midpoint}")

# ---------------------------------------------------------------------------
# Example 2: Lines and Angles
# ---------------------------------------------------------------------------

print("\n=== Lines and Angles ===")
l1 = Line(Point(0, 0), Point(1, 1))
l2 = Line(Point(0, 0), Point(1, 0))

angle = l1.angle_between(l2)
print(f"Line 1: through (0,0) and (1,1)")
print(f"Line 2: through (0,0) and (1,0)")
print(f"Angle between lines: {angle} radians = {N(angle * 180 / pi, 4)}°")

# Parallel and perpendicular lines
l3 = Line(Point(0, 1), slope=1)
l4 = Line(Point(0, 0), slope=-1)
print(f"\nAre y=x+1 and y=x parallel? {l1.is_parallel(l3)}")
print(f"Are y=x and y=-x perpendicular? {l1.is_perpendicular(l4)}")

# Line equation
print(f"Equation of line through (0,0) and (3,4): {Line(Point(0,0), Point(3,4)).equation()}")

# ---------------------------------------------------------------------------
# Example 3: Triangles
# ---------------------------------------------------------------------------

print("\n=== Triangles ===")
T = Triangle(Point(0, 0), Point(4, 0), Point(2, 3))

print(f"Vertices: {T.vertices}")
print(f"Area: {T.area}")
print(f"Perimeter: {T.perimeter}")
print(f"Centroid: {T.centroid}")
print(f"Circumcenter: {T.circumcenter}")
print(f"Incenter: {T.incenter}")
print(f"Orthocenter: {T.orthocenter}")

# Angles
angles = T.angles
print(f"Angles: {angles}")
print(f"Sum of angles: {sum(angles.values())} = π ? {simplify(sum(angles.values()) - pi) == 0}")

# Type checking
print(f"Is right triangle? {T.is_right()}")
print(f"Is isosceles? {T.is_isosceles()}")
print(f"Is equilateral? {T.is_equilateral()}")

# ---------------------------------------------------------------------------
# Example 4: Regular Polygons
# ---------------------------------------------------------------------------

print("\n=== Regular Polygons ===")

for n in [3, 4, 5, 6, 8]:
    poly = RegularPolygon(Point(0, 0), 1, n)
    print(f"Regular {n}-gon (unit radius):")
    print(f"  Area: {simplify(poly.area)}")
    print(f"  Perimeter: {simplify(poly.perimeter)}")
    print(f"  Interior angle: {simplify(poly.interior_angle)} rad = {N(poly.interior_angle * 180 / pi)}°")
    print(f"  Apothem: {simplify(poly.apothem)}")

# ---------------------------------------------------------------------------
# Example 5: Area Formulas
# ---------------------------------------------------------------------------

print("\n=== Area Calculations ===")

# Arbitrary polygon area (Shoelace formula)
quad = Polygon(Point(0, 0), Point(4, 0), Point(5, 3), Point(1, 4))
print(f"Quadrilateral vertices: {quad.vertices}")
print(f"Area (Shoelace): {quad.area}")
print(f"Perimeter: {quad.perimeter}")
print(f"Is convex? {quad.is_convex()}")

# ---------------------------------------------------------------------------
# Example 6: Geometric Predicates
# ---------------------------------------------------------------------------

print("\n=== Geometric Predicates ===")

A, B, C = Point(0, 0), Point(1, 1), Point(2, 2)
print(f"Are (0,0), (1,1), (2,2) collinear? {Point.is_collinear(A, B, C)}")

D = Point(1, 0)
print(f"Are (0,0), (1,1), (1,0) collinear? {Point.is_collinear(A, B, D)}")

# Point in polygon
poly = Polygon(Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4))
test_point = Point(2, 2)
print(f"Is (2,2) inside the square? {poly.encloses_point(test_point)}")
