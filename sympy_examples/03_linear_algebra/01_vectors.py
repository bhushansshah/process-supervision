"""
SymPy for Vectors
==================
Demonstrates vector operations including dot product, cross product,
magnitude, projection, and symbolic vector manipulation.

Relevant domain: Algebra > Linear Algebra > Vectors
"""

from sympy import symbols, sqrt, Rational, simplify, cos, acos, pi, Matrix
from sympy.vector import CoordSys3D

# ---------------------------------------------------------------------------
# Example 1: Vector Basics using Matrix representation
# ---------------------------------------------------------------------------

print("=== Vector Basics (Matrix Representation) ===")

v1 = Matrix([1, 2, 3])
v2 = Matrix([4, 5, 6])

print(f"v1 = {v1.T}")
print(f"v2 = {v2.T}")
print(f"v1 + v2 = {(v1 + v2).T}")
print(f"v1 - v2 = {(v1 - v2).T}")
print(f"3 * v1  = {(3 * v1).T}")

# ---------------------------------------------------------------------------
# Example 2: Dot Product and Angle
# ---------------------------------------------------------------------------

print("\n=== Dot Product and Angle Between Vectors ===")

dot = v1.dot(v2)
mag_v1 = v1.norm()
mag_v2 = v2.norm()
angle = acos(dot / (mag_v1 * mag_v2))

print(f"v1 · v2 = {dot}")
print(f"|v1| = {mag_v1} = {simplify(mag_v1)}")
print(f"|v2| = {mag_v2} = {simplify(mag_v2)}")
print(f"Angle between v1 and v2 = {angle}")
print(f"  ≈ {float(angle):.4f} radians ≈ {float(angle * 180 / pi):.2f}°")

# ---------------------------------------------------------------------------
# Example 3: Cross Product
# ---------------------------------------------------------------------------

print("\n=== Cross Product ===")

cross = v1.cross(v2)
print(f"v1 × v2 = {cross.T}")
print(f"|v1 × v2| = {cross.norm()} = {simplify(cross.norm())}")

# Verify perpendicularity
print(f"(v1 × v2) · v1 = {cross.dot(v1)} (should be 0)")
print(f"(v1 × v2) · v2 = {cross.dot(v2)} (should be 0)")

# ---------------------------------------------------------------------------
# Example 4: Projection
# ---------------------------------------------------------------------------

print("\n=== Vector Projection ===")

# Projection of v1 onto v2
proj = (v1.dot(v2) / v2.dot(v2)) * v2
print(f"proj_v2(v1) = {proj.T}")

# Scalar projection
scalar_proj = v1.dot(v2) / v2.norm()
print(f"Scalar projection = {scalar_proj} ≈ {float(scalar_proj):.4f}")

# ---------------------------------------------------------------------------
# Example 5: Unit Vectors
# ---------------------------------------------------------------------------

print("\n=== Unit Vectors ===")

unit_v1 = v1 / v1.norm()
print(f"Unit vector of v1 = {unit_v1.T}")
print(f"|unit_v1| = {simplify(unit_v1.norm())}")

# ---------------------------------------------------------------------------
# Example 6: Symbolic Vectors using CoordSys3D
# ---------------------------------------------------------------------------

print("\n=== Symbolic Vectors (CoordSys3D) ===")

N = CoordSys3D('N')
a, b, c, d, e, f = symbols('a b c d e f')

vec1 = a*N.i + b*N.j + c*N.k
vec2 = d*N.i + e*N.j + f*N.k

print(f"vec1 = {vec1}")
print(f"vec2 = {vec2}")
print(f"vec1 · vec2 = {vec1.dot(vec2)}")
print(f"vec1 × vec2 = {vec1.cross(vec2)}")

# ---------------------------------------------------------------------------
# Example 7: Linear Independence Check
# ---------------------------------------------------------------------------

print("\n=== Linear Independence ===")

v1 = Matrix([1, 2, 3])
v2 = Matrix([4, 5, 6])
v3 = Matrix([7, 8, 9])

# Form a matrix with vectors as columns
M = Matrix([v1.T, v2.T, v3.T]).T
rank = M.rank()
print(f"Vectors: {v1.T}, {v2.T}, {v3.T}")
print(f"Matrix rank: {rank}")
print(f"Linearly independent: {rank == 3}")
