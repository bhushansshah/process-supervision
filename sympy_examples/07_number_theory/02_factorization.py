"""
SymPy for Factorization
========================
Demonstrates integer factorization, divisors, totient function,
and related number-theoretic functions.

Relevant domain: Number Theory > Factorization
"""

from sympy import (factorint, divisors, divisor_count, divisor_sigma,
                   totient, mobius, factorial, isprime, primefactors,
                   Mul, Pow, symbols, prod)

# ---------------------------------------------------------------------------
# Example 1: Prime Factorization
# ---------------------------------------------------------------------------

print("=== Prime Factorization ===")
numbers = [12, 60, 100, 360, 1001, 2310, 10080, 123456]
for n in numbers:
    factors = factorint(n)
    factor_str = " × ".join(f"{p}^{e}" if e > 1 else str(p)
                             for p, e in sorted(factors.items()))
    print(f"{n:>8} = {factor_str}")

# ---------------------------------------------------------------------------
# Example 2: Finding All Divisors
# ---------------------------------------------------------------------------

print("\n=== Divisors ===")
for n in [12, 28, 60, 100]:
    divs = divisors(n)
    print(f"Divisors of {n}: {divs}")
    print(f"  Count: {divisor_count(n)}")
    print(f"  Sum: {divisor_sigma(n, 1)}")

# ---------------------------------------------------------------------------
# Example 3: Perfect Numbers
# A number equals the sum of its proper divisors
# ---------------------------------------------------------------------------

print("\n=== Perfect Numbers (up to 10000) ===")
for n in range(2, 10001):
    if sum(divisors(n)[:-1]) == n:  # sum of proper divisors
        print(f"{n} is perfect: divisors = {divisors(n)[:-1]}, sum = {sum(divisors(n)[:-1])}")

# ---------------------------------------------------------------------------
# Example 4: Euler's Totient Function φ(n)
# Count of integers 1..n that are coprime to n
# ---------------------------------------------------------------------------

print("\n=== Euler's Totient Function φ(n) ===")
for n in range(1, 21):
    print(f"φ({n:>2}) = {totient(n)}")

# Property: For prime p, φ(p) = p - 1
print("\nVerify: for prime p, φ(p) = p-1")
for p in [2, 3, 5, 7, 11, 13]:
    print(f"  φ({p}) = {totient(p)} = {p} - 1 = {p - 1} ✓")

# Property: Sum of φ(d) for all d|n equals n
print("\nVerify: Σ φ(d) for d|n equals n")
for n in [12, 20, 30]:
    phi_sum = sum(totient(d) for d in divisors(n))
    print(f"  Σ φ(d) for d|{n} = {phi_sum} = {n} ✓")

# ---------------------------------------------------------------------------
# Example 5: Möbius Function μ(n)
# ---------------------------------------------------------------------------

print("\n=== Möbius Function μ(n) ===")
for n in range(1, 21):
    print(f"μ({n:>2}) = {str(mobius(n)):>2}  ({factorint(n) if n > 1 else 'unit'})")

# ---------------------------------------------------------------------------
# Example 6: Highly Composite Numbers
# Numbers with more divisors than any smaller positive integer
# ---------------------------------------------------------------------------

print("\n=== Highly Composite Numbers (up to 1000) ===")
max_divs = 0
for n in range(1, 1001):
    d = divisor_count(n)
    if d > max_divs:
        print(f"  {n}: {d} divisors, factorization = {factorint(n)}")
        max_divs = d

# ---------------------------------------------------------------------------
# Example 7: Fundamental Theorem of Arithmetic
# Verify unique factorization by reconstructing the number
# ---------------------------------------------------------------------------

print("\n=== Fundamental Theorem of Arithmetic ===")
for n in [360, 2520, 100100]:
    factors = factorint(n)
    reconstructed = 1
    for p, e in factors.items():
        reconstructed *= p**e
    print(f"{n} = {factors} → product = {reconstructed}, match = {reconstructed == n}")
