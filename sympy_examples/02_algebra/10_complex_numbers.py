"""
SymPy for Complex Numbers
===========================
Demonstrates complex number arithmetic, polar form, roots of unity,
and complex analysis basics.

Relevant domain: Algebra > Intermediate Algebra > Complex Numbers
"""

from sympy import (I, sqrt, Abs, arg, conjugate, re, im, exp, pi,
                   simplify, expand, symbols, solve, Eq, cos, sin,
                   Rational, trigsimp, roots, N)

# ---------------------------------------------------------------------------
# Example 1: Complex Number Arithmetic
# ---------------------------------------------------------------------------

print("=== Complex Number Arithmetic ===")
z1 = 3 + 4*I
z2 = 1 - 2*I

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 - z2 = {z1 - z2}")
print(f"z1 * z2 = {expand(z1 * z2)}")
print(f"z1 / z2 = {simplify(z1 / z2)}")
print(f"z1² = {expand(z1**2)}")

# ---------------------------------------------------------------------------
# Example 2: Components and Properties
# ---------------------------------------------------------------------------

print("\n=== Components and Properties ===")
z = 3 + 4*I
print(f"z = {z}")
print(f"Re(z) = {re(z)}")
print(f"Im(z) = {im(z)}")
print(f"|z| (modulus) = {Abs(z)}")
print(f"z̄ (conjugate) = {conjugate(z)}")
print(f"arg(z) = {arg(z)}")
print(f"z * z̄ = {expand(z * conjugate(z))}")
print(f"|z|² = {Abs(z)**2}")

# ---------------------------------------------------------------------------
# Example 3: Polar Form
# z = r(cos θ + i sin θ) = r·e^(iθ)
# ---------------------------------------------------------------------------

print("\n=== Polar Form ===")
z = 1 + I*sqrt(3)
r = Abs(z)
theta = arg(z)
print(f"z = {z}")
print(f"r = |z| = {r}")
print(f"θ = arg(z) = {theta}")
print(f"Polar form: {r} * e^(i·{theta})")

# Convert back
z_from_polar = r * exp(I * theta)
print(f"Back to rectangular: {simplify(z_from_polar)}")

# ---------------------------------------------------------------------------
# Example 4: Euler's Formula
# e^(iθ) = cos(θ) + i·sin(θ)
# ---------------------------------------------------------------------------

print("\n=== Euler's Formula ===")
theta = symbols('theta', real=True)
euler = exp(I * theta)
print(f"e^(iθ) expanded = {euler.rewrite(cos)}")
print(f"e^(iπ) = {exp(I * pi)}")
print(f"e^(iπ) + 1 = {exp(I * pi) + 1}  (Euler's identity!)")

# ---------------------------------------------------------------------------
# Example 5: Roots of Unity
# The n-th roots of unity: z^n = 1
# ---------------------------------------------------------------------------

print("\n=== Roots of Unity ===")
z = symbols('z')

for n in [3, 4, 5]:
    r = solve(z**n - 1, z)
    print(f"The {n}-th roots of unity:")
    for i, root in enumerate(r):
        val = N(root, 4)
        print(f"  ω_{i} = {root} ≈ {val}")
    print()

# ---------------------------------------------------------------------------
# Example 6: Solving Equations with Complex Numbers
# ---------------------------------------------------------------------------

print("=== Complex Equations ===")
z = symbols('z')

# z² + 2z + 5 = 0  (complex roots)
sol = solve(z**2 + 2*z + 5, z)
print(f"z² + 2z + 5 = 0  =>  z = {sol}")

# z³ = 8
sol = solve(z**3 - 8, z)
print(f"z³ = 8  =>  z = {sol}")

# z⁴ + 16 = 0
sol = solve(z**4 + 16, z)
print(f"z⁴ + 16 = 0  =>  z = {sol}")

# ---------------------------------------------------------------------------
# Example 7: De Moivre's Theorem
# (cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)
# ---------------------------------------------------------------------------

print("\n=== De Moivre's Theorem ===")
theta = symbols('theta', real=True)
n = 3
lhs = (cos(theta) + I * sin(theta))**n
expanded = expand(lhs)
simplified = trigsimp(re(expanded))
print(f"(cos θ + i sin θ)³:")
print(f"  Real part = cos(3θ) = {trigsimp(re(expanded))}")
print(f"  Imag part = sin(3θ) = {trigsimp(im(expanded))}")
