"""
SymPy for Permutations and Combinations
=========================================
Demonstrates counting methods including permutations, combinations,
factorials, and the Binomial coefficient.

Relevant domain: Applied Mathematics > Probability > Counting Methods
"""

from sympy import factorial, binomial, symbols, Product, Sum, Function
from sympy.functions.combinatorial.numbers import nC, nP, nT

# ---------------------------------------------------------------------------
# Example 1: Factorials
# ---------------------------------------------------------------------------

print("=== Factorials ===")
for n in range(1, 11):
    print(f"{n}! = {factorial(n)}")

# Symbolic factorial
n = symbols('n', positive=True, integer=True)
print(f"\nn! / (n-2)! simplified = {(factorial(n) / factorial(n - 2)).simplify()}")

# ---------------------------------------------------------------------------
# Example 2: Permutations  P(n, r) = n! / (n-r)!
# ---------------------------------------------------------------------------

print("\n=== Permutations P(n, r) ===")
# How many ways to arrange 3 items from 10?
print(f"P(10, 3) = {nP(10, 3)}")
print(f"P(5, 5)  = {nP(5, 5)}")  # All items
print(f"P(8, 2)  = {nP(8, 2)}")

# Manual computation
n_val, r_val = 10, 3
manual_perm = factorial(n_val) / factorial(n_val - r_val)
print(f"P(10, 3) manual = {manual_perm}")

# ---------------------------------------------------------------------------
# Example 3: Combinations  C(n, r) = n! / (r! * (n-r)!)
# ---------------------------------------------------------------------------

print("\n=== Combinations C(n, r) ===")
# How many ways to choose 3 items from 10?
print(f"C(10, 3) = {binomial(10, 3)}")
print(f"C(52, 5) = {binomial(52, 5)}")   # Poker hands
print(f"C(20, 10) = {binomial(20, 10)}")

# Symbolic binomial coefficient
n, k = symbols('n k', positive=True, integer=True)
print(f"\nC(n, k) = {binomial(n, k)}")
print(f"C(n, 0) = {binomial(n, 0)}")
print(f"C(n, 1) = {binomial(n, 1)}")
print(f"C(n, n) = {binomial(n, n)}")

# ---------------------------------------------------------------------------
# Example 4: Binomial Theorem
# ---------------------------------------------------------------------------

from sympy import expand, Symbol

x, y = symbols('x y')

print("\n=== Binomial Theorem ===")
for power in range(2, 6):
    expansion = expand((x + y) ** power)
    print(f"(x + y)^{power} = {expansion}")

# ---------------------------------------------------------------------------
# Example 5: Pascal's Triangle Row
# ---------------------------------------------------------------------------

print("\n=== Pascal's Triangle (first 8 rows) ===")
for row in range(8):
    coeffs = [binomial(row, col) for col in range(row + 1)]
    print(f"Row {row}: {coeffs}")

# ---------------------------------------------------------------------------
# Example 6: Counting Problems
# ---------------------------------------------------------------------------

print("\n=== Counting Problems ===")

# How many 4-letter words (with repetition) from 26 letters?
print(f"4-letter words with repetition: {26**4}")

# How many 4-letter words (without repetition) from 26 letters?
print(f"4-letter words without repetition: {nP(26, 4)}")

# Committee selection: Choose a president, VP, and secretary from 10 people
print(f"Ordered selection of 3 from 10: {nP(10, 3)}")

# Committee selection: Choose 3 members from 10 (unordered)
print(f"Unordered selection of 3 from 10: {binomial(10, 3)}")

# Stars and bars: distribute 10 identical balls into 4 distinct boxes
# C(10 + 4 - 1, 4 - 1)
print(f"Stars & bars (10 balls, 4 boxes): {binomial(10 + 4 - 1, 4 - 1)}")

# Multinomial: arrange letters in "MISSISSIPPI"
from sympy import Mul
letters = "MISSISSIPPI"
n_total = len(letters)
freq = {ch: letters.count(ch) for ch in set(letters)}
denom = Mul(*[factorial(v) for v in freq.values()])
arrangements = factorial(n_total) / denom
print(f"Arrangements of '{letters}': {arrangements}")
print(f"  Letter frequencies: {freq}")
