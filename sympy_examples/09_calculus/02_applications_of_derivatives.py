"""
SymPy for Applications of Derivatives
========================================
Demonstrates optimization, related rates, curve sketching,
tangent lines, and Taylor approximation.

Relevant domain: Calculus > Differential Calculus > Applications of Derivatives, Related Rates
"""

from sympy import (symbols, diff, solve, Eq, sqrt, Rational, pi, oo,
                   simplify, sign, Interval, S, limit, series, exp,
                   sin, cos, log, Abs, Function)

x, t, h = symbols('x t h')

# ---------------------------------------------------------------------------
# Example 1: Finding Critical Points and Extrema
# ---------------------------------------------------------------------------

print("=== Critical Points and Extrema ===")

f = x**3 - 6*x**2 + 9*x + 1
f_prime = diff(f, x)
f_double_prime = diff(f, x, 2)

critical_points = solve(f_prime, x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")
print(f"Critical points: x = {critical_points}")

for cp in critical_points:
    second_deriv = f_double_prime.subs(x, cp)
    if second_deriv > 0:
        print(f"  x = {cp}: f''({cp}) = {second_deriv} > 0 → LOCAL MINIMUM, f({cp}) = {f.subs(x, cp)}")
    elif second_deriv < 0:
        print(f"  x = {cp}: f''({cp}) = {second_deriv} < 0 → LOCAL MAXIMUM, f({cp}) = {f.subs(x, cp)}")
    else:
        print(f"  x = {cp}: f''({cp}) = 0 → INCONCLUSIVE")

# ---------------------------------------------------------------------------
# Example 2: Optimization Problem
# "Find the dimensions of a box with square base and volume 1000 cm³
#  that minimizes surface area."
# ---------------------------------------------------------------------------

print("\n=== Optimization: Box with Minimum Surface Area ===")
s, h_var = symbols('s h', positive=True)

volume = s**2 * h_var
surface = 2 * s**2 + 4 * s * h_var

# Constraint: volume = 1000
h_expr = solve(Eq(volume, 1000), h_var)[0]
surface_one_var = surface.subs(h_var, h_expr)
print(f"Surface area in terms of s: SA = {surface_one_var}")

# Minimize
dSA = diff(surface_one_var, s)
s_optimal = solve(dSA, s)
s_opt = [sol for sol in s_optimal if sol.is_real and sol > 0][0]
h_opt = h_expr.subs(s, s_opt)

print(f"Optimal base side: s = {s_opt} ≈ {float(s_opt):.4f} cm")
print(f"Optimal height: h = {simplify(h_opt)} ≈ {float(h_opt):.4f} cm")
print(f"Minimum surface area: {simplify(surface_one_var.subs(s, s_opt))} ≈ {float(surface_one_var.subs(s, s_opt)):.2f} cm²")

# ---------------------------------------------------------------------------
# Example 3: Related Rates
# "A ladder 10 ft long rests against a wall. Bottom slides away at 1 ft/s.
#  How fast is the top sliding down when bottom is 6 ft from wall?"
# ---------------------------------------------------------------------------

print("\n=== Related Rates: Sliding Ladder ===")

# x² + y² = 100 (ladder length 10)
# Differentiate: 2x(dx/dt) + 2y(dy/dt) = 0
# Solve for dy/dt = -x(dx/dt) / y

x_val = 6
y_val = sqrt(100 - x_val**2)  # = 8
dxdt = 1  # ft/s

# dy/dt = -x * (dx/dt) / y
dydt = -x_val * dxdt / y_val

print(f"x² + y² = 100")
print(f"Differentiating: 2x(dx/dt) + 2y(dy/dt) = 0")
print(f"When x={x_val}: y={y_val}, dx/dt={dxdt}")
print(f"dy/dt = -{x_val}*{dxdt}/{y_val} = {dydt} ft/s (negative = sliding down)")

# ---------------------------------------------------------------------------
# Example 4: Tangent Line
# ---------------------------------------------------------------------------

print("\n=== Tangent Line ===")

f = x**3 - 2*x + 1
x0 = 1
slope = diff(f, x).subs(x, x0)
y0 = f.subs(x, x0)
tangent = slope * (x - x0) + y0

print(f"f(x) = {f}")
print(f"At x = {x0}: f({x0}) = {y0}, f'({x0}) = {slope}")
print(f"Tangent line: y = {tangent}")

# ---------------------------------------------------------------------------
# Example 5: Newton's Method (one step)
# ---------------------------------------------------------------------------

print("\n=== Newton's Method ===")
f = x**3 - 2*x - 5
f_prime = diff(f, x)

x_n = Rational(2)  # Initial guess
print(f"Solving f(x) = {f} = 0")
print(f"x₀ = {x_n}")

for i in range(5):
    x_next = x_n - f.subs(x, x_n) / f_prime.subs(x, x_n)
    print(f"x_{i+1} = {float(x_next):.10f}")
    x_n = x_next

# ---------------------------------------------------------------------------
# Example 6: Taylor / Maclaurin Polynomial
# ---------------------------------------------------------------------------

print("\n=== Taylor Polynomial Approximation ===")

f = exp(x)
for order in [1, 2, 3, 5, 10]:
    taylor = series(f, x, 0, order + 1).removeO()
    error_at_1 = abs(float(taylor.subs(x, 1)) - float(exp(1)))
    print(f"  T_{order}(x) at x=1: approx = {float(taylor.subs(x, 1)):.8f}, "
          f"error = {error_at_1:.2e}")

# ---------------------------------------------------------------------------
# Example 7: L'Hôpital's Rule (SymPy handles automatically via limits)
# ---------------------------------------------------------------------------

print("\n=== L'Hôpital's Rule ===")

# 0/0 form
expr = sin(x) / x
print(f"lim(x→0) sin(x)/x = {limit(expr, x, 0)} [applied L'Hôpital]")

# ∞/∞ form
expr = log(x) / x
print(f"lim(x→∞) ln(x)/x = {limit(expr, x, oo)} [applied L'Hôpital]")

# Repeated application
expr = (exp(x) - 1 - x) / x**2
print(f"lim(x→0) (eˣ-1-x)/x² = {limit(expr, x, 0)} [applied twice]")
