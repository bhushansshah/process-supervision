"""
SymPy for Determinants
=======================
Demonstrates determinant computation, properties, cofactor expansion,
and applications of determinants.

Relevant domain: Algebra > Linear Algebra > Determinants
"""

from sympy import Matrix, symbols, det, simplify, Rational, expand

# ---------------------------------------------------------------------------
# Example 1: Computing Determinants
# ---------------------------------------------------------------------------

print("=== Computing Determinants ===")

# 2x2 determinant
A = Matrix([[3, 7],
            [1, 5]])
print(f"2x2 matrix A:\n{A}")
print(f"det(A) = {A.det()}")

# 3x3 determinant
B = Matrix([[2, 1, 3],
            [0, 4, 5],
            [1, 0, 2]])
print(f"\n3x3 matrix B:\n{B}")
print(f"det(B) = {B.det()}")

# 4x4 determinant
C = Matrix([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [2, 6, 4, 8],
            [3, 1, 1, 2]])
print(f"\n4x4 matrix C:\n{C}")
print(f"det(C) = {C.det()}")

# ---------------------------------------------------------------------------
# Example 2: Properties of Determinants
# ---------------------------------------------------------------------------

print("\n=== Properties of Determinants ===")

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(f"det(A) = {A.det()}")
print(f"det(B) = {B.det()}")
print(f"det(A*B) = {(A*B).det()}")
print(f"det(A) * det(B) = {A.det() * B.det()}")
print(f"det(A*B) == det(A)*det(B)? {(A*B).det() == A.det() * B.det()}")

print(f"\ndet(A^T) = {A.T.det()}")
print(f"det(A) = {A.det()}")
print(f"det(A^T) == det(A)? {A.T.det() == A.det()}")

k = 3
print(f"\ndet({k}A) = {(k*A).det()}")
print(f"{k}² * det(A) = {k**2 * A.det()}")
print(f"det(kA) == k^n * det(A)? {(k*A).det() == k**2 * A.det()}")

# ---------------------------------------------------------------------------
# Example 3: Cofactor and Adjugate Matrix
# ---------------------------------------------------------------------------

print("\n=== Cofactor and Adjugate ===")

M = Matrix([[1, 2, 3],
            [0, 4, 5],
            [1, 0, 6]])

print(f"M:\n{M}")
print(f"det(M) = {M.det()}")

cofactor_matrix = M.cofactor_matrix()
print(f"Cofactor matrix:\n{cofactor_matrix}")

adjugate = M.adjugate()
print(f"Adjugate (adj M):\n{adjugate}")
print(f"M * adj(M) = det(M) * I:\n{simplify(M * adjugate)}")

# ---------------------------------------------------------------------------
# Example 4: Minor Matrix
# ---------------------------------------------------------------------------

print("\n=== Minors ===")
M = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print(f"M:\n{M}")
for i in range(3):
    for j in range(3):
        minor = M.minor(i, j)
        print(f"  Minor M_{i+1}{j+1} = {minor}")

# ---------------------------------------------------------------------------
# Example 5: Cramer's Rule
# Solve Ax = b using determinants
# ---------------------------------------------------------------------------

print("\n=== Cramer's Rule ===")

A = Matrix([[2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]])
b = Matrix([8, -11, -3])

det_A = A.det()
print(f"A:\n{A}")
print(f"b = {b.T}")
print(f"det(A) = {det_A}")

# Replace each column with b and compute determinant
for col in range(3):
    A_mod = A.copy()
    A_mod[:, col] = b
    det_mod = A_mod.det()
    x_val = Rational(det_mod, det_A)
    print(f"x_{col+1} = det(A_{col+1})/det(A) = {det_mod}/{det_A} = {x_val}")

# Verify with direct solve
x_direct = A.solve(b)
print(f"Direct solve: x = {x_direct.T}")

# ---------------------------------------------------------------------------
# Example 6: Symbolic Determinant
# ---------------------------------------------------------------------------

print("\n=== Symbolic Determinant ===")
a, b, c, d, e, f, g, h, i = symbols('a b c d e f g h i')
M = Matrix([[a, b, c],
            [d, e, f],
            [g, h, i]])
print(f"det(M) = {expand(M.det())}")
