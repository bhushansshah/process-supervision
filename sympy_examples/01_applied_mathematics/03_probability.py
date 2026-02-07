"""
SymPy for Probability
======================
Demonstrates probability computations including conditional probability,
Bayes' theorem, and probability distributions.

Relevant domain: Applied Mathematics > Statistics > Probability
"""

from sympy.stats import (Die, Coin, P, E, variance, density,
                          Normal, Bernoulli, given)
from sympy import Eq, Rational, symbols, simplify

# ---------------------------------------------------------------------------
# Example 1: Dice Probability
# ---------------------------------------------------------------------------

D1 = Die('D1', 6)
D2 = Die('D2', 6)

print("=== Dice Probability ===")
print(f"P(D1 = 4)       = {P(Eq(D1, 4))}")
print(f"P(D1 + D2 = 7)  = {P(Eq(D1 + D2, 7))}")
print(f"P(D1 + D2 >= 10) = {P(D1 + D2 >= 10)}")
print(f"E[D1 + D2]      = {E(D1 + D2)}")

# ---------------------------------------------------------------------------
# Example 2: Coin Flip Probability
# ---------------------------------------------------------------------------

# Using Bernoulli instead of Coin (more compatible across versions)
from sympy.stats import Bernoulli as BernoulliRV

fair_coin = BernoulliRV('fair_coin', Rational(1, 2))

print("\n=== Coin Probability ===")
print(f"P(Fair Coin = Heads) = {P(Eq(fair_coin, 1))}")

# Biased coin
biased_coin = BernoulliRV('biased_coin', Rational(3, 4))
print(f"P(Biased Coin = Heads) = {P(Eq(biased_coin, 1))}")

# ---------------------------------------------------------------------------
# Example 3: Conditional Probability
# ---------------------------------------------------------------------------

D = Die('D', 6)

# P(D >= 4 | D >= 2)
cond_prob = P(D >= 4, D >= 2)
print("\n=== Conditional Probability ===")
print(f"P(D >= 4 | D >= 2) = {cond_prob}")

# ---------------------------------------------------------------------------
# Example 4: Bernoulli Trials
# ---------------------------------------------------------------------------

p = Rational(1, 3)
B = Bernoulli('B', p)

print("\n=== Bernoulli Trial (p=1/3) ===")
print(f"E[B]   = {E(B)}")
print(f"Var[B] = {variance(B)}")
print(f"P(B=1) = {density(B).dict[1]}")
print(f"P(B=0) = {density(B).dict[0]}")

# ---------------------------------------------------------------------------
# Example 5: Bayes' Theorem (manual symbolic computation)
# "1% of population has a disease. A test has 99% sensitivity and 95% specificity.
#  If a person tests positive, what's the probability they have the disease?"
# ---------------------------------------------------------------------------

P_disease = Rational(1, 100)
P_no_disease = 1 - P_disease
sensitivity = Rational(99, 100)     # P(positive | disease)
specificity = Rational(95, 100)     # P(negative | no disease)
false_positive = 1 - specificity    # P(positive | no disease)

# Bayes' theorem
P_positive = sensitivity * P_disease + false_positive * P_no_disease
P_disease_given_positive = (sensitivity * P_disease) / P_positive

print("\n=== Bayes' Theorem: Medical Test ===")
print(f"P(Disease | Positive) = {P_disease_given_positive} ≈ {float(P_disease_given_positive):.4f}")
print("Note: Despite a 99% sensitive test, only ~16.8% chance of disease!")

# ---------------------------------------------------------------------------
# Example 6: Expected Value of a Game
# "Roll a die. Win $10 if 6, win $5 if 4 or 5, lose $3 otherwise."
# ---------------------------------------------------------------------------

D = Die('D', 6)

# Define payout function
from sympy import Piecewise

x = symbols('x')
# We compute manually using density
d = density(D).dict
expected_payout = (10 * d[6] + 5 * d[4] + 5 * d[5] + (-3) * d[1] +
                   (-3) * d[2] + (-3) * d[3])

print("\n=== Expected Value of a Game ===")
print(f"Expected payout = {expected_payout} = ${float(expected_payout):.2f}")
