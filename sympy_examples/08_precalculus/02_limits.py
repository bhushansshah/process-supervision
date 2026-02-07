"""
SymPy for Limits
=================
Demonstrates computing limits: finite, infinite, one-sided,
and limits involving indeterminate forms.

Relevant domain: Precalculus > Limits
"""

from sympy import (symbols, limit, oo, sin, cos, tan, exp, log, sqrt,
                   Rational, E, pi, simplify, Symbol)

x = symbols('x')

# ---------------------------------------------------------------------------
# Example 1: Basic Limits
# ---------------------------------------------------------------------------

print("=== Basic Limits ===")

# Polynomial limit
print(f"lim(x→2) x² - 3x + 2 = {limit(x**2 - 3*x + 2, x, 2)}")

# Rational function
print(f"lim(x→1) (x²-1)/(x-1) = {limit((x**2 - 1)/(x - 1), x, 1)}")

# Square root
print(f"lim(x→4) (√x - 2)/(x - 4) = {limit((sqrt(x) - 2)/(x - 4), x, 4)}")

# ---------------------------------------------------------------------------
# Example 2: Limits at Infinity
# ---------------------------------------------------------------------------

print("\n=== Limits at Infinity ===")

print(f"lim(x→∞) 1/x = {limit(1/x, x, oo)}")
print(f"lim(x→∞) (3x² + 2x)/(x² + 1) = {limit((3*x**2 + 2*x)/(x**2 + 1), x, oo)}")
print(f"lim(x→∞) x/eˣ = {limit(x/exp(x), x, oo)}")
print(f"lim(x→∞) ln(x)/x = {limit(log(x)/x, x, oo)}")
print(f"lim(x→∞) (1 + 1/x)ˣ = {limit((1 + 1/x)**x, x, oo)}")

# ---------------------------------------------------------------------------
# Example 3: One-Sided Limits
# ---------------------------------------------------------------------------

print("\n=== One-Sided Limits ===")

# lim(x→0⁺) 1/x = +∞
print(f"lim(x→0⁺) 1/x = {limit(1/x, x, 0, '+')}")
print(f"lim(x→0⁻) 1/x = {limit(1/x, x, 0, '-')}")

# Step function behavior
print(f"lim(x→0⁺) 1/x² = {limit(1/x**2, x, 0, '+')}")
print(f"lim(x→0⁻) 1/x² = {limit(1/x**2, x, 0, '-')}")

# ln(x) as x→0⁺
print(f"lim(x→0⁺) ln(x) = {limit(log(x), x, 0, '+')}")

# ---------------------------------------------------------------------------
# Example 4: Famous Limits
# ---------------------------------------------------------------------------

print("\n=== Famous Limits ===")

# sin(x)/x as x→0
print(f"lim(x→0) sin(x)/x = {limit(sin(x)/x, x, 0)}")

# (1-cos(x))/x² as x→0
print(f"lim(x→0) (1-cos(x))/x² = {limit((1 - cos(x))/x**2, x, 0)}")

# (eˣ - 1)/x as x→0
print(f"lim(x→0) (eˣ-1)/x = {limit((exp(x) - 1)/x, x, 0)}")

# tan(x)/x as x→0
print(f"lim(x→0) tan(x)/x = {limit(tan(x)/x, x, 0)}")

# x·sin(1/x) as x→0
print(f"lim(x→0) x·sin(1/x) = {limit(x * sin(1/x), x, 0)}")

# ---------------------------------------------------------------------------
# Example 5: L'Hôpital's Rule Cases (SymPy handles automatically)
# ---------------------------------------------------------------------------

print("\n=== Indeterminate Forms (handled automatically) ===")

# 0/0 form
print(f"lim(x→0) sin(x)/x = {limit(sin(x)/x, x, 0)}  [0/0]")

# ∞/∞ form
print(f"lim(x→∞) x²/eˣ = {limit(x**2/exp(x), x, oo)}  [∞/∞]")

# 0·∞ form
print(f"lim(x→0⁺) x·ln(x) = {limit(x * log(x), x, 0, '+')}  [0·∞]")

# 1^∞ form
print(f"lim(x→∞) (1+1/x)ˣ = {limit((1 + 1/x)**x, x, oo)}  [1^∞]")

# 0⁰ form
print(f"lim(x→0⁺) xˣ = {limit(x**x, x, 0, '+')}  [0⁰]")

# ∞⁰ form
print(f"lim(x→∞) x^(1/x) = {limit(x**(1/x), x, oo)}  [∞⁰]")

# ---------------------------------------------------------------------------
# Example 6: Squeeze Theorem Demonstration
# ---------------------------------------------------------------------------

print("\n=== Limit of Bounded Oscillation ===")
# -1 ≤ sin(1/x) ≤ 1, so -x² ≤ x²·sin(1/x) ≤ x²
print(f"lim(x→0) x²·sin(1/x) = {limit(x**2 * sin(1/x), x, 0)}")
print("  (Squeeze: -x² ≤ x²·sin(1/x) ≤ x², both bounds → 0)")
