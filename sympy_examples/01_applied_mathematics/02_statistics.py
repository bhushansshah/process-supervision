"""
SymPy for Mathematical Statistics
==================================
Demonstrates SymPy's statistics module for working with random variables,
probability distributions, expectations, and variance.

Relevant domain: Applied Mathematics > Statistics > Mathematical Statistics
"""

from sympy.stats import (Normal, Uniform, Exponential, Binomial, Poisson,
                          E, variance, std, density, P, cdf)
from sympy import symbols, oo, sqrt, Rational, simplify, pprint

# ---------------------------------------------------------------------------
# Example 1: Normal Distribution
# ---------------------------------------------------------------------------

X = Normal('X', mean=0, std=1)  # Standard normal

print("=== Standard Normal Distribution ===")
print(f"E[X]   = {E(X)}")
print(f"Var[X] = {variance(X)}")
print(f"P(X > 0) = {P(X > 0)}")
print(f"P(-1 < X < 1) = {simplify(P((X > -1) & (X < 1)))}")

# ---------------------------------------------------------------------------
# Example 2: Binomial Distribution
# ---------------------------------------------------------------------------

n, p = 10, Rational(1, 2)
Y = Binomial('Y', n, p)

print("\n=== Binomial Distribution (n=10, p=0.5) ===")
print(f"E[Y]   = {E(Y)}")
print(f"Var[Y] = {variance(Y)}")
from sympy import Eq as Eq_
print(f"P(Y = 5) = {P(Eq_(Y, 5))}")
print(f"P(Y >= 8) = {P(Y >= 8)}")

# ---------------------------------------------------------------------------
# Example 3: Poisson Distribution
# ---------------------------------------------------------------------------

from sympy import Eq as Eq_sym
Z = Poisson('Z', 3)  # lambda = 3

print("\n=== Poisson Distribution (λ=3) ===")
print(f"E[Z]   = {E(Z)}")
print(f"Var[Z] = {variance(Z)}")
print(f"P(Z = 0) = {P(Eq_sym(Z, 0))}")
print(f"P(Z = 3) = {P(Eq_sym(Z, 3))}")

# ---------------------------------------------------------------------------
# Example 4: Uniform Distribution
# ---------------------------------------------------------------------------

a, b = 0, 10
U = Uniform('U', a, b)

print("\n=== Uniform Distribution [0, 10] ===")
print(f"E[U]   = {E(U)}")
print(f"Var[U] = {variance(U)}")
print(f"Std[U] = {simplify(std(U))}")

# ---------------------------------------------------------------------------
# Example 5: Exponential Distribution
# ---------------------------------------------------------------------------

rate = 2
W = Exponential('W', rate)

print("\n=== Exponential Distribution (rate=2) ===")
print(f"E[W]   = {E(W)}")
print(f"Var[W] = {variance(W)}")
print(f"P(W > 1) = {simplify(P(W > 1))}")

# ---------------------------------------------------------------------------
# Example 6: Symbolic Statistics
# ---------------------------------------------------------------------------

mu, sigma = symbols('mu sigma', positive=True)
X_sym = Normal('X_sym', mu, sigma)

print("\n=== Symbolic Normal Distribution N(μ, σ) ===")
print(f"E[X]   = {E(X_sym)}")
print(f"Var[X] = {variance(X_sym)}")
