"""
SymPy for Quadratic Functions
===============================
Demonstrates analysis of quadratic functions: vertex, axis of symmetry,
discriminant, roots, and transformations.

Relevant domain: Algebra > Intermediate Algebra > Quadratic Functions
"""

from sympy import (symbols, solve, Eq, sqrt, Rational, simplify,
                   expand, factor, discriminant, Poly, plot)

x = symbols('x')
a, b, c, h, k_sym = symbols('a b c h k')

# ---------------------------------------------------------------------------
# Example 1: Standard Form Analysis  f(x) = ax² + bx + c
# ---------------------------------------------------------------------------

print("=== Standard Form Analysis ===")

f = 2*x**2 - 8*x + 6

# Roots (x-intercepts)
roots = solve(f, x)
print(f"f(x) = {f}")
print(f"Roots: x = {roots}")

# Discriminant
disc = discriminant(Poly(f, x))
print(f"Discriminant: {disc}")
if disc > 0:
    print("  => Two distinct real roots")
elif disc == 0:
    print("  => One repeated real root")
else:
    print("  => Two complex roots")

# Vertex: x_v = -b/(2a)
coeffs = Poly(f, x).all_coeffs()
a_val, b_val, c_val = coeffs
x_vertex = Rational(-b_val, 2 * a_val)
y_vertex = f.subs(x, x_vertex)
print(f"Vertex: ({x_vertex}, {y_vertex})")
print(f"Axis of symmetry: x = {x_vertex}")
print(f"Opens: {'upward' if a_val > 0 else 'downward'}")

# ---------------------------------------------------------------------------
# Example 2: Vertex Form  f(x) = a(x - h)² + k
# ---------------------------------------------------------------------------

print("\n=== Convert to Vertex Form (Completing the Square) ===")

# Complete the square for 3x² + 12x + 7
f2 = 3*x**2 + 12*x + 7
coeffs2 = Poly(f2, x).all_coeffs()
a2, b2, c2 = coeffs2

h_val = Rational(-b2, 2 * a2)
k_val = f2.subs(x, h_val)

vertex_form = a2 * (x - h_val)**2 + k_val
print(f"Standard: {f2}")
print(f"Vertex form: {a2}(x - ({h_val}))² + ({k_val})")
print(f"Verify: expand gives {expand(vertex_form)}")

# ---------------------------------------------------------------------------
# Example 3: Symbolic Quadratic Formula
# ---------------------------------------------------------------------------

print("\n=== Quadratic Formula (Symbolic) ===")
quadratic = a*x**2 + b*x + c
roots_symbolic = solve(Eq(quadratic, 0), x)
print(f"For ax² + bx + c = 0:")
for i, r in enumerate(roots_symbolic):
    print(f"  x_{i+1} = {r}")

# Vieta's formulas
print(f"\nVieta's formulas for roots r1, r2:")
print(f"  r1 + r2 = {simplify(roots_symbolic[0] + roots_symbolic[1])}")
print(f"  r1 * r2 = {simplify(roots_symbolic[0] * roots_symbolic[1])}")

# ---------------------------------------------------------------------------
# Example 4: Application - Projectile Motion
# "A ball is thrown upward at 20 m/s from a height of 5m.
#  h(t) = -5t² + 20t + 5. Find max height and when it hits ground."
# ---------------------------------------------------------------------------

print("\n=== Projectile Motion Application ===")
t = symbols('t')
h = -5*t**2 + 20*t + 5

# Time to reach max height
t_max = solve(h.diff(t), t)[0]
h_max = h.subs(t, t_max)
print(f"h(t) = {h}")
print(f"Max height: {h_max}m at t = {t_max}s")

# When does it hit the ground?
t_ground = solve(Eq(h, 0), t)
t_ground_positive = [t_val for t_val in t_ground if t_val > 0]
print(f"Hits ground at t = {t_ground_positive[0]} ≈ {float(t_ground_positive[0]):.3f}s")
