"""
SymPy for Partial Differential Equations (PDEs)
=================================================
Demonstrates solving basic PDEs using SymPy's pdsolve and
verification of solutions.

Relevant domain: Differential Equations > Partial Differential Equations (PDEs)
"""

from sympy import (symbols, Function, Eq, exp, sin, cos, pi,
                   pdsolve, classify_pde, checkpdesol,
                   diff, simplify, pprint, sqrt)

x, y, t = symbols('x y t')
u = Function('u')

# ---------------------------------------------------------------------------
# Example 1: First-Order PDE
# ∂u/∂x + ∂u/∂y = 0  (Transport equation)
# ---------------------------------------------------------------------------

print("=== First-Order PDE: uₓ + uᵧ = 0 ===")
pde = Eq(u(x, y).diff(x) + u(x, y).diff(y), 0)
print(f"PDE: ∂u/∂x + ∂u/∂y = 0")

classification = classify_pde(pde)
print(f"Classification: {classification}")

sol = pdsolve(pde)
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 2: First-Order PDE with Coefficients
# x·∂u/∂x + y·∂u/∂y = 0
# ---------------------------------------------------------------------------

print("\n=== First-Order PDE: x·uₓ + y·uᵧ = 0 ===")
pde = Eq(x * u(x, y).diff(x) + y * u(x, y).diff(y), 0)
sol = pdsolve(pde)
print(f"PDE: x·∂u/∂x + y·∂u/∂y = 0")
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 3: First-Order PDE
# ∂u/∂x + x·∂u/∂y = 0
# ---------------------------------------------------------------------------

print("\n=== First-Order PDE: uₓ + x·uᵧ = 0 ===")
pde = Eq(u(x, y).diff(x) + x * u(x, y).diff(y), 0)
sol = pdsolve(pde)
print(f"Solution: {sol}")

# ---------------------------------------------------------------------------
# Example 4: Verify PDE Solutions Manually
# Heat equation: ∂u/∂t = k·∂²u/∂x²
# Check that u = e^(-k·n²·π²·t)·sin(nπx) is a solution
# ---------------------------------------------------------------------------

print("\n=== Verify Heat Equation Solution ===")
k, n = symbols('k n', positive=True)

# Proposed solution
u_sol = exp(-k * n**2 * pi**2 * t) * sin(n * pi * x)
print(f"Proposed solution: u(x,t) = {u_sol}")

# Check: ∂u/∂t = k·∂²u/∂x²
lhs = diff(u_sol, t)
rhs = k * diff(u_sol, x, 2)
residual = simplify(lhs - rhs)
print(f"∂u/∂t = {lhs}")
print(f"k·∂²u/∂x² = {rhs}")
print(f"Residual = {residual}")
print(f"Is solution valid? {residual == 0}")

# ---------------------------------------------------------------------------
# Example 5: Verify Wave Equation Solution
# ∂²u/∂t² = c²·∂²u/∂x²
# Check u = f(x - ct) + g(x + ct) (d'Alembert's solution)
# ---------------------------------------------------------------------------

print("\n=== Verify Wave Equation Solution ===")
c = symbols('c', positive=True)
f = Function('f')
g = Function('g')

u_wave = f(x - c*t) + g(x + c*t)
print(f"d'Alembert solution: u = f(x-ct) + g(x+ct)")

utt = diff(u_wave, t, 2)
uxx = diff(u_wave, x, 2)
residual = simplify(utt - c**2 * uxx)
print(f"∂²u/∂t² = {utt}")
print(f"c²·∂²u/∂x² = {c**2 * uxx}")
print(f"Residual = {residual}")
print(f"Is solution valid? {residual == 0}")

# ---------------------------------------------------------------------------
# Example 6: Verify Laplace Equation Solution
# ∂²u/∂x² + ∂²u/∂y² = 0
# Check that u = e^(nx)·sin(ny) is a harmonic function
# ---------------------------------------------------------------------------

print("\n=== Verify Laplace Equation Solution ===")

u_lap = exp(n*x) * sin(n*y)
print(f"Proposed solution: u = {u_lap}")

uxx = diff(u_lap, x, 2)
uyy = diff(u_lap, y, 2)
laplacian = simplify(uxx + uyy)
print(f"∂²u/∂x² + ∂²u/∂y² = {laplacian}")
print(f"Is harmonic? {laplacian == 0}")

# Another harmonic function: u = ln(x² + y²)
u_log = (x**2 + y**2)
u_ln = symbols('dummy')  # Use a concrete example
u_harm = x**2 - y**2  # Real part of z²
uxx2 = diff(u_harm, x, 2)
uyy2 = diff(u_harm, y, 2)
print(f"\nu = x² - y² (real part of z²)")
print(f"∂²u/∂x² + ∂²u/∂y² = {uxx2 + uyy2}")
print(f"Is harmonic? {uxx2 + uyy2 == 0}")
