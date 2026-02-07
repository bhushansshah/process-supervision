"""
SymPy for Exponential Functions
=================================
Demonstrates exponential expressions, equations, growth/decay models,
and symbolic manipulation of exponential functions.

Relevant domain: Algebra > Intermediate Algebra > Exponential Functions
"""

from sympy import (symbols, exp, E, log, ln, solve, Eq, simplify,
                   expand, Rational, oo, limit, N, powsimp)

x, t, k, r = symbols('x t k r')
a, b, c = symbols('a b c', positive=True)

# ---------------------------------------------------------------------------
# Example 1: Exponential Simplification
# ---------------------------------------------------------------------------

print("=== Exponential Simplification ===")

expr1 = exp(x) * exp(2*x)
print(f"e^x * e^(2x) = {powsimp(expr1)}")

expr2 = (exp(x))**3
print(f"(e^x)³ = {powsimp(expr2)}")

y_var = symbols('y')
expr3 = exp(x + y_var) / exp(y_var)
print(f"e^(x+y) / e^y = {simplify(expr3)}")

# ---------------------------------------------------------------------------
# Example 2: Solving Exponential Equations
# ---------------------------------------------------------------------------

print("\n=== Solving Exponential Equations ===")

# 2^x = 32
sol = solve(Eq(2**x, 32), x)
print(f"2^x = 32  =>  x = {sol}")

# e^(2x) = 7
sol = solve(Eq(exp(2*x), 7), x)
real_sols = [s for s in sol if s.is_real]
print(f"e^(2x) = 7  =>  x = {real_sols}")
print(f"  ≈ {[float(s) for s in real_sols]}")

# 3^(x+1) = 27^x
sol = solve(Eq(3**(x+1), 27**x), x)
print(f"3^(x+1) = 27^x  =>  x = {sol}")

# 5 * 2^x - 3 = 37
sol = solve(Eq(5 * 2**x - 3, 37), x)
print(f"5·2^x - 3 = 37  =>  x = {sol}")

# ---------------------------------------------------------------------------
# Example 3: Exponential Growth Model
# P(t) = P0 * e^(rt)
# ---------------------------------------------------------------------------

print("\n=== Exponential Growth Model ===")
P0, r_val = symbols('P0 r', positive=True)
P = P0 * exp(r_val * t)

print(f"Growth model: P(t) = {P}")

# Example: Population of 1000, growth rate 5%
P_specific = P.subs([(P0, 1000), (r_val, Rational(5, 100))])
print(f"\nP(t) with P0=1000, r=5%: P(t) = {P_specific}")
print(f"After 10 years: P(10) = {N(P_specific.subs(t, 10), 6)}")
print(f"After 20 years: P(20) = {N(P_specific.subs(t, 20), 6)}")

# Doubling time: P(t) = 2*P0
doubling_time = solve(Eq(P_specific, 2000), t)[0]
print(f"Doubling time: t = {doubling_time} ≈ {float(doubling_time):.2f} years")

# ---------------------------------------------------------------------------
# Example 4: Exponential Decay (Radioactive Decay / Half-Life)
# ---------------------------------------------------------------------------

print("\n=== Exponential Decay (Half-Life) ===")
# N(t) = N0 * e^(-kt)
N0, k_val = symbols('N0 k', positive=True)
Nt = N0 * exp(-k_val * t)

# Half-life: N(t_half) = N0/2
half_life = solve(Eq(Nt, N0 / 2), t)[0]
print(f"Half-life formula: t_½ = {half_life}")

# Carbon-14: half-life ≈ 5730 years
# Find decay constant
k_c14 = solve(Eq(half_life, 5730), k_val)[0]
print(f"Carbon-14 decay constant: k = {k_c14} ≈ {float(k_c14):.8f}")

# How old is a sample with 30% C-14 remaining?
age = solve(Eq(exp(-k_c14 * t), Rational(30, 100)), t)[0]
print(f"Age of sample with 30% C-14: t ≈ {float(age):.0f} years")

# ---------------------------------------------------------------------------
# Example 5: Compound Interest
# A = P(1 + r/n)^(nt)
# ---------------------------------------------------------------------------

print("\n=== Compound Interest ===")
P_val, n = symbols('P n', positive=True)
A = P_val * (1 + r / n) ** (n * t)

print(f"Compound interest formula: A = {A}")

# $1000 at 6% compounded monthly for 5 years
A_specific = A.subs([(P_val, 1000), (r, Rational(6, 100)), (n, 12), (t, 5)])
print(f"$1000 at 6% monthly for 5 years: A = ${float(A_specific):.2f}")

# Continuous compounding limit
A_continuous = limit(A, n, oo)
print(f"Continuous compounding: A = {A_continuous}")
A_cont_val = A_continuous.subs([(P_val, 1000), (r, Rational(6, 100)), (t, 5)])
print(f"$1000 at 6% continuous for 5 years: A = ${float(A_cont_val):.2f}")
