"""
SymPy for Prealgebra: Integers, Fractions, and Decimals
=========================================================
Demonstrates SymPy's exact rational arithmetic, integer operations,
and conversion between fractions and decimals.

Relevant domain: Algebra > Prealgebra > Integers, Fractions, Decimals
"""

from sympy import Rational, Integer, gcd, lcm, factorint, isprime, nsimplify, S

# ---------------------------------------------------------------------------
# Example 1: Integer Operations
# ---------------------------------------------------------------------------

print("=== Integer Operations ===")
a, b = Integer(48), Integer(18)
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b (exact) = {a / b}")  # Returns Rational
print(f"a // b (floor div) = {a // b}")
print(f"a % b (mod) = {a % b}")
print(f"a ** 3 = {a ** 3}")
print(f"GCD(a, b) = {gcd(a, b)}")
print(f"LCM(a, b) = {lcm(a, b)}")

# ---------------------------------------------------------------------------
# Example 2: Fraction Arithmetic (Exact)
# ---------------------------------------------------------------------------

print("\n=== Fraction Arithmetic (Exact) ===")
f1 = Rational(3, 7)
f2 = Rational(2, 5)

print(f"3/7 + 2/5 = {f1 + f2}")
print(f"3/7 - 2/5 = {f1 - f2}")
print(f"3/7 * 2/5 = {f1 * f2}")
print(f"3/7 / 2/5 = {f1 / f2}")
print(f"(3/7)^2   = {f1 ** 2}")

# Simplification
f3 = Rational(24, 36)
print(f"\n24/36 simplified = {f3}")  # Auto-simplifies to 2/3

# Mixed numbers to improper fractions
whole = 3
num, den = 2, 5
improper = Rational(whole * den + num, den)
print(f"3 and 2/5 = {improper}")

# ---------------------------------------------------------------------------
# Example 3: Decimal to Fraction Conversion
# ---------------------------------------------------------------------------

print("\n=== Decimal ↔ Fraction Conversion ===")

# Decimal to fraction
print(f"0.75 as fraction = {Rational(0.75).limit_denominator(1000)}")
print(f"0.333... as fraction = {nsimplify(0.333333333333)}")
print(f"1.625 as fraction = {Rational(1625, 1000)}")

# Fraction to decimal
print(f"1/3 as decimal = {float(Rational(1, 3)):.10f}")
print(f"22/7 as decimal = {float(Rational(22, 7)):.10f}")

# ---------------------------------------------------------------------------
# Example 4: Ordering and Comparing Fractions
# ---------------------------------------------------------------------------

print("\n=== Comparing Fractions ===")
fracs = [Rational(3, 7), Rational(2, 5), Rational(1, 3), Rational(4, 9)]
sorted_fracs = sorted(fracs)
print(f"Fractions: {fracs}")
print(f"Sorted (ascending): {sorted_fracs}")
print(f"Largest: {max(fracs)}")
print(f"Smallest: {min(fracs)}")
print(f"3/7 > 2/5 ? {Rational(3, 7) > Rational(2, 5)}")

# ---------------------------------------------------------------------------
# Example 5: Absolute Value and Number Line
# ---------------------------------------------------------------------------

print("\n=== Absolute Value ===")
from sympy import Abs, sign

values = [Integer(-5), Rational(-3, 2), Integer(0), Rational(7, 4), Integer(3)]
for v in values:
    print(f"|{v}| = {Abs(v)},  sign({v}) = {sign(v)}")
