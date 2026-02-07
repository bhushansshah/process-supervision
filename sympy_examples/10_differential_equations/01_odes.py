"""
SymPy for Ordinary Differential Equations (ODEs)
==================================================
Demonstrates solving first-order, second-order, and systems of ODEs,
plus initial value problems.

Relevant domain: Differential Equations > Ordinary Differential Equations (ODEs)
"""

from sympy import (symbols, Function, dsolve, Eq, exp, sin, cos, classify_ode,
                   Derivative, simplify, checkodesol, pprint, sqrt, pi)

x, t = symbols('x t')
y = Function('y')

# ---------------------------------------------------------------------------
# Example 1: First-Order Separable ODE
# dy/dx = x/y  =>  y dy = x dx
# ---------------------------------------------------------------------------

print("=== First-Order Separable ODE ===")
ode = Eq(y(x).diff(x), x / y(x))
print(f"ODE: y' = x/y")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 2: First-Order Linear ODE
# y' + 2y = e^(-x)
# ---------------------------------------------------------------------------

print("\n=== First-Order Linear ODE ===")
ode = Eq(y(x).diff(x) + 2*y(x), exp(-x))
print(f"ODE: y' + 2y = e^(-x)")
classification = classify_ode(ode, y(x))
print(f"Classification: {classification[:3]}...")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 3: Initial Value Problem (IVP)
# y' = -2y, y(0) = 3
# ---------------------------------------------------------------------------

print("\n=== Initial Value Problem ===")
ode = Eq(y(t).diff(t), -2*y(t))
sol = dsolve(ode, y(t), ics={y(0): 3})
print(f"ODE: y' = -2y, y(0) = 3")
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 4: Second-Order ODE (Constant Coefficients)
# y'' + 3y' + 2y = 0
# ---------------------------------------------------------------------------

print("\n=== Second-Order Homogeneous ODE ===")
ode = Eq(y(x).diff(x, 2) + 3*y(x).diff(x) + 2*y(x), 0)
print(f"ODE: y'' + 3y' + 2y = 0")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 5: Second-Order ODE with Non-Homogeneous Term
# y'' - y = sin(x)
# ---------------------------------------------------------------------------

print("\n=== Second-Order Non-Homogeneous ODE ===")
ode = Eq(y(x).diff(x, 2) - y(x), sin(x))
print(f"ODE: y'' - y = sin(x)")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 6: Harmonic Oscillator  y'' + ω²y = 0
# ---------------------------------------------------------------------------

print("\n=== Harmonic Oscillator ===")
omega = symbols('omega', positive=True)
ode = Eq(y(t).diff(t, 2) + omega**2 * y(t), 0)
print(f"ODE: y'' + ω²y = 0")
sol = dsolve(ode, y(t))
print(f"Solution: {sol}")

# With initial conditions: y(0) = 1, y'(0) = 0
sol_ivp = dsolve(ode, y(t), ics={y(0): 1, y(t).diff(t).subs(t, 0): 0})
print(f"With y(0)=1, y'(0)=0: {sol_ivp}")

# ---------------------------------------------------------------------------
# Example 7: Damped Oscillator  y'' + 2by' + ω²y = 0
# ---------------------------------------------------------------------------

print("\n=== Damped Oscillator ===")
b_coef = symbols('b', positive=True)
ode = Eq(y(t).diff(t, 2) + 2*b_coef*y(t).diff(t) + omega**2*y(t), 0)
print(f"ODE: y'' + 2by' + ω²y = 0")
sol = dsolve(ode, y(t))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 8: Exact ODE
# (2xy + 3) dx + (x² - 1) dy = 0
# ---------------------------------------------------------------------------

print("\n=== Exact ODE ===")
ode = Eq((2*x*y(x) + 3) + (x**2 - 1)*y(x).diff(x), 0)
print(f"ODE: (2xy + 3) + (x² - 1)y' = 0")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 9: Bernoulli Equation
# y' + y/x = y²
# ---------------------------------------------------------------------------

print("\n=== Bernoulli Equation ===")
ode = Eq(y(x).diff(x) + y(x)/x, y(x)**2)
print(f"ODE: y' + y/x = y²")
sol = dsolve(ode, y(x))
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 10: Verify Solution
# ---------------------------------------------------------------------------

print("\n=== Verify Solution ===")
ode = Eq(y(x).diff(x), y(x))
sol = dsolve(ode, y(x))
print(f"ODE: y' = y  =>  {sol}")
check = checkodesol(ode, sol)
print(f"Verification: {check}")
