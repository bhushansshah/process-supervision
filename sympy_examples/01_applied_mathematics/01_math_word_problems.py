"""
SymPy for Math Word Problems
=============================
Demonstrates how SymPy can translate word problems into symbolic equations
and solve them automatically.

Relevant domain: Applied Mathematics > Math Word Problems
"""

from sympy import symbols, Eq, solve, Rational

# ---------------------------------------------------------------------------
# Example 1: Age Word Problem
# "John is twice as old as Mary. In 5 years, the sum of their ages will be 40.
#  How old are they now?"
# ---------------------------------------------------------------------------

john, mary = symbols('john mary')

eq1 = Eq(john, 2 * mary)              # John is twice Mary's age
eq2 = Eq((john + 5) + (mary + 5), 40) # In 5 years their ages sum to 40

solution = solve([eq1, eq2], [john, mary])
print("=== Age Word Problem ===")
print(f"John's age: {solution[john]}")
print(f"Mary's age: {solution[mary]}")

# ---------------------------------------------------------------------------
# Example 2: Distance-Rate-Time Problem
# "A car travels at 60 mph for some time, then at 40 mph for 2 hours longer.
#  Total distance is 280 miles. How long did it travel at 60 mph?"
# ---------------------------------------------------------------------------

t = symbols('t', positive=True)

distance_eq = Eq(60 * t + 40 * (t + 2), 280)
time_solution = solve(distance_eq, t)
print("\n=== Distance-Rate-Time Problem ===")
print(f"Time at 60 mph: {time_solution[0]} hours")
print(f"Time at 40 mph: {time_solution[0] + 2} hours")
print(f"Total distance: {60 * time_solution[0] + 40 * (time_solution[0] + 2)}")

# ---------------------------------------------------------------------------
# Example 3: Mixture Problem
# "How many liters of 30% acid solution must be mixed with 10 liters of 50%
#  acid solution to get a 35% acid solution?"
# ---------------------------------------------------------------------------

x = symbols('x', positive=True)

# 0.30*x + 0.50*10 = 0.35*(x + 10)
mixture_eq = Eq(Rational(30, 100) * x + Rational(50, 100) * 10,
                Rational(35, 100) * (x + 10))
liters = solve(mixture_eq, x)
print("\n=== Mixture Problem ===")
print(f"Liters of 30% solution needed: {liters[0]}")

# ---------------------------------------------------------------------------
# Example 4: Work Rate Problem
# "Alice can paint a room in 5 hours. Bob can paint it in 3 hours.
#  How long does it take them working together?"
# ---------------------------------------------------------------------------

t = symbols('t', positive=True)

work_eq = Eq(t / 5 + t / 3, 1)  # combined work = 1 room
together_time = solve(work_eq, t)
print("\n=== Work Rate Problem ===")
print(f"Time working together: {together_time[0]} hours = {float(together_time[0]):.2f} hours")

# ---------------------------------------------------------------------------
# Example 5: Profit/Revenue Problem
# "A company sells x units at price (50 - 0.5x) each. Cost is 10x + 200.
#  Find the number of units that maximizes profit."
# ---------------------------------------------------------------------------

from sympy import diff

x = symbols('x')
revenue = x * (50 - Rational(1, 2) * x)
cost = 10 * x + 200
profit = revenue - cost

# Maximize profit: set derivative to zero
critical = solve(diff(profit, x), x)
max_profit = profit.subs(x, critical[0])
print("\n=== Profit Maximization ===")
print(f"Units for max profit: {critical[0]}")
print(f"Maximum profit: {max_profit}")
