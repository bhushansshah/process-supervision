"""
SymPy for GCD and LCM
=======================
Demonstrates GCD, LCM, extended Euclidean algorithm,
Bézout's identity, and applications.

Relevant domain: Number Theory > GCD, LCM
"""

from sympy import gcd, lcm, igcd, ilcm, gcdex, symbols, Rational, factorint

# ---------------------------------------------------------------------------
# Example 1: GCD Computation
# ---------------------------------------------------------------------------

print("=== Greatest Common Divisor (GCD) ===")
pairs = [(12, 18), (48, 36), (100, 75), (252, 198), (1001, 77)]
for a, b in pairs:
    print(f"GCD({a}, {b}) = {gcd(a, b)}")

# GCD of multiple numbers
print(f"\nGCD(12, 18, 24) = {gcd(gcd(12, 18), 24)}")
print(f"GCD(120, 84, 60) = {gcd(gcd(120, 84), 60)}")

# ---------------------------------------------------------------------------
# Example 2: LCM Computation
# ---------------------------------------------------------------------------

print("\n=== Least Common Multiple (LCM) ===")
for a, b in pairs:
    print(f"LCM({a}, {b}) = {lcm(a, b)}")

# LCM of multiple numbers
print(f"\nLCM(4, 6, 10) = {lcm(lcm(4, 6), 10)}")
print(f"LCM(12, 15, 20) = {lcm(lcm(12, 15), 20)}")

# ---------------------------------------------------------------------------
# Example 3: Fundamental Identity: GCD × LCM = a × b
# ---------------------------------------------------------------------------

print("\n=== Identity: GCD(a,b) × LCM(a,b) = a × b ===")
for a, b in pairs:
    g = gcd(a, b)
    l = lcm(a, b)
    print(f"  GCD({a},{b})={g}, LCM({a},{b})={l}, "
          f"GCD×LCM={g*l}, a×b={a*b}, equal? {g*l == a*b}")

# ---------------------------------------------------------------------------
# Example 4: Extended Euclidean Algorithm (Bézout's Identity)
# GCD(a, b) = a*s + b*t
# ---------------------------------------------------------------------------

print("\n=== Extended Euclidean Algorithm (Bézout's Identity) ===")

for a, b in [(240, 46), (35, 15), (120, 23), (1001, 77)]:
    s, t, g = gcdex(a, b)
    print(f"GCD({a}, {b}) = {g}")
    print(f"  Bézout: {a}×({s}) + {b}×({t}) = {a*s + b*t}")

# ---------------------------------------------------------------------------
# Example 5: Coprime Testing
# ---------------------------------------------------------------------------

print("\n=== Coprime Testing ===")
pairs_coprime = [(15, 28), (12, 35), (9, 16), (14, 21), (8, 15)]
for a, b in pairs_coprime:
    print(f"  GCD({a}, {b}) = {gcd(a, b)} → coprime? {gcd(a, b) == 1}")

# ---------------------------------------------------------------------------
# Example 6: GCD Using Prime Factorization
# ---------------------------------------------------------------------------

print("\n=== GCD/LCM via Prime Factorization ===")

a, b = 360, 2520
fa = factorint(a)
fb = factorint(b)
print(f"{a} = {fa}")
print(f"{b} = {fb}")

# GCD: take min of each prime power
all_primes = set(fa.keys()) | set(fb.keys())
gcd_factors = {p: min(fa.get(p, 0), fb.get(p, 0)) for p in all_primes if min(fa.get(p, 0), fb.get(p, 0)) > 0}
lcm_factors = {p: max(fa.get(p, 0), fb.get(p, 0)) for p in all_primes}

gcd_val = 1
for p, e in gcd_factors.items():
    gcd_val *= p**e

lcm_val = 1
for p, e in lcm_factors.items():
    lcm_val *= p**e

print(f"GCD via factorization: {gcd_factors} = {gcd_val}")
print(f"LCM via factorization: {lcm_factors} = {lcm_val}")
print(f"Verify: GCD = {gcd(a, b)}, LCM = {lcm(a, b)}")

# ---------------------------------------------------------------------------
# Example 7: Symbolic GCD
# ---------------------------------------------------------------------------

print("\n=== Symbolic GCD ===")
from sympy import Poly

x = symbols('x')
p1 = x**3 - x
p2 = x**2 - 1

g = gcd(p1, p2)
print(f"GCD of {p1} and {p2} = {g}")

# ---------------------------------------------------------------------------
# Example 8: Application - Simplifying Fractions
# ---------------------------------------------------------------------------

print("\n=== Application: Simplifying Fractions ===")
fractions = [(24, 36), (105, 315), (48, 180), (1071, 462)]
for num, den in fractions:
    g = gcd(num, den)
    print(f"{num}/{den} = {num//g}/{den//g}  (divided by GCD={g})")
