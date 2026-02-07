"""
SymPy for Triangles and Triangulation
=======================================
Demonstrates triangle properties, trigonometric rules (law of cosines,
law of sines), and triangle congruence/similarity.

Relevant domain: Geometry > Plane Geometry > Triangulations
"""

from sympy.geometry import Point, Triangle, Segment, Line
from sympy import (symbols, cos, sin, sqrt, Rational, simplify, pi, N,
                   acos, asin, solve, Eq, Symbol, tan)

# ---------------------------------------------------------------------------
# Example 1: Triangle from Vertices
# ---------------------------------------------------------------------------

print("=== Triangle Properties ===")
T = Triangle(Point(0, 0), Point(5, 0), Point(2, 4))

sides = T.sides
print(f"Vertices: {T.vertices}")
print(f"Side lengths:")
for i, s in enumerate(sides):
    print(f"  Side {i+1}: {simplify(s.length)}")

print(f"Area: {T.area}")
print(f"Perimeter: {simplify(T.perimeter)}")
print(f"Is right: {T.is_right()}")
print(f"Is isosceles: {T.is_isosceles()}")
print(f"Is scalene: {T.is_scalene()}")

# ---------------------------------------------------------------------------
# Example 2: Law of Cosines
# c² = a² + b² - 2ab·cos(C)
# ---------------------------------------------------------------------------

print("\n=== Law of Cosines ===")
a, b, c_side = symbols('a b c', positive=True)
A_angle, B_angle, C_angle = symbols('A B C', positive=True)

# Given: a=7, b=10, C=60°, find c
a_val, b_val, C_val = 7, 10, pi/3
c_squared = a_val**2 + b_val**2 - 2*a_val*b_val*cos(C_val)
c_val = sqrt(c_squared)
print(f"Given a={a_val}, b={b_val}, C=60°")
print(f"c² = a² + b² - 2ab·cos(C) = {c_squared}")
print(f"c = {simplify(c_val)} ≈ {float(c_val):.4f}")

# Find angle given three sides: a=3, b=4, c=5
a_v, b_v, c_v = 3, 4, 5
cos_C = (a_v**2 + b_v**2 - c_v**2) / (2 * a_v * b_v)
angle_C = acos(cos_C)
print(f"\nGiven a=3, b=4, c=5")
print(f"cos(C) = {cos_C}")
print(f"C = {angle_C} = {N(angle_C * 180 / pi)}°")

# ---------------------------------------------------------------------------
# Example 3: Law of Sines
# a/sin(A) = b/sin(B) = c/sin(C)
# ---------------------------------------------------------------------------

print("\n=== Law of Sines ===")

# Given: a=8, A=30°, B=45°, find b
a_val = 8
A_val = pi/6   # 30°
B_val = pi/4   # 45°

# a/sin(A) = b/sin(B)
b_val = a_val * sin(B_val) / sin(A_val)
print(f"Given a={a_val}, A=30°, B=45°")
print(f"b = a·sin(B)/sin(A) = {simplify(b_val)} ≈ {float(b_val):.4f}")

# Find C
C_val = pi - A_val - B_val
c_val = a_val * sin(C_val) / sin(A_val)
print(f"C = 180° - 30° - 45° = {N(C_val * 180 / pi)}°")
print(f"c = {simplify(c_val)} ≈ {float(c_val):.4f}")

# ---------------------------------------------------------------------------
# Example 4: Heron's Formula
# Area = √(s(s-a)(s-b)(s-c))  where s = (a+b+c)/2
# ---------------------------------------------------------------------------

print("\n=== Heron's Formula ===")
a, b, c = symbols('a b c', positive=True)
s = (a + b + c) / 2
heron = sqrt(s * (s - a) * (s - b) * (s - c))

print(f"s = (a+b+c)/2 = {s}")
print(f"Area = √(s(s-a)(s-b)(s-c))")

# Specific: a=13, b=14, c=15
a_v, b_v, c_v = 13, 14, 15
s_v = (a_v + b_v + c_v) / 2
area = sqrt(s_v * (s_v - a_v) * (s_v - b_v) * (s_v - c_v))
print(f"\nFor a=13, b=14, c=15:")
print(f"  s = {s_v}")
print(f"  Area = {area}")

# ---------------------------------------------------------------------------
# Example 5: Triangle Centers
# ---------------------------------------------------------------------------

print("\n=== Triangle Centers ===")
T = Triangle(Point(0, 0), Point(6, 0), Point(3, 5))

print(f"Centroid (intersection of medians): {T.centroid}")
print(f"Circumcenter (equidistant from vertices): {T.circumcenter}")
print(f"Incenter (equidistant from sides): {T.incenter}")
print(f"Orthocenter (intersection of altitudes): {T.orthocenter}")

# Verify Euler line: Centroid lies on line through Circumcenter and Orthocenter
O = T.circumcenter
G = T.centroid
H = T.orthocenter
euler_line = Line(O, H)
print(f"\nEuler line passes through centroid? {euler_line.contains(G)}")

# ---------------------------------------------------------------------------
# Example 6: Similar Triangles
# ---------------------------------------------------------------------------

print("\n=== Similar Triangles ===")
T1 = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
T2 = Triangle(Point(0, 0), Point(6, 0), Point(0, 8))

print(f"T1 sides: {[simplify(s.length) for s in T1.sides]}")
print(f"T2 sides: {[simplify(s.length) for s in T2.sides]}")
print(f"Are T1 and T2 similar? {T1.is_similar(T2)}")

# Scale factor
ratio = simplify(T2.sides[0].length / T1.sides[0].length)
print(f"Scale factor: {ratio}")
print(f"Area ratio: {simplify(T2.area / T1.area)}")
