"""
SymPy for Congruences and Modular Arithmetic
===============================================
Demonstrates modular arithmetic, Chinese Remainder Theorem,
modular inverse, Fermat's little theorem, and RSA basics.

Relevant domain: Number Theory > Congruences
"""

from sympy import (Mod, symbols, gcd, mod_inverse, isprime, factorint,
                   totient, Rational, Integer, nextprime)
from sympy.ntheory import primitive_root, is_primitive_root
from sympy.ntheory.modular import crt

# ---------------------------------------------------------------------------
# Example 1: Basic Modular Arithmetic
# ---------------------------------------------------------------------------

print("=== Basic Modular Arithmetic ===")
print(f"17 mod 5 = {17 % 5}")
print(f"25 mod 7 = {25 % 7}")
print(f"-3 mod 7 = {(-3) % 7}")  # Python gives positive result
print(f"(13 + 22) mod 10 = {(13 + 22) % 10}")
print(f"(13 * 22) mod 10 = {(13 * 22) % 10}")

# Power mod: a^b mod m
print(f"\n3^100 mod 7 = {pow(3, 100, 7)}")
print(f"2^10 mod 100 = {pow(2, 10, 100)}")

# ---------------------------------------------------------------------------
# Example 2: Modular Inverse
# a⁻¹ mod m  (exists iff gcd(a, m) = 1)
# ---------------------------------------------------------------------------

print("\n=== Modular Inverse ===")
pairs = [(3, 7), (5, 11), (7, 13), (4, 9), (17, 100)]
for a, m in pairs:
    if gcd(a, m) == 1:
        inv = mod_inverse(a, m)
        print(f"{a}⁻¹ mod {m} = {inv}  (verify: {a}×{inv} mod {m} = {(a * inv) % m})")
    else:
        print(f"{a}⁻¹ mod {m} does not exist (gcd = {gcd(a, m)})")

# ---------------------------------------------------------------------------
# Example 3: Chinese Remainder Theorem
# Solve system: x ≡ a₁ (mod m₁), x ≡ a₂ (mod m₂), ...
# ---------------------------------------------------------------------------

print("\n=== Chinese Remainder Theorem ===")

# x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
remainders = [2, 3, 2]
moduli = [3, 5, 7]
result, mod_product = crt(moduli, remainders)
print(f"x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)")
print(f"Solution: x ≡ {result} (mod {mod_product})")
# Verify
for r, m in zip(remainders, moduli):
    print(f"  {result} mod {m} = {result % m} (expected {r})")

# Another example
remainders2 = [1, 2, 3]
moduli2 = [5, 7, 11]
result2, mod2 = crt(moduli2, remainders2)
print(f"\nx ≡ 1 (mod 5), x ≡ 2 (mod 7), x ≡ 3 (mod 11)")
print(f"Solution: x ≡ {result2} (mod {mod2})")

# ---------------------------------------------------------------------------
# Example 4: Fermat's Little Theorem
# If p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p)
# ---------------------------------------------------------------------------

print("\n=== Fermat's Little Theorem ===")
p = 13
for a in range(2, 13):
    result = pow(a, p - 1, p)
    print(f"  {a}^{p-1} mod {p} = {result}")

# ---------------------------------------------------------------------------
# Example 5: Euler's Theorem
# If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)
# ---------------------------------------------------------------------------

print("\n=== Euler's Theorem ===")
n = 20
phi_n = totient(n)
print(f"n = {n}, φ({n}) = {phi_n}")
for a in [3, 7, 9, 11, 13, 17, 19]:
    if gcd(a, n) == 1:
        result = pow(a, int(phi_n), n)
        print(f"  {a}^{phi_n} mod {n} = {result}")

# ---------------------------------------------------------------------------
# Example 6: Primitive Roots
# ---------------------------------------------------------------------------

print("\n=== Primitive Roots ===")
for p in [5, 7, 11, 13, 17]:
    g = primitive_root(p)
    powers = [pow(g, k, p) for k in range(1, p)]
    print(f"Primitive root of {p}: {g}")
    print(f"  Powers: {powers}")

# ---------------------------------------------------------------------------
# Example 7: Linear Congruence  ax ≡ b (mod m)
# ---------------------------------------------------------------------------

print("\n=== Linear Congruences ===")

def solve_linear_congruence(a, b, m):
    """Solve ax ≡ b (mod m)."""
    g = gcd(a, m)
    if b % g != 0:
        return None
    a1, b1, m1 = a // g, b // g, m // g
    inv_a1 = mod_inverse(int(a1), int(m1))
    x0 = (inv_a1 * b1) % m1
    solutions = [(x0 + k * m1) % m for k in range(g)]
    return sorted(set(solutions))

cases = [(3, 6, 9), (5, 3, 7), (4, 2, 6), (7, 3, 11)]
for a, b, m in cases:
    sols = solve_linear_congruence(a, b, m)
    print(f"{a}x ≡ {b} (mod {m})  =>  x = {sols}")
