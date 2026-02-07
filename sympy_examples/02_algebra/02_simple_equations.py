"""
SymPy for Simple Equations (Prealgebra)
========================================
Demonstrates solving basic linear equations, proportions, and simple
variable isolation — the building blocks of algebra.

Relevant domain: Algebra > Prealgebra > Simple Equations
"""

from sympy import symbols, Eq, solve, Rational, simplify

x, y, z = symbols('x y z')

# ---------------------------------------------------------------------------
# Example 1: One-Step Equations
# ---------------------------------------------------------------------------

print("=== One-Step Equations ===")

# x + 7 = 15
sol = solve(Eq(x + 7, 15), x)
print(f"x + 7 = 15  =>  x = {sol[0]}")

# 3x = 21
sol = solve(Eq(3 * x, 21), x)
print(f"3x = 21     =>  x = {sol[0]}")

# x/4 = 9
sol = solve(Eq(x / 4, 9), x)
print(f"x/4 = 9     =>  x = {sol[0]}")

# ---------------------------------------------------------------------------
# Example 2: Two-Step Equations
# ---------------------------------------------------------------------------

print("\n=== Two-Step Equations ===")

# 2x + 5 = 17
sol = solve(Eq(2 * x + 5, 17), x)
print(f"2x + 5 = 17     =>  x = {sol[0]}")

# (x - 3) / 2 = 7
sol = solve(Eq((x - 3) / 2, 7), x)
print(f"(x-3)/2 = 7     =>  x = {sol[0]}")

# 4(x + 1) = 20
sol = solve(Eq(4 * (x + 1), 20), x)
print(f"4(x + 1) = 20   =>  x = {sol[0]}")

# ---------------------------------------------------------------------------
# Example 3: Multi-Step Equations
# ---------------------------------------------------------------------------

print("\n=== Multi-Step Equations ===")

# 3x + 2 = 5x - 8
sol = solve(Eq(3 * x + 2, 5 * x - 8), x)
print(f"3x + 2 = 5x - 8      =>  x = {sol[0]}")

# 2(x - 1) + 3 = x + 7
sol = solve(Eq(2 * (x - 1) + 3, x + 7), x)
print(f"2(x-1) + 3 = x + 7   =>  x = {sol[0]}")

# ---------------------------------------------------------------------------
# Example 4: Proportions
# ---------------------------------------------------------------------------

print("\n=== Proportions ===")

# x/3 = 8/12
sol = solve(Eq(x / 3, Rational(8, 12)), x)
print(f"x/3 = 8/12  =>  x = {sol[0]}")

# 5/x = 15/9
sol = solve(Eq(5 / x, Rational(15, 9)), x)
print(f"5/x = 15/9  =>  x = {sol[0]}")

# ---------------------------------------------------------------------------
# Example 5: System of Simple Linear Equations
# ---------------------------------------------------------------------------

print("\n=== System of Linear Equations ===")

# x + y = 10
# x - y = 4
solution = solve([Eq(x + y, 10), Eq(x - y, 4)], [x, y])
print(f"x + y = 10, x - y = 4  =>  x = {solution[x]}, y = {solution[y]}")

# 2x + 3y = 13
# x + y = 5
solution = solve([Eq(2*x + 3*y, 13), Eq(x + y, 5)], [x, y])
print(f"2x + 3y = 13, x + y = 5  =>  x = {solution[x]}, y = {solution[y]}")

# 3 variables
solution = solve([
    Eq(x + y + z, 6),
    Eq(2*x - y + z, 3),
    Eq(x + 2*y - z, 3)
], [x, y, z])
print(f"3-variable system  =>  x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")
