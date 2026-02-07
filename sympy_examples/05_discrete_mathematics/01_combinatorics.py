"""
SymPy for Combinatorics
========================
Demonstrates combinatorial functions: partitions, Bell numbers,
Catalan numbers, Stirling numbers, and generating functions.

Relevant domain: Discrete Mathematics > Combinatorics
"""

from sympy import (binomial, factorial, symbols, Sum, oo, Function,
                   bell, catalan, bernoulli, fibonacci, harmonic,
                   Rational, simplify, npartitions)
from sympy.functions.combinatorial.numbers import stirling

n, k, x = symbols('n k x')

# ---------------------------------------------------------------------------
# Example 1: Basic Counting
# ---------------------------------------------------------------------------

print("=== Basic Counting ===")
print(f"C(10, 3) = {binomial(10, 3)}")
print(f"C(52, 5) = {binomial(52, 5)} (poker hands)")
print(f"10! = {factorial(10)}")
print(f"P(10, 3) = 10!/(10-3)! = {factorial(10) // factorial(7)}")

# ---------------------------------------------------------------------------
# Example 2: Integer Partitions
# "In how many ways can n be written as sum of positive integers?"
# ---------------------------------------------------------------------------

print("\n=== Integer Partitions ===")
for n_val in range(1, 16):
    print(f"p({n_val}) = {npartitions(n_val)}")

# ---------------------------------------------------------------------------
# Example 3: Bell Numbers
# "Number of ways to partition a set of n elements"
# ---------------------------------------------------------------------------

print("\n=== Bell Numbers (set partitions) ===")
for n_val in range(0, 11):
    print(f"B({n_val}) = {bell(n_val)}")

# ---------------------------------------------------------------------------
# Example 4: Catalan Numbers
# "Count of valid parenthesizations, binary trees, etc."
# ---------------------------------------------------------------------------

print("\n=== Catalan Numbers ===")
for n_val in range(0, 11):
    print(f"C({n_val}) = {catalan(n_val)}")

print("\nCatalan numbers count:")
print("  - Valid parenthesizations of n pairs")
print("  - Number of full binary trees with n+1 leaves")
print("  - Number of paths in a grid that don't cross diagonal")

# ---------------------------------------------------------------------------
# Example 5: Stirling Numbers
# ---------------------------------------------------------------------------

print("\n=== Stirling Numbers of the Second Kind ===")
print("S(n, k) = number of ways to partition n elements into k non-empty subsets")
for n_val in range(1, 7):
    row = [stirling(n_val, k_val, kind=2) for k_val in range(1, n_val + 1)]
    print(f"n={n_val}: {row}")

# ---------------------------------------------------------------------------
# Example 6: Bernoulli Numbers
# ---------------------------------------------------------------------------

print("\n=== Bernoulli Numbers ===")
for n_val in range(0, 11):
    print(f"B({n_val}) = {bernoulli(n_val)}")

# ---------------------------------------------------------------------------
# Example 7: Harmonic Numbers
# ---------------------------------------------------------------------------

print("\n=== Harmonic Numbers ===")
for n_val in range(1, 11):
    print(f"H({n_val}) = {harmonic(n_val)} ≈ {float(harmonic(n_val)):.6f}")

# ---------------------------------------------------------------------------
# Example 8: Derangements (Subfactorial)
# "Number of permutations with no fixed points"
# ---------------------------------------------------------------------------

print("\n=== Derangements (Subfactorial) ===")
from sympy import subfactorial

for n_val in range(0, 11):
    print(f"D({n_val}) = !{n_val} = {subfactorial(n_val)}")
