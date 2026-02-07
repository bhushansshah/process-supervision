"""
SymPy for Equations and Inequalities
======================================
Demonstrates solving equations (linear, quadratic, polynomial, rational)
and inequalities symbolically.

Relevant domain: Algebra > Equations and Inequalities
"""

from sympy import (symbols, Eq, solve, solveset, S, oo, sqrt, Rational,
                   Abs, Piecewise, And, Or, Interval, Union, FiniteSet,
                   simplify, latex)

x, y = symbols('x y')

# ---------------------------------------------------------------------------
# Example 1: Linear Equations
# ---------------------------------------------------------------------------

print("=== Linear Equations ===")

eq = Eq(3*x + 7, 22)
print(f"3x + 7 = 22  =>  x = {solve(eq, x)}")

eq = Eq(5*x - 2*(x + 3), 9)
print(f"5x - 2(x+3) = 9  =>  x = {solve(eq, x)}")

# ---------------------------------------------------------------------------
# Example 2: Quadratic Equations
# ---------------------------------------------------------------------------

print("\n=== Quadratic Equations ===")

eq = Eq(x**2 - 5*x + 6, 0)
print(f"x² - 5x + 6 = 0  =>  x = {solve(eq, x)}")

eq = Eq(2*x**2 + 3*x - 2, 0)
print(f"2x² + 3x - 2 = 0  =>  x = {solve(eq, x)}")

# Complex roots
eq = Eq(x**2 + 4, 0)
print(f"x² + 4 = 0  =>  x = {solve(eq, x)}")

# Using quadratic formula symbolically
a, b, c = symbols('a b c')
quadratic = Eq(a*x**2 + b*x + c, 0)
roots = solve(quadratic, x)
print(f"ax² + bx + c = 0  =>  x = {roots}")

# ---------------------------------------------------------------------------
# Example 3: Polynomial Equations
# ---------------------------------------------------------------------------

print("\n=== Polynomial Equations ===")

eq = Eq(x**3 - 6*x**2 + 11*x - 6, 0)
print(f"x³ - 6x² + 11x - 6 = 0  =>  x = {solve(eq, x)}")

eq = Eq(x**4 - 5*x**2 + 4, 0)
print(f"x⁴ - 5x² + 4 = 0  =>  x = {solve(eq, x)}")

# ---------------------------------------------------------------------------
# Example 4: Rational Equations
# ---------------------------------------------------------------------------

print("\n=== Rational Equations ===")

eq = Eq(1/x + 1/(x+1), Rational(5, 6))
sol = solve(eq, x)
print(f"1/x + 1/(x+1) = 5/6  =>  x = {sol}")

# ---------------------------------------------------------------------------
# Example 5: Absolute Value Equations
# ---------------------------------------------------------------------------

print("\n=== Absolute Value Equations ===")

# Solve |2x - 3| = 7 by splitting into two cases
x_real = symbols('x', real=True)
sol_pos = solve(Eq(2*x_real - 3, 7), x_real)
sol_neg = solve(Eq(2*x_real - 3, -7), x_real)
print(f"|2x - 3| = 7  =>  x = {sol_pos + sol_neg}")

# ---------------------------------------------------------------------------
# Example 6: Inequalities
# ---------------------------------------------------------------------------

print("\n=== Inequalities ===")

# Linear inequality
sol = solveset(2*x - 5 > 0, x, domain=S.Reals)
print(f"2x - 5 > 0  =>  x ∈ {sol}")

# Quadratic inequality
sol = solveset(x**2 - 4 < 0, x, domain=S.Reals)
print(f"x² - 4 < 0  =>  x ∈ {sol}")

sol = solveset(x**2 - 5*x + 6 >= 0, x, domain=S.Reals)
print(f"x² - 5x + 6 >= 0  =>  x ∈ {sol}")

# Rational inequality
sol = solveset((x - 1) / (x + 2) > 0, x, domain=S.Reals)
print(f"(x-1)/(x+2) > 0  =>  x ∈ {sol}")

# ---------------------------------------------------------------------------
# Example 7: System of Equations
# ---------------------------------------------------------------------------

print("\n=== System of Non-Linear Equations ===")

# Circle and line intersection
sol = solve([Eq(x**2 + y**2, 25), Eq(y, x + 1)], [x, y])
print(f"x² + y² = 25 and y = x + 1  =>  {sol}")

# Two parabolas
sol = solve([Eq(y, x**2), Eq(y, 2*x + 3)], [x, y])
print(f"y = x² and y = 2x + 3  =>  {sol}")
