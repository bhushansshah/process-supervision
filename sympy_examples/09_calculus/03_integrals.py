"""
SymPy for Integrals
====================
Demonstrates indefinite and definite integration, applications
of integrals (area, volume), and improper integrals.

Relevant domain: Calculus > Integral Calculus > Applications of Integrals
"""

from sympy import (symbols, integrate, sin, cos, exp, log, sqrt, pi,
                   Rational, oo, simplify, Abs, Piecewise, N, tan, sec)

x, y, a, b = symbols('x y a b')

# ---------------------------------------------------------------------------
# Example 1: Basic Indefinite Integrals
# ---------------------------------------------------------------------------

print("=== Basic Indefinite Integrals ===")

integrands = [
    ("x^n", x**5),
    ("sin(x)", sin(x)),
    ("cos(x)", cos(x)),
    ("e^x", exp(x)),
    ("1/x", 1/x),
    ("x² + 3x - 1", x**2 + 3*x - 1),
    ("sec²(x)", 1/cos(x)**2),
]

for name, f in integrands:
    result = integrate(f, x)
    print(f"  ∫ {name} dx = {result}")

# ---------------------------------------------------------------------------
# Example 2: Definite Integrals
# ---------------------------------------------------------------------------

print("\n=== Definite Integrals ===")

# ∫₀¹ x² dx
print(f"∫₀¹ x² dx = {integrate(x**2, (x, 0, 1))}")

# ∫₀ᵖⁱ sin(x) dx
print(f"∫₀ᵖⁱ sin(x) dx = {integrate(sin(x), (x, 0, pi))}")

# ∫₁ᵉ 1/x dx
from sympy import E
print(f"∫₁ᵉ 1/x dx = {integrate(1/x, (x, 1, E))}")

# ∫₀¹ e^x dx
print(f"∫₀¹ eˣ dx = {integrate(exp(x), (x, 0, 1))}")

# ---------------------------------------------------------------------------
# Example 3: Area Between Curves
# ---------------------------------------------------------------------------

print("\n=== Area Between Curves ===")

# Area between y = x² and y = x from x=0 to x=1
f1 = x
f2 = x**2
area = integrate(f1 - f2, (x, 0, 1))
print(f"Area between y=x and y=x² on [0,1]: {area}")

# Area between y = sin(x) and y = 0 from 0 to π
area2 = integrate(sin(x), (x, 0, pi))
print(f"Area under y=sin(x) on [0,π]: {area2}")

# ---------------------------------------------------------------------------
# Example 4: Volume of Revolution (Disk Method)
# ---------------------------------------------------------------------------

print("\n=== Volume of Revolution ===")

# Rotate y = x² around x-axis from x=0 to x=2
y_func = x**2
V_disk = pi * integrate(y_func**2, (x, 0, 2))
print(f"Disk: rotate y=x² about x-axis, [0,2]: V = {V_disk}")

# Rotate y = √x around x-axis from x=0 to x=4
y_func = sqrt(x)
V_disk2 = pi * integrate(y_func**2, (x, 0, 4))
print(f"Disk: rotate y=√x about x-axis, [0,4]: V = {V_disk2}")

# Shell method: rotate y = x² about y-axis from x=0 to x=1
V_shell = 2 * pi * integrate(x * x**2, (x, 0, 1))
print(f"Shell: rotate y=x² about y-axis, [0,1]: V = {V_shell}")

# ---------------------------------------------------------------------------
# Example 5: Improper Integrals
# ---------------------------------------------------------------------------

print("\n=== Improper Integrals ===")

print(f"∫₁^∞ 1/x² dx = {integrate(1/x**2, (x, 1, oo))}")
print(f"∫₀^∞ e^(-x) dx = {integrate(exp(-x), (x, 0, oo))}")
print(f"∫₋∞^∞ e^(-x²) dx = {integrate(exp(-x**2), (x, -oo, oo))}")

# Divergent integral
result = integrate(1/x, (x, 1, oo))
print(f"∫₁^∞ 1/x dx = {result} (diverges)")

# ---------------------------------------------------------------------------
# Example 6: Average Value of a Function
# avg = (1/(b-a)) ∫ₐᵇ f(x) dx
# ---------------------------------------------------------------------------

print("\n=== Average Value ===")

f = x**2
a_val, b_val = 0, 3
avg = integrate(f, (x, a_val, b_val)) / (b_val - a_val)
print(f"Average of f(x) = x² on [0, 3]: {avg}")

f = sin(x)
avg2 = integrate(f, (x, 0, pi)) / pi
print(f"Average of sin(x) on [0, π]: {avg2}")

# ---------------------------------------------------------------------------
# Example 7: Arc Length via Integration
# L = ∫ √(1 + (dy/dx)²) dx
# ---------------------------------------------------------------------------

print("\n=== Arc Length ===")
from sympy import diff

y = x**2
dy_dx = diff(y, x)
arc_length = integrate(sqrt(1 + dy_dx**2), (x, 0, 1))
print(f"Arc length of y=x² from x=0 to x=1: {arc_length} ≈ {float(arc_length):.6f}")
