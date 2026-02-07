"""
SymPy for Prime Numbers
========================
Demonstrates primality testing, prime generation, prime counting,
and prime-related functions.

Relevant domain: Number Theory > Prime Numbers
"""

from sympy import (isprime, prime, primerange, nextprime, prevprime,
                   primorial, primepi, factorint, Rational, sieve,
                   symbols, Sum, oo, N)

# ---------------------------------------------------------------------------
# Example 1: Primality Testing
# ---------------------------------------------------------------------------

print("=== Primality Testing ===")
test_numbers = [2, 7, 15, 97, 100, 997, 1009, 10007, 104729]
for n in test_numbers:
    print(f"  Is {n} prime? {isprime(n)}")

# ---------------------------------------------------------------------------
# Example 2: Generating Primes
# ---------------------------------------------------------------------------

print("\n=== Generating Primes ===")

# First 20 primes
first_20 = [prime(i) for i in range(1, 21)]
print(f"First 20 primes: {first_20}")

# Primes in a range
primes_50_100 = list(primerange(50, 100))
print(f"Primes between 50 and 100: {primes_50_100}")

# Next/Previous prime
print(f"\nNext prime after 100: {nextprime(100)}")
print(f"Previous prime before 100: {prevprime(100)}")
print(f"Next prime after 1000: {nextprime(1000)}")

# ---------------------------------------------------------------------------
# Example 3: Prime Counting Function π(n)
# ---------------------------------------------------------------------------

print("\n=== Prime Counting Function π(n) ===")
milestones = [10, 100, 1000, 10000, 100000]
for n in milestones:
    count = primepi(n)
    print(f"π({n:>6}) = {count}")

# ---------------------------------------------------------------------------
# Example 4: Primorial
# n# = product of all primes ≤ n
# ---------------------------------------------------------------------------

print("\n=== Primorial (n#) ===")
for n in [2, 3, 5, 7, 11, 13]:
    print(f"{n}# = {primorial(n)}")

# ---------------------------------------------------------------------------
# Example 5: Sieve of Eratosthenes
# ---------------------------------------------------------------------------

print("\n=== Sieve of Eratosthenes ===")
sieve.extend(100)
primes_to_100 = list(sieve.primerange(2, 100))
print(f"Primes up to 100: {primes_to_100}")
print(f"Count: {len(primes_to_100)}")

# ---------------------------------------------------------------------------
# Example 6: Twin Primes
# ---------------------------------------------------------------------------

print("\n=== Twin Primes (up to 200) ===")
twins = []
for p in primerange(2, 200):
    if isprime(p + 2):
        twins.append((p, p + 2))
print(f"Twin primes: {twins}")

# ---------------------------------------------------------------------------
# Example 7: Goldbach's Conjecture Verification
# "Every even number > 2 is the sum of two primes"
# ---------------------------------------------------------------------------

print("\n=== Goldbach Check (even numbers 4-50) ===")
for n in range(4, 52, 2):
    found = False
    for p in primerange(2, n):
        if isprime(n - p):
            print(f"{n} = {p} + {n - p}")
            found = True
            break
    if not found:
        print(f"{n}: NO DECOMPOSITION FOUND!")

# ---------------------------------------------------------------------------
# Example 8: Mersenne Primes
# Primes of the form 2^p - 1
# ---------------------------------------------------------------------------

print("\n=== Mersenne Primes (small) ===")
for p in primerange(2, 32):
    mp = 2**p - 1
    if isprime(mp):
        print(f"M_{p} = 2^{p} - 1 = {mp} is PRIME")
