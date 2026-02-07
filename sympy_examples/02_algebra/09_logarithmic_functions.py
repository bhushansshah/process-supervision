"""
SymPy for Logarithmic Functions
=================================
Demonstrates logarithm properties, equations, change of base,
and applications.

Relevant domain: Algebra > Intermediate Algebra > Logarithmic Functions
"""

from sympy import (symbols, log, ln, exp, solve, Eq, simplify,
                   expand_log, logcombine, Rational, N, E, oo)

x, y, a, b = symbols('x y a b', positive=True)

# ---------------------------------------------------------------------------
# Example 1: Logarithm Basics
# ---------------------------------------------------------------------------

print("=== Logarithm Basics ===")
# SymPy's log(x) is natural log; log(x, base) for other bases
print(f"ln(1)     = {ln(1)}")
print(f"ln(e)     = {ln(E)}")
print(f"ln(e²)    = {ln(E**2)}")
print(f"log₂(8)   = {log(8, 2)}")
print(f"log₁₀(100)= {log(100, 10)}")
print(f"log₃(81)  = {log(81, 3)}")
print(f"log₅(125) = {log(125, 5)}")

# ---------------------------------------------------------------------------
# Example 2: Logarithm Properties
# ---------------------------------------------------------------------------

print("\n=== Logarithm Properties ===")

# Product rule: log(ab) = log(a) + log(b)
expr = ln(a * b)
print(f"ln(a·b) expanded = {expand_log(expr, force=True)}")

# Quotient rule: log(a/b) = log(a) - log(b)
expr = ln(a / b)
print(f"ln(a/b) expanded = {expand_log(expr, force=True)}")

# Power rule: log(a^n) = n*log(a)
n = symbols('n')
expr = ln(a**n)
print(f"ln(a^n) expanded = {expand_log(expr, force=True)}")

# Combining logs
expr = ln(x) + ln(y)
print(f"ln(x) + ln(y) combined = {logcombine(expr, force=True)}")

expr = 2*ln(x) - 3*ln(y)
print(f"2ln(x) - 3ln(y) combined = {logcombine(expr, force=True)}")

# ---------------------------------------------------------------------------
# Example 3: Change of Base Formula
# ---------------------------------------------------------------------------

print("\n=== Change of Base ===")
# log_b(x) = ln(x) / ln(b)
base = symbols('base', positive=True)
print(f"log_b(x) = ln(x)/ln(b) = {log(x, base)}")

# Numeric example
print(f"log₇(50) = ln(50)/ln(7) = {N(log(50, 7), 6)}")
print(f"log₂(100) = {N(log(100, 2), 6)}")

# ---------------------------------------------------------------------------
# Example 4: Solving Logarithmic Equations
# ---------------------------------------------------------------------------

print("\n=== Solving Logarithmic Equations ===")

x = symbols('x', positive=True)

# ln(x) = 5
sol = solve(Eq(ln(x), 5), x)
print(f"ln(x) = 5  =>  x = {sol}")

# log₂(x) = 6
sol = solve(Eq(log(x, 2), 6), x)
print(f"log₂(x) = 6  =>  x = {sol}")

# ln(x) + ln(x-2) = ln(3)
sol = solve(Eq(ln(x) + ln(x - 2), ln(3)), x)
print(f"ln(x) + ln(x-2) = ln(3)  =>  x = {sol}")

# 2^x = 10  (solving using logs)
x = symbols('x')
sol = solve(Eq(2**x, 10), x)
print(f"2^x = 10  =>  x = {sol[0]} ≈ {float(sol[0]):.4f}")

# ---------------------------------------------------------------------------
# Example 5: Logarithmic Scale Application (pH)
# pH = -log₁₀([H⁺])
# ---------------------------------------------------------------------------

print("\n=== Application: pH Calculation ===")
H_conc = symbols('H', positive=True)
pH = -log(H_conc, 10)

concentrations = [Rational(1, 10**i) for i in range(1, 8)]
for c in concentrations:
    print(f"[H⁺] = {float(c):.0e}  =>  pH = {pH.subs(H_conc, c)}")

# ---------------------------------------------------------------------------
# Example 6: Natural Logarithm and Integration Connection
# ---------------------------------------------------------------------------

print("\n=== ln(x) Properties ===")
x = symbols('x', positive=True)
from sympy import diff, integrate

print(f"d/dx [ln(x)] = {diff(ln(x), x)}")
print(f"∫ 1/x dx = {integrate(1/x, x)}")
print(f"ln(x) as x→0⁺ = {ln(x).limit(x, 0, '+')}")
print(f"ln(x) as x→∞ = {ln(x).limit(x, oo)}")
