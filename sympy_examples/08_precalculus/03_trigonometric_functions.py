"""
SymPy for Trigonometric Functions
===================================
Demonstrates trig identities, simplification, equation solving,
and inverse trig functions.

Relevant domain: Precalculus > Trigonometric Functions
"""

from sympy import (symbols, sin, cos, tan, cot, sec, csc,
                   asin, acos, atan, atan2,
                   simplify, trigsimp, expand_trig, pi, sqrt,
                   Rational, solve, Eq, N, latex)

x, y, theta, alpha, beta = symbols('x y theta alpha beta')

# ---------------------------------------------------------------------------
# Example 1: Exact Trig Values
# ---------------------------------------------------------------------------

print("=== Exact Trigonometric Values ===")
angles = [0, pi/6, pi/4, pi/3, pi/2, pi]
print(f"{'Angle':<12} {'sin':<20} {'cos':<20} {'tan':<20}")
print("-" * 72)
for a in angles:
    s = sin(a)
    c = cos(a)
    t = tan(a) if a != pi/2 else "undefined"
    print(f"{str(a):<12} {str(s):<20} {str(c):<20} {str(t):<20}")

# ---------------------------------------------------------------------------
# Example 2: Trigonometric Identities (Verification)
# ---------------------------------------------------------------------------

print("\n=== Verifying Trig Identities ===")

# Pythagorean identity
identity1 = sin(x)**2 + cos(x)**2
print(f"sin²(x) + cos²(x) = {trigsimp(identity1)}")

# Double angle
print(f"sin(2x) = {expand_trig(sin(2*x))}")
print(f"cos(2x) = {expand_trig(cos(2*x))}")
print(f"tan(2x) = {expand_trig(tan(2*x))}")

# Sum formulas
print(f"\nsin(α+β) = {expand_trig(sin(alpha + beta))}")
print(f"cos(α+β) = {expand_trig(cos(alpha + beta))}")

# Half angle
half_angle = x / 2
print(f"\nHalf-angle identity demo:")
# SymPy simplification
expr = 2 * sin(x/2) * cos(x/2)
print(f"2·sin(x/2)·cos(x/2) = {trigsimp(expr)}")

# ---------------------------------------------------------------------------
# Example 3: Trigonometric Simplification
# ---------------------------------------------------------------------------

print("\n=== Trigonometric Simplification ===")

expr1 = sin(x)**2 - cos(x)**2
print(f"sin²x - cos²x = {trigsimp(expr1)}")

expr2 = sin(x) * cos(y) + cos(x) * sin(y)
print(f"sin(x)cos(y) + cos(x)sin(y) = {trigsimp(expr2)}")

expr3 = (1 - cos(2*x)) / 2
print(f"(1 - cos(2x))/2 = {trigsimp(expr3)}")

expr4 = sin(x)**4 + cos(x)**4
print(f"sin⁴x + cos⁴x = {trigsimp(expr4)}")

# ---------------------------------------------------------------------------
# Example 4: Solving Trigonometric Equations
# ---------------------------------------------------------------------------

print("\n=== Solving Trig Equations ===")

from sympy import solveset, S

# sin(x) = 1/2
sol = solveset(Eq(sin(x), Rational(1, 2)), x, domain=S.Reals)
print(f"sin(x) = 1/2  =>  x = {sol}")

# cos(x) = 0
sol = solveset(Eq(cos(x), 0), x, domain=S.Reals)
print(f"cos(x) = 0  =>  x = {sol}")

# 2sin²(x) - 1 = 0
sol = solveset(Eq(2*sin(x)**2 - 1, 0), x, domain=S.Reals)
print(f"2sin²(x) - 1 = 0  =>  x = {sol}")

# tan(x) = 1
sol = solveset(Eq(tan(x), 1), x, domain=S.Reals)
print(f"tan(x) = 1  =>  x = {sol}")

# ---------------------------------------------------------------------------
# Example 5: Inverse Trigonometric Functions
# ---------------------------------------------------------------------------

print("\n=== Inverse Trig Functions ===")
values = [Rational(-1, 1), -sqrt(3)/2, -sqrt(2)/2, Rational(-1, 2),
          0, Rational(1, 2), sqrt(2)/2, sqrt(3)/2, 1]

print("arcsin values:")
for v in values:
    try:
        result = asin(v)
        print(f"  arcsin({v}) = {result}")
    except:
        pass

print("\narccos values:")
for v in values:
    result = acos(v)
    print(f"  arccos({v}) = {result}")

# ---------------------------------------------------------------------------
# Example 6: Converting Between Degrees and Radians (Symbolic)
# ---------------------------------------------------------------------------

print("\n=== Degree-Radian Conversion ===")
degrees = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for d in degrees:
    rad = d * pi / 180
    print(f"  {d}° = {rad} radians")

# ---------------------------------------------------------------------------
# Example 7: Law of Cosines / Sines using SymPy trig
# ---------------------------------------------------------------------------

print("\n=== Trig Application: Triangle Solving ===")
# Given: triangle with sides a=7, b=10, angle C=60°
a_val, b_val = 7, 10
C = pi / 3

# Law of cosines: c² = a² + b² - 2ab·cos(C)
c_val = sqrt(a_val**2 + b_val**2 - 2*a_val*b_val*cos(C))
print(f"Sides a={a_val}, b={b_val}, angle C=60°")
print(f"c = √(a²+b²-2ab·cos C) = {simplify(c_val)} ≈ {float(c_val):.4f}")

# Law of sines to find angle A
A = asin(a_val * sin(C) / c_val)
print(f"A = arcsin(a·sin C/c) = {simplify(A)} ≈ {float(A * 180 / pi):.2f}°")
