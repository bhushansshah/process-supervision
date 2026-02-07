"""
SymPy for Polynomial Operations
=================================
Demonstrates polynomial arithmetic, division, roots, GCD,
and other polynomial manipulations.

Relevant domain: Algebra > Polynomial Operations
"""

from sympy import (symbols, Poly, div, gcd, lcm, factor, expand,
                   resultant, discriminant, roots, degree, LC, LT,
                   groebner, real_roots, count_roots, Rational,
                   together, cancel, apart)

x, y = symbols('x y')

# ---------------------------------------------------------------------------
# Example 1: Creating and Inspecting Polynomials
# ---------------------------------------------------------------------------

print("=== Polynomial Basics ===")
p = Poly(3*x**4 - 2*x**3 + x - 7, x)

print(f"Polynomial: {p.as_expr()}")
print(f"Degree: {p.degree()}")
print(f"Leading coefficient: {p.LC()}")
print(f"Coefficients: {p.all_coeffs()}")
print(f"Monomial terms: {p.as_dict()}")

# ---------------------------------------------------------------------------
# Example 2: Polynomial Arithmetic
# ---------------------------------------------------------------------------

print("\n=== Polynomial Arithmetic ===")
p1 = Poly(x**2 + 2*x + 1, x)
p2 = Poly(x + 3, x)

print(f"p1 = {p1.as_expr()}")
print(f"p2 = {p2.as_expr()}")
print(f"p1 + p2 = {(p1 + p2).as_expr()}")
print(f"p1 - p2 = {(p1 - p2).as_expr()}")
print(f"p1 * p2 = {(p1 * p2).as_expr()}")

# ---------------------------------------------------------------------------
# Example 3: Polynomial Division
# ---------------------------------------------------------------------------

print("\n=== Polynomial Division ===")
dividend = x**3 + 2*x**2 - x + 3
divisor = x - 1

quotient, remainder = div(dividend, divisor, x)
print(f"({dividend}) ÷ ({divisor})")
print(f"  Quotient:  {quotient}")
print(f"  Remainder: {remainder}")
print(f"  Verify: ({quotient}) * ({divisor}) + {remainder} = {expand(quotient * divisor + remainder)}")

# ---------------------------------------------------------------------------
# Example 4: Finding Roots
# ---------------------------------------------------------------------------

print("\n=== Finding Roots ===")

p = x**3 - 6*x**2 + 11*x - 6
r = roots(p, x)
print(f"Roots of {p}: {r}")
# Output format: {root: multiplicity}

p = x**4 - 1
r = roots(p, x)
print(f"Roots of {p}: {r}")

# Real roots only
p = x**5 - 3*x**3 + 2*x
rr = real_roots(p)
print(f"Real roots of {p}: {rr}")

# ---------------------------------------------------------------------------
# Example 5: GCD and LCM of Polynomials
# ---------------------------------------------------------------------------

print("\n=== Polynomial GCD and LCM ===")
p1 = x**3 - x
p2 = x**2 - 1

g = gcd(p1, p2)
l = lcm(p1, p2)
print(f"GCD({p1}, {p2}) = {g}")
print(f"LCM({p1}, {p2}) = {l}")

# ---------------------------------------------------------------------------
# Example 6: Discriminant
# ---------------------------------------------------------------------------

print("\n=== Discriminant ===")
a, b, c = symbols('a b c')
# For quadratic ax^2 + bx + c
disc = discriminant(Poly(a*x**2 + b*x + c, x))
print(f"Discriminant of ax² + bx + c = {disc}")

# Specific example
disc_val = discriminant(Poly(x**2 - 4*x + 4, x))
print(f"Discriminant of x² - 4x + 4 = {disc_val} (perfect square, one repeated root)")

disc_val = discriminant(Poly(x**2 + 1, x))
print(f"Discriminant of x² + 1 = {disc_val} (negative, complex roots)")

# ---------------------------------------------------------------------------
# Example 7: Polynomial Composition
# ---------------------------------------------------------------------------

print("\n=== Polynomial Composition ===")
f = x**2 + 1
g = 2*x - 3

fog = f.subs(x, g)
gof = g.subs(x, f)
print(f"f(x) = {f}")
print(f"g(x) = {g}")
print(f"f(g(x)) = {expand(fog)}")
print(f"g(f(x)) = {expand(gof)}")
