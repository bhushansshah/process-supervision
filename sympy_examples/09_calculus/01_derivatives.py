"""
SymPy for Derivatives
======================
Demonstrates differentiation: basic rules, chain rule, implicit
differentiation, higher-order derivatives, and partial derivatives.

Relevant domain: Calculus > Differential Calculus > Derivatives
"""

from sympy import (symbols, diff, sin, cos, tan, exp, log, sqrt,
                   simplify, Rational, Function, Eq, solve, oo,
                   Derivative, pprint, latex, ln)

x, y, z, t = symbols('x y z t')

# ---------------------------------------------------------------------------
# Example 1: Basic Derivative Rules
# ---------------------------------------------------------------------------

print("=== Basic Derivative Rules ===")

functions = [
    ("x^5", x**5),
    ("3x² + 2x - 7", 3*x**2 + 2*x - 7),
    ("sin(x)", sin(x)),
    ("cos(x)", cos(x)),
    ("e^x", exp(x)),
    ("ln(x)", log(x)),
    ("√x", sqrt(x)),
    ("1/x", 1/x),
    ("tan(x)", tan(x)),
]

for name, f in functions:
    print(f"  d/dx [{name}] = {diff(f, x)}")

# ---------------------------------------------------------------------------
# Example 2: Product and Quotient Rules
# ---------------------------------------------------------------------------

print("\n=== Product and Quotient Rules ===")

# Product rule: d/dx[f·g] = f'g + fg'
f = x**2 * sin(x)
print(f"d/dx [x²·sin(x)] = {diff(f, x)}")

g = exp(x) * cos(x)
print(f"d/dx [eˣ·cos(x)] = {diff(g, x)}")

# Quotient rule
h = sin(x) / x
print(f"d/dx [sin(x)/x] = {simplify(diff(h, x))}")

# ---------------------------------------------------------------------------
# Example 3: Chain Rule
# ---------------------------------------------------------------------------

print("\n=== Chain Rule ===")

f = sin(3*x + 1)
print(f"d/dx [sin(3x+1)] = {diff(f, x)}")

f = exp(x**2)
print(f"d/dx [e^(x²)] = {diff(f, x)}")

f = log(x**2 + 1)
print(f"d/dx [ln(x²+1)] = {diff(f, x)}")

f = (2*x + 3)**5
print(f"d/dx [(2x+3)⁵] = {diff(f, x)}")

f = sqrt(1 + sin(x))
print(f"d/dx [√(1+sin x)] = {simplify(diff(f, x))}")

# ---------------------------------------------------------------------------
# Example 4: Higher-Order Derivatives
# ---------------------------------------------------------------------------

print("\n=== Higher-Order Derivatives ===")

f = x**5 - 3*x**3 + 2*x
print(f"f(x) = {f}")
for order in range(1, 7):
    d = diff(f, x, order)
    print(f"  f{'′' * order}(x) = {d}")

# ---------------------------------------------------------------------------
# Example 5: Implicit Differentiation
# x² + y² = 25  => find dy/dx
# ---------------------------------------------------------------------------

print("\n=== Implicit Differentiation ===")

y_func = Function('y')(x)

# x² + y² = 25
equation = x**2 + y_func**2 - 25
# Differentiate both sides with respect to x
diff_eq = diff(equation, x)
dydx = solve(diff_eq, y_func.diff(x))[0]
print(f"x² + y² = 25")
print(f"d/dx: {diff_eq} = 0")
print(f"dy/dx = {dydx}")

# x³ + y³ = 6xy
equation2 = x**3 + y_func**3 - 6*x*y_func
diff_eq2 = diff(equation2, x)
dydx2 = solve(diff_eq2, y_func.diff(x))[0]
print(f"\nx³ + y³ = 6xy")
print(f"dy/dx = {simplify(dydx2)}")

# ---------------------------------------------------------------------------
# Example 6: Partial Derivatives
# ---------------------------------------------------------------------------

print("\n=== Partial Derivatives ===")

f = x**2*y + x*y**3 + x*y*z
print(f"f(x,y,z) = {f}")
print(f"∂f/∂x = {diff(f, x)}")
print(f"∂f/∂y = {diff(f, y)}")
print(f"∂f/∂z = {diff(f, z)}")
print(f"∂²f/∂x² = {diff(f, x, 2)}")
print(f"∂²f/∂x∂y = {diff(f, x, y)}")
print(f"∂²f/∂y∂x = {diff(f, y, x)}")
print(f"Mixed partials equal? {diff(f, x, y) == diff(f, y, x)}")

# ---------------------------------------------------------------------------
# Example 7: Unevaluated Derivatives (Symbolic)
# ---------------------------------------------------------------------------

print("\n=== Unevaluated (Symbolic) Derivatives ===")
f = Function('f')
g = Function('g')

# Chain rule symbolically
expr = f(g(x))
deriv = Derivative(expr, x)
print(f"d/dx [f(g(x))] = {deriv.doit()}")
