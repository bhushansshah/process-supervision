"""
SymPy for Matrices
===================
Demonstrates matrix operations, eigenvalues, row reduction, inverse,
and solving linear systems.

Relevant domain: Algebra > Linear Algebra > Matrices
"""

from sympy import (Matrix, symbols, eye, zeros, ones, Rational,
                   simplify, sqrt, pprint, latex)

# ---------------------------------------------------------------------------
# Example 1: Matrix Creation and Basic Operations
# ---------------------------------------------------------------------------

print("=== Matrix Basics ===")
A = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

B = Matrix([[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])

print(f"A = {A}")
print(f"B = {B}")
print(f"A + B = {A + B}")
print(f"A * B = {A * B}")
print(f"3 * A = {3 * A}")
print(f"A^T = {A.T}")

# ---------------------------------------------------------------------------
# Example 2: Special Matrices
# ---------------------------------------------------------------------------

print("\n=== Special Matrices ===")
print(f"Identity 3x3:\n{eye(3)}")
print(f"Zero 2x3:\n{zeros(2, 3)}")
print(f"Ones 2x2:\n{ones(2, 2)}")
print(f"Diagonal:\n{Matrix.diag(1, 2, 3)}")

# ---------------------------------------------------------------------------
# Example 3: Determinant and Inverse
# ---------------------------------------------------------------------------

print("\n=== Determinant and Inverse ===")
M = Matrix([[2, 1, 1],
            [1, 3, 2],
            [1, 0, 0]])

det = M.det()
print(f"M = {M}")
print(f"det(M) = {det}")

if det != 0:
    M_inv = M.inv()
    print(f"M⁻¹ = {M_inv}")
    print(f"M * M⁻¹ = {simplify(M * M_inv)}")

# ---------------------------------------------------------------------------
# Example 4: Row Echelon Form and Rank
# ---------------------------------------------------------------------------

print("\n=== Row Reduction (RREF) ===")
A = Matrix([[1, 2, 3, 4],
            [2, 4, 6, 8],
            [1, 3, 5, 7]])

rref, pivots = A.rref()
print(f"A = {A}")
print(f"RREF = {rref}")
print(f"Pivot columns: {pivots}")
print(f"Rank: {A.rank()}")

# ---------------------------------------------------------------------------
# Example 5: Eigenvalues and Eigenvectors
# ---------------------------------------------------------------------------

print("\n=== Eigenvalues and Eigenvectors ===")
M = Matrix([[4, 1],
            [2, 3]])

eigenvals = M.eigenvals()
eigenvects = M.eigenvects()

print(f"M = {M}")
print(f"Eigenvalues (with multiplicity): {eigenvals}")
for val, mult, vects in eigenvects:
    print(f"  λ = {val} (multiplicity {mult}): eigenvectors = {vects}")

# Diagonalization
P, D = M.diagonalize()
print(f"\nDiagonalization: M = P·D·P⁻¹")
print(f"P = {P}")
print(f"D = {D}")
print(f"Verify P·D·P⁻¹ = {simplify(P * D * P.inv())}")

# ---------------------------------------------------------------------------
# Example 6: Solving Linear Systems  Ax = b
# ---------------------------------------------------------------------------

print("\n=== Solving Linear Systems ===")
A = Matrix([[2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]])
b = Matrix([8, -11, -3])

x = A.solve(b)
print(f"A = {A}")
print(f"b = {b.T}")
print(f"Solution x = {x.T}")
print(f"Verify Ax = {(A * x).T}")

# ---------------------------------------------------------------------------
# Example 7: Symbolic Matrices
# ---------------------------------------------------------------------------

print("\n=== Symbolic Matrices ===")
a, b, c, d = symbols('a b c d')
M = Matrix([[a, b],
            [c, d]])

print(f"M = {M}")
print(f"det(M) = {M.det()}")
print(f"trace(M) = {M.trace()}")
print(f"Characteristic poly: {M.charpoly().as_expr()}")

# Inverse of 2x2 matrix
print(f"M⁻¹ = {M.inv()}")

# ---------------------------------------------------------------------------
# Example 8: Null Space and Column Space
# ---------------------------------------------------------------------------

print("\n=== Null Space and Column Space ===")
A = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print(f"Null space: {A.nullspace()}")
print(f"Column space: {A.columnspace()}")
print(f"Row space: {A.rowspace()}")
