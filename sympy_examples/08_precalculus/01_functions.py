"""
SymPy for Functions (Precalculus)
==================================
Demonstrates function analysis: domain, range, composition,
inverse functions, and piecewise functions.

Relevant domain: Precalculus > Functions
"""

from sympy import (symbols, sqrt, Rational, log, exp, solve, Eq, oo,
                   S, solveset, Interval, Union, FiniteSet, simplify,
                   Piecewise, Abs, Function, Lambda, plot)

x, y = symbols('x y')

# ---------------------------------------------------------------------------
# Example 1: Defining and Evaluating Functions
# ---------------------------------------------------------------------------

print("=== Defining and Evaluating Functions ===")

# Using Lambda (anonymous function)
f = Lambda(x, x**2 + 3*x - 5)
print(f"f(x) = x² + 3x - 5")
print(f"f(0) = {f(0)}")
print(f"f(2) = {f(2)}")
print(f"f(-3) = {f(-3)}")
print(f"f(a+1) = {f(symbols('a') + 1).expand()}")

# ---------------------------------------------------------------------------
# Example 2: Domain of a Function
# ---------------------------------------------------------------------------

print("\n=== Domain Analysis ===")

# f(x) = 1/(x-2)  — domain excludes x=2
expr1 = 1 / (x - 2)
# Find where denominator is zero
excluded = solve(x - 2, x)
print(f"f(x) = 1/(x-2): domain = ℝ \\ {{{excluded[0]}}}")

# g(x) = √(x-3)  — domain requires x ≥ 3
domain_g = solveset(x - 3 >= 0, x, domain=S.Reals)
print(f"g(x) = √(x-3): domain = {domain_g}")

# h(x) = ln(x)  — domain requires x > 0
domain_h = Interval.open(0, oo)
print(f"h(x) = ln(x): domain = {domain_h}")

# Combined: f(x) = √(x) / (x - 4)
domain_combined = Interval(0, oo) - FiniteSet(4)
print(f"f(x) = √x/(x-4): domain = {domain_combined}")

# ---------------------------------------------------------------------------
# Example 3: Function Composition
# ---------------------------------------------------------------------------

print("\n=== Function Composition ===")

f_expr = x**2 + 1
g_expr = 2*x - 3

fog = f_expr.subs(x, g_expr)
gof = g_expr.subs(x, f_expr)

print(f"f(x) = {f_expr}")
print(f"g(x) = {g_expr}")
print(f"f(g(x)) = f(2x-3) = {fog.expand()}")
print(f"g(f(x)) = g(x²+1) = {gof.expand()}")
print(f"f ∘ g ≠ g ∘ f: {fog.expand() != gof.expand()}")

# ---------------------------------------------------------------------------
# Example 4: Inverse Functions
# ---------------------------------------------------------------------------

print("\n=== Inverse Functions ===")

# f(x) = 2x + 3, find f⁻¹
f_expr = 2*x + 3
# Solve y = 2x + 3 for x
f_inv = solve(Eq(y, f_expr), x)[0]
print(f"f(x) = {f_expr}")
print(f"f⁻¹(y) = {f_inv}")

# g(x) = x² (x ≥ 0), inverse is √x
g_expr = x**2
g_inv = sqrt(y)  # Taking positive root
print(f"\ng(x) = {g_expr} (x ≥ 0)")
print(f"g⁻¹(y) = {g_inv}")

# Verify: f(f⁻¹(x)) = x
verify = f_expr.subs(x, f_inv.subs(y, x))
print(f"\nVerify f(f⁻¹(x)) = {simplify(verify)}")

# ---------------------------------------------------------------------------
# Example 5: Piecewise Functions
# ---------------------------------------------------------------------------

print("\n=== Piecewise Functions ===")

f_pw = Piecewise(
    (x**2, x < 0),
    (x + 1, (x >= 0) & (x < 3)),
    (7, x >= 3)
)
print(f"f(x) = {f_pw}")
print(f"f(-2) = {f_pw.subs(x, -2)}")
print(f"f(0)  = {f_pw.subs(x, 0)}")
print(f"f(2)  = {f_pw.subs(x, 2)}")
print(f"f(5)  = {f_pw.subs(x, 5)}")

# ---------------------------------------------------------------------------
# Example 6: Even and Odd Functions
# ---------------------------------------------------------------------------

print("\n=== Even/Odd Function Test ===")

functions = {
    'x²': x**2,
    'x³': x**3,
    'x² + 1': x**2 + 1,
    'x³ + x': x**3 + x,
    'x² + x': x**2 + x,
    '|x|': Abs(x),
}

for name, f_expr in functions.items():
    f_neg = f_expr.subs(x, -x)
    is_even = simplify(f_expr - f_neg) == 0
    is_odd = simplify(f_expr + f_neg) == 0
    label = "even" if is_even else ("odd" if is_odd else "neither")
    print(f"  f(x) = {name}: {label}")

# ---------------------------------------------------------------------------
# Example 7: Finding Zeros / X-Intercepts
# ---------------------------------------------------------------------------

print("\n=== Finding Zeros ===")
functions_zeros = [
    x**2 - 4,
    x**3 - 6*x**2 + 11*x - 6,
    x**2 + 1,
    2*x - 7,
]

for f_expr in functions_zeros:
    zeros = solve(f_expr, x)
    print(f"  f(x) = {f_expr}: zeros at x = {zeros}")
