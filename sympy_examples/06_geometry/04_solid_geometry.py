"""
SymPy for Solid Geometry (3D Shapes, Volume, Surface Area)
============================================================
Demonstrates 3D geometry computations for common solids
using symbolic expressions.

Relevant domain: Geometry > Solid Geometry > 3D Shapes, Volume, Surface Area
"""

from sympy import symbols, pi, Rational, sqrt, simplify, N, integrate, oo

r, h, a, b, l, s = symbols('r h a b l s', positive=True)

# ---------------------------------------------------------------------------
# Example 1: Sphere
# ---------------------------------------------------------------------------

print("=== Sphere (radius r) ===")
volume_sphere = Rational(4, 3) * pi * r**3
surface_sphere = 4 * pi * r**2
print(f"Volume = {volume_sphere}")
print(f"Surface Area = {surface_sphere}")
print(f"  r=5: Volume = {volume_sphere.subs(r, 5)} ≈ {float(volume_sphere.subs(r, 5)):.2f}")
print(f"  r=5: Surface = {surface_sphere.subs(r, 5)} ≈ {float(surface_sphere.subs(r, 5)):.2f}")

# ---------------------------------------------------------------------------
# Example 2: Cylinder
# ---------------------------------------------------------------------------

print("\n=== Cylinder (radius r, height h) ===")
volume_cyl = pi * r**2 * h
surface_cyl = 2 * pi * r * h + 2 * pi * r**2  # lateral + 2 bases
print(f"Volume = {volume_cyl}")
print(f"Surface Area = {surface_cyl}")
print(f"  r=3, h=10: Volume = {volume_cyl.subs([(r, 3), (h, 10)])} ≈ {float(volume_cyl.subs([(r, 3), (h, 10)])):.2f}")

# ---------------------------------------------------------------------------
# Example 3: Cone
# ---------------------------------------------------------------------------

print("\n=== Cone (radius r, height h) ===")
volume_cone = Rational(1, 3) * pi * r**2 * h
slant = sqrt(r**2 + h**2)
surface_cone = pi * r * slant + pi * r**2  # lateral + base
print(f"Volume = {volume_cone}")
print(f"Slant height = {slant}")
print(f"Surface Area = {surface_cone}")
print(f"  r=4, h=3: Volume = {volume_cone.subs([(r, 4), (h, 3)])}")
print(f"  r=4, h=3: Slant = {slant.subs([(r, 4), (h, 3)])}")

# ---------------------------------------------------------------------------
# Example 4: Rectangular Prism (Box)
# ---------------------------------------------------------------------------

print("\n=== Rectangular Prism (a × b × h) ===")
volume_box = a * b * h
surface_box = 2 * (a*b + b*h + a*h)
diagonal_box = sqrt(a**2 + b**2 + h**2)
print(f"Volume = {volume_box}")
print(f"Surface Area = {surface_box}")
print(f"Space diagonal = {diagonal_box}")
print(f"  3×4×5: Volume = {volume_box.subs([(a, 3), (b, 4), (h, 5)])}")
print(f"  3×4×5: Surface = {surface_box.subs([(a, 3), (b, 4), (h, 5)])}")
print(f"  3×4×5: Diagonal = {diagonal_box.subs([(a, 3), (b, 4), (h, 5)])}")

# ---------------------------------------------------------------------------
# Example 5: Regular Tetrahedron
# ---------------------------------------------------------------------------

print("\n=== Regular Tetrahedron (edge a) ===")
volume_tet = a**3 * sqrt(2) / 12
surface_tet = sqrt(3) * a**2
print(f"Volume = {volume_tet}")
print(f"Surface Area = {surface_tet}")
print(f"  a=6: Volume = {simplify(volume_tet.subs(a, 6))} ≈ {float(volume_tet.subs(a, 6)):.2f}")

# ---------------------------------------------------------------------------
# Example 6: Torus
# ---------------------------------------------------------------------------

print("\n=== Torus (major radius R, tube radius r_tube) ===")
R = symbols('R', positive=True)
r_tube = symbols('r_t', positive=True)
volume_torus = 2 * pi**2 * R * r_tube**2
surface_torus = 4 * pi**2 * R * r_tube
print(f"Volume = {volume_torus}")
print(f"Surface Area = {surface_torus}")
print(f"  R=5, r=2: Volume = {volume_torus.subs([(R, 5), (r_tube, 2)])} ≈ {float(volume_torus.subs([(R, 5), (r_tube, 2)])):.2f}")

# ---------------------------------------------------------------------------
# Example 7: Pyramid
# ---------------------------------------------------------------------------

print("\n=== Square Pyramid (base side a, height h) ===")
a, h = symbols('a h', positive=True)
volume_pyr = Rational(1, 3) * a**2 * h
slant_pyr = sqrt((a/2)**2 + h**2)
surface_pyr = a**2 + 2 * a * slant_pyr  # base + 4 triangular faces
print(f"Volume = {volume_pyr}")
print(f"Slant height = {simplify(slant_pyr)}")
print(f"Surface Area = {simplify(surface_pyr)}")
print(f"  a=6, h=4: Volume = {volume_pyr.subs([(a, 6), (h, 4)])}")

# ---------------------------------------------------------------------------
# Example 8: Volume via Integration (Revolution)
# Sphere volume by revolving semicircle y = √(R²-x²) around x-axis
# ---------------------------------------------------------------------------

print("\n=== Volume of Revolution (Disk Method) ===")
from sympy import Symbol
x = Symbol('x')
R_val = Symbol('R', positive=True)

# V = π ∫ y² dx = π ∫ (R²-x²) dx from -R to R
y_sq = R_val**2 - x**2
V = pi * integrate(y_sq, (x, -R_val, R_val))
print(f"V = π ∫₋ᴿᴿ (R²-x²) dx = {simplify(V)}")
print(f"This equals (4/3)πR³? {simplify(V - Rational(4,3)*pi*R_val**3) == 0}")
