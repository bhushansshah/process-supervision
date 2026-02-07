"""
SymPy for Linear Transformations
==================================
Demonstrates representing and analyzing linear transformations
using matrices — rotation, scaling, reflection, and more.

Relevant domain: Algebra > Linear Algebra > Linear Transformations
"""

from sympy import (Matrix, symbols, cos, sin, pi, sqrt, simplify,
                   eye, Rational, N, trigsimp)

theta = symbols('theta')

# ---------------------------------------------------------------------------
# Example 1: 2D Rotation Matrix
# ---------------------------------------------------------------------------

print("=== 2D Rotation Matrix ===")
R = Matrix([[cos(theta), -sin(theta)],
            [sin(theta),  cos(theta)]])
print(f"R(θ) =\n{R}")

# Rotate the point (1, 0) by 90 degrees
R_90 = R.subs(theta, pi/2)
point = Matrix([1, 0])
rotated = R_90 * point
print(f"\nRotate (1, 0) by 90°: {rotated.T}")

# Rotate (1, 1) by 45 degrees
R_45 = R.subs(theta, pi/4)
point2 = Matrix([1, 1])
rotated2 = simplify(R_45 * point2)
print(f"Rotate (1, 1) by 45°: {rotated2.T}")

# Composition of rotations
R_a = R.subs(theta, symbols('alpha'))
R_b = R.subs(theta, symbols('beta'))
composed = trigsimp(R_a * R_b)
print(f"\nR(α)·R(β) = R(α+β)? Composition:\n{composed}")

# ---------------------------------------------------------------------------
# Example 2: Scaling Transformation
# ---------------------------------------------------------------------------

print("\n=== Scaling Transformation ===")
sx, sy = symbols('s_x s_y')
S = Matrix([[sx, 0],
            [0, sy]])
print(f"Scale matrix S =\n{S}")

# Scale (3, 4) by 2x horizontally, 3x vertically
point = Matrix([3, 4])
scaled = S.subs([(sx, 2), (sy, 3)]) * point
print(f"Scale (3,4) by (2x, 3x): {scaled.T}")

# ---------------------------------------------------------------------------
# Example 3: Reflection Transformations
# ---------------------------------------------------------------------------

print("\n=== Reflection Transformations ===")

# Reflect over x-axis
Rx = Matrix([[1, 0], [0, -1]])
print(f"Reflect (2, 3) over x-axis: {(Rx * Matrix([2, 3])).T}")

# Reflect over y-axis
Ry = Matrix([[-1, 0], [0, 1]])
print(f"Reflect (2, 3) over y-axis: {(Ry * Matrix([2, 3])).T}")

# Reflect over y=x
Ryx = Matrix([[0, 1], [1, 0]])
print(f"Reflect (2, 3) over y=x: {(Ryx * Matrix([2, 3])).T}")

# Reflect over arbitrary line through origin at angle θ/2
R_line = Matrix([[cos(theta), sin(theta)],
                 [sin(theta), -cos(theta)]])
print(f"\nReflection over line at angle θ/2:\n{R_line}")

# ---------------------------------------------------------------------------
# Example 4: Shear Transformation
# ---------------------------------------------------------------------------

print("\n=== Shear Transformation ===")
k = symbols('k')
shear_x = Matrix([[1, k], [0, 1]])  # Horizontal shear
shear_y = Matrix([[1, 0], [k, 1]])  # Vertical shear

point = Matrix([1, 1])
print(f"Horizontal shear (k=2) of (1,1): {(shear_x.subs(k, 2) * point).T}")
print(f"Vertical shear (k=3) of (1,1):   {(shear_y.subs(k, 3) * point).T}")

# ---------------------------------------------------------------------------
# Example 5: Kernel and Image of a Transformation
# ---------------------------------------------------------------------------

print("\n=== Kernel and Image ===")

# T: R^3 -> R^2 given by matrix A
A = Matrix([[1, 2, 3],
            [4, 5, 6]])

kernel = A.nullspace()
image = A.columnspace()
print(f"Transformation matrix:\n{A}")
print(f"Kernel (null space): {kernel}")
print(f"Image (column space): {image}")
print(f"dim(kernel) + dim(image) = {len(kernel)} + {len(image)} = {len(kernel) + len(image)} = n = {A.cols}")

# ---------------------------------------------------------------------------
# Example 6: Change of Basis
# ---------------------------------------------------------------------------

print("\n=== Change of Basis ===")

# Standard basis representation
A = Matrix([[2, 1],
            [1, 3]])

# New basis vectors
v1 = Matrix([1, 1])
v2 = Matrix([1, -1])
P = Matrix([v1.T, v2.T]).T  # Change of basis matrix

# Representation in new basis
A_new = simplify(P.inv() * A * P)
print(f"Original matrix A:\n{A}")
print(f"Change of basis matrix P:\n{P}")
print(f"A in new basis (P⁻¹AP):\n{A_new}")
