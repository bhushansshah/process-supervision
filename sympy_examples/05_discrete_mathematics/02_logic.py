"""
SymPy for Logic and Boolean Algebra
=====================================
Demonstrates propositional logic, truth tables, simplification,
and logical inference.

Relevant domain: Discrete Mathematics > Logic
"""

from sympy.logic.boolalg import (And, Or, Not, Implies, Equivalent, Xor,
                                   to_cnf, to_dnf, simplify_logic,
                                   truth_table, SOPform, POSform)
from sympy import symbols, satisfiable, Symbol

# ---------------------------------------------------------------------------
# Example 1: Basic Logical Operations
# ---------------------------------------------------------------------------

print("=== Basic Logical Operations ===")
p, q, r = symbols('p q r')

print(f"p AND q     = {And(p, q)}")
print(f"p OR q      = {Or(p, q)}")
print(f"NOT p       = {Not(p)}")
print(f"p → q       = {Implies(p, q)}")
print(f"p ↔ q       = {Equivalent(p, q)}")
print(f"p XOR q     = {Xor(p, q)}")

# ---------------------------------------------------------------------------
# Example 2: Truth Table Generation
# ---------------------------------------------------------------------------

print("\n=== Truth Tables ===")

expr = Implies(p, q)
print(f"Truth table for p → q:")
print(f"{'p':<8}{'q':<8}{'p → q':<8}")
print("-" * 24)
for p_val in [True, False]:
    for q_val in [True, False]:
        result = expr.subs([(p, p_val), (q, q_val)])
        print(f"{str(p_val):<8}{str(q_val):<8}{str(result):<8}")

# ---------------------------------------------------------------------------
# Example 3: Logical Simplification
# ---------------------------------------------------------------------------

print("\n=== Logical Simplification ===")

# De Morgan's laws
expr1 = Not(And(p, q))
print(f"¬(p ∧ q)   = {simplify_logic(expr1)}")

expr2 = Not(Or(p, q))
print(f"¬(p ∨ q)   = {simplify_logic(expr2)}")

# Complex expression
expr3 = And(Or(p, q), Or(p, Not(q)))
print(f"(p∨q) ∧ (p∨¬q) = {simplify_logic(expr3)}")

expr4 = Or(And(p, q), And(p, Not(q)))
print(f"(p∧q) ∨ (p∧¬q) = {simplify_logic(expr4)}")

# ---------------------------------------------------------------------------
# Example 4: Normal Forms (CNF and DNF)
# ---------------------------------------------------------------------------

print("\n=== Normal Forms ===")

expr = Implies(And(p, q), r)

cnf = to_cnf(expr)
dnf = to_dnf(expr)
print(f"Expression: (p ∧ q) → r")
print(f"CNF: {cnf}")
print(f"DNF: {dnf}")

# ---------------------------------------------------------------------------
# Example 5: Satisfiability
# ---------------------------------------------------------------------------

print("\n=== Satisfiability (SAT) ===")

# Is this expression satisfiable?
expr = And(Or(p, q), Or(Not(p), r), Or(Not(q), Not(r)))
result = satisfiable(expr)
print(f"Expression: {expr}")
print(f"Satisfiable? {result}")

# Tautology check: is the negation unsatisfiable?
taut = Or(p, Not(p))
is_taut = not satisfiable(Not(taut))
print(f"\n{taut} is a tautology? {is_taut}")

# Contradiction check
contra = And(p, Not(p))
is_contra = not satisfiable(contra)
print(f"{contra} is a contradiction? {is_contra}")

# ---------------------------------------------------------------------------
# Example 6: Sum of Products / Product of Sums
# ---------------------------------------------------------------------------

print("\n=== SOP and POS Forms ===")

# From truth table minterms
# f(p, q, r) = 1 when (p,q,r) is (0,0,1), (0,1,0), (1,0,1), (1,1,1)
minterms = [[0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 1]]
sop = SOPform([p, q, r], minterms)
print(f"SOP from minterms: {sop}")

# From maxterms
dontcares = [[1, 0, 0]]
pos = POSform([p, q, r], minterms, dontcares)
print(f"POS from minterms (with don't cares): {pos}")

# ---------------------------------------------------------------------------
# Example 7: Logical Equivalence Check
# ---------------------------------------------------------------------------

print("\n=== Logical Equivalence ===")

# p → q  ≡  ¬p ∨ q
e1 = Implies(p, q)
e2 = Or(Not(p), q)
equiv = Equivalent(e1, e2)
# Check by SAT: if e1 ↔ e2 is a tautology
is_equiv = not satisfiable(Not(equiv))
print(f"(p → q) ≡ (¬p ∨ q)? {is_equiv}")

# Contrapositive: (p → q) ≡ (¬q → ¬p)
e3 = Implies(Not(q), Not(p))
is_contra = not satisfiable(Not(Equivalent(e1, e3)))
print(f"(p → q) ≡ (¬q → ¬p)? {is_contra} (contrapositive)")
