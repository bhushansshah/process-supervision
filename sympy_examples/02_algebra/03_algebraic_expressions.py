"""
SymPy for Algebraic Expressions
=================================
Demonstrates simplification, expansion, factoring, and substitution
of algebraic expressions.

Relevant domain: Algebra > Algebraic Expressions
"""

from sympy import (symbols, expand, factor, simplify, collect, cancel,
                   apart, together, radsimp, sqrt, Rational, powsimp,
                   trigsimp, sin, cos)

x, y, z, a, b, c = symbols('x y z a b c')

# ---------------------------------------------------------------------------
# Example 1: Expansion
# ---------------------------------------------------------------------------

print("=== Expansion ===")
expr1 = (x + 2) * (x - 3)
print(f"(x + 2)(x - 3) = {expand(expr1)}")

expr2 = (x + y) ** 3
print(f"(x + y)^3 = {expand(expr2)}")

expr3 = (2*x - 1) * (3*x + 4)
print(f"(2x - 1)(3x + 4) = {expand(expr3)}")

expr4 = (a + b) * (a - b)
print(f"(a + b)(a - b) = {expand(expr4)}")

# ---------------------------------------------------------------------------
# Example 2: Factoring
# ---------------------------------------------------------------------------

print("\n=== Factoring ===")
expr1 = x**2 - 5*x + 6
print(f"x² - 5x + 6 = {factor(expr1)}")

expr2 = x**3 - 8
print(f"x³ - 8 = {factor(expr2)}")

expr3 = x**4 - 1
print(f"x⁴ - 1 = {factor(expr3)}")

expr4 = 6*x**2 + 7*x - 3
print(f"6x² + 7x - 3 = {factor(expr4)}")

expr5 = x**2 - y**2
print(f"x² - y² = {factor(expr5)}")

# ---------------------------------------------------------------------------
# Example 3: Simplification
# ---------------------------------------------------------------------------

print("\n=== Simplification ===")
expr1 = (x**2 + 2*x + 1) / (x + 1)
print(f"(x² + 2x + 1)/(x + 1) = {simplify(expr1)}")

expr2 = (x**3 - x) / (x**2 - 1)
print(f"(x³ - x)/(x² - 1) = {cancel(expr2)}")

expr3 = sin(x)**2 + cos(x)**2
print(f"sin²(x) + cos²(x) = {trigsimp(expr3)}")

# ---------------------------------------------------------------------------
# Example 4: Collecting Terms
# ---------------------------------------------------------------------------

print("\n=== Collecting Terms ===")
expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
collected = collect(expr, x)
print(f"Collect by x: {collected}")

# ---------------------------------------------------------------------------
# Example 5: Partial Fractions
# ---------------------------------------------------------------------------

print("\n=== Partial Fractions ===")
expr = (3*x + 5) / (x**2 - 1)
print(f"(3x + 5)/(x² - 1) = {apart(expr, x)}")

expr2 = (x**2 + 1) / (x**3 + x**2 - x - 1)
print(f"(x² + 1)/(x³ + x² - x - 1) = {apart(expr2, x)}")

# ---------------------------------------------------------------------------
# Example 6: Substitution
# ---------------------------------------------------------------------------

print("\n=== Substitution ===")
expr = x**2 + 3*x + 2
print(f"f(x) = {expr}")
print(f"f(2)  = {expr.subs(x, 2)}")
print(f"f(-1) = {expr.subs(x, -1)}")
print(f"f(a)  = {expr.subs(x, a)}")
print(f"f(x+1) = {expand(expr.subs(x, x + 1))}")

# Multiple substitution
expr_multi = x**2 + y**2 + z
result = expr_multi.subs([(x, 1), (y, 2), (z, 3)])
print(f"\nx² + y² + z at (x=1, y=2, z=3) = {result}")
