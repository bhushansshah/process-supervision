"""
SymPy for Sequences and Series
================================
Demonstrates arithmetic/geometric sequences, summation formulas,
power series, and convergence testing.

Relevant domain: Algebra > Sequences and Series
"""

from sympy import (symbols, Sum, Product, oo, Rational, factorial,
                   simplify, series, summation, sequence, limit,
                   SeqFormula, SeqPer, fibonacci, lucas, binomial)

n, k, x = symbols('n k x')

# ---------------------------------------------------------------------------
# Example 1: Arithmetic Sequence
# ---------------------------------------------------------------------------

print("=== Arithmetic Sequence ===")
a1, d = 3, 5  # First term = 3, common difference = 5

# General term: a_n = a1 + (n-1)*d
a_n = a1 + (n - 1) * d
print(f"General term: a_n = {a_n}")

# First 10 terms
terms = [a_n.subs(n, i) for i in range(1, 11)]
print(f"First 10 terms: {terms}")

# Sum of first N terms
N = symbols('N', positive=True, integer=True)
arith_sum = summation(a1 + (k - 1) * d, (k, 1, N))
print(f"Sum of first N terms: S_N = {simplify(arith_sum)}")
print(f"Sum of first 10 terms: S_10 = {arith_sum.subs(N, 10)}")

# ---------------------------------------------------------------------------
# Example 2: Geometric Sequence
# ---------------------------------------------------------------------------

print("\n=== Geometric Sequence ===")
a1, r = 2, 3  # First term = 2, common ratio = 3

# General term: a_n = a1 * r^(n-1)
g_n = a1 * r ** (n - 1)
print(f"General term: a_n = {g_n}")

terms = [g_n.subs(n, i) for i in range(1, 9)]
print(f"First 8 terms: {terms}")

# Sum of first N terms
geo_sum = summation(a1 * r ** (k - 1), (k, 1, N))
print(f"Sum of first N terms: S_N = {simplify(geo_sum)}")

# Infinite geometric series (|r| < 1)
a1_inf, r_inf = 1, Rational(1, 2)
inf_sum = summation(a1_inf * r_inf ** (k - 1), (k, 1, oo))
print(f"\nInfinite series (a=1, r=1/2): S = {inf_sum}")

# ---------------------------------------------------------------------------
# Example 3: Famous Summation Formulas
# ---------------------------------------------------------------------------

print("\n=== Famous Summation Formulas ===")

# Sum of first n natural numbers
s1 = summation(k, (k, 1, n))
print(f"Σk (k=1..n) = {s1}")

# Sum of squares
s2 = summation(k**2, (k, 1, n))
print(f"Σk² (k=1..n) = {simplify(s2)}")

# Sum of cubes
s3 = summation(k**3, (k, 1, n))
print(f"Σk³ (k=1..n) = {simplify(s3)}")

# ---------------------------------------------------------------------------
# Example 4: Power Series / Taylor Series
# ---------------------------------------------------------------------------

print("\n=== Taylor Series Expansions ===")
from sympy import sin, cos, exp, ln, atan

# e^x around x=0, first 8 terms
print(f"e^x   = {series(exp(x), x, 0, 8)}")
print(f"sin(x) = {series(sin(x), x, 0, 8)}")
print(f"cos(x) = {series(cos(x), x, 0, 8)}")
print(f"ln(1+x) = {series(ln(1 + x), x, 0, 8)}")
print(f"1/(1-x) = {series(1/(1-x), x, 0, 8)}")

# ---------------------------------------------------------------------------
# Example 5: Fibonacci and Lucas Sequences
# ---------------------------------------------------------------------------

print("\n=== Fibonacci Sequence ===")
fibs = [fibonacci(i) for i in range(1, 16)]
print(f"First 15 Fibonacci numbers: {fibs}")

print("\n=== Lucas Sequence ===")
lucs = [lucas(i) for i in range(1, 16)]
print(f"First 15 Lucas numbers: {lucs}")

# ---------------------------------------------------------------------------
# Example 6: Products
# ---------------------------------------------------------------------------

print("\n=== Products ===")

# n! = product of 1..n
prod = Product(k, (k, 1, n))
print(f"Π(k, k=1..n) = {prod} = {prod.doit()}")

# Product formula for sine
print(f"5! = {Product(k, (k, 1, 5)).doit()}")
