"""
SymPy for Techniques of Integration
======================================
Demonstrates integration techniques: substitution, integration by parts,
partial fractions, trigonometric integrals, and more.

Relevant domain: Calculus > Integral Calculus > Techniques of Integration
"""

from sympy import (symbols, integrate, sin, cos, tan, sec, csc, exp, log,
                   sqrt, pi, Rational, simplify, apart, oo, atan, asin,
                   trigsimp)

x = symbols('x')

# ---------------------------------------------------------------------------
# Example 1: U-Substitution (SymPy handles automatically)
# ---------------------------------------------------------------------------

print("=== U-Substitution (automatic) ===")

# ∫ 2x·cos(x²) dx  [u = x²]
print(f"∫ 2x·cos(x²) dx = {integrate(2*x*cos(x**2), x)}")

# ∫ x·e^(x²) dx  [u = x²]
print(f"∫ x·e^(x²) dx = {integrate(x*exp(x**2), x)}")

# ∫ sin(x)/cos(x) dx  [u = cos(x)]
print(f"∫ tan(x) dx = {integrate(tan(x), x)}")

# ∫ x/(x²+1) dx  [u = x²+1]
print(f"∫ x/(x²+1) dx = {integrate(x/(x**2 + 1), x)}")

# ---------------------------------------------------------------------------
# Example 2: Integration by Parts
# ∫ u dv = uv - ∫ v du
# ---------------------------------------------------------------------------

print("\n=== Integration by Parts ===")

# ∫ x·e^x dx
print(f"∫ x·eˣ dx = {integrate(x*exp(x), x)}")

# ∫ x·sin(x) dx
print(f"∫ x·sin(x) dx = {integrate(x*sin(x), x)}")

# ∫ x²·e^x dx  (requires two applications)
print(f"∫ x²·eˣ dx = {integrate(x**2 * exp(x), x)}")

# ∫ ln(x) dx
print(f"∫ ln(x) dx = {integrate(log(x), x)}")

# ∫ x·ln(x) dx
print(f"∫ x·ln(x) dx = {integrate(x*log(x), x)}")

# ∫ arctan(x) dx
print(f"∫ arctan(x) dx = {integrate(atan(x), x)}")

# ---------------------------------------------------------------------------
# Example 3: Trigonometric Integrals
# ---------------------------------------------------------------------------

print("\n=== Trigonometric Integrals ===")

print(f"∫ sin²(x) dx = {integrate(sin(x)**2, x)}")
print(f"∫ cos²(x) dx = {integrate(cos(x)**2, x)}")
print(f"∫ sin³(x) dx = {integrate(sin(x)**3, x)}")
print(f"∫ sin²(x)·cos²(x) dx = {integrate(sin(x)**2 * cos(x)**2, x)}")
print(f"∫ sec³(x) dx = {simplify(integrate(sec(x)**3, x))}")
print(f"∫ tan²(x) dx = {integrate(tan(x)**2, x)}")

# ---------------------------------------------------------------------------
# Example 4: Partial Fractions Integration
# ---------------------------------------------------------------------------

print("\n=== Partial Fractions Integration ===")

# ∫ 1/(x²-1) dx
f = 1/(x**2 - 1)
print(f"Partial fractions of 1/(x²-1): {apart(f, x)}")
print(f"∫ 1/(x²-1) dx = {integrate(f, x)}")

# ∫ (3x+5)/(x²+4x+3) dx
f = (3*x + 5) / (x**2 + 4*x + 3)
print(f"\nPartial fractions: {apart(f, x)}")
print(f"∫ (3x+5)/(x²+4x+3) dx = {integrate(f, x)}")

# ∫ x/(x-1)² dx
f = x / (x - 1)**2
print(f"\n∫ x/(x-1)² dx = {integrate(f, x)}")

# ---------------------------------------------------------------------------
# Example 5: Trigonometric Substitution
# ---------------------------------------------------------------------------

print("\n=== Trigonometric Substitution (automatic) ===")

# ∫ 1/√(1-x²) dx  [x = sin θ]
print(f"∫ 1/√(1-x²) dx = {integrate(1/sqrt(1-x**2), x)}")

# ∫ 1/√(x²+1) dx  [x = tan θ]
print(f"∫ 1/√(x²+1) dx = {integrate(1/sqrt(x**2+1), x)}")

# ∫ √(4-x²) dx  [x = 2sin θ]
print(f"∫ √(4-x²) dx = {integrate(sqrt(4-x**2), x)}")

# ∫ 1/(x²+4) dx
print(f"∫ 1/(x²+4) dx = {integrate(1/(x**2+4), x)}")

# ---------------------------------------------------------------------------
# Example 6: Definite Integrals with Techniques
# ---------------------------------------------------------------------------

print("\n=== Definite Integrals ===")

# ∫₀¹ x·e^(-x) dx
print(f"∫₀¹ x·e^(-x) dx = {integrate(x*exp(-x), (x, 0, 1))}")

# ∫₀^(π/2) sin²(x) dx
print(f"∫₀^(π/2) sin²(x) dx = {integrate(sin(x)**2, (x, 0, pi/2))}")

# ∫₀^∞ e^(-x²) dx  (Gaussian integral)
print(f"∫₀^∞ e^(-x²) dx = {integrate(exp(-x**2), (x, 0, oo))}")

# ∫₋∞^∞ e^(-x²) dx  (full Gaussian)
print(f"∫₋∞^∞ e^(-x²) dx = {integrate(exp(-x**2), (x, -oo, oo))}")
