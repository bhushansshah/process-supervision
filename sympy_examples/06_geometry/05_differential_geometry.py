"""
SymPy for Differential Geometry
=================================
Demonstrates curvature, arc length, parametric curves,
and surface analysis using SymPy.

Relevant domain: Geometry > Differential Geometry > Curvature, Geodesics
"""

from sympy import (symbols, sqrt, diff, simplify, integrate, pi, cos, sin,
                   Abs, Rational, N, atan2, Matrix, Function)

t, s, u, v = symbols('t s u v')

# ---------------------------------------------------------------------------
# Example 1: Curvature of a Plane Curve y = f(x)
# κ = |y''| / (1 + y'²)^(3/2)
# ---------------------------------------------------------------------------

print("=== Curvature of y = f(x) ===")
x = symbols('x')

# Parabola y = x²
y = x**2
y_prime = diff(y, x)
y_double_prime = diff(y, x, 2)
kappa = Abs(y_double_prime) / (1 + y_prime**2)**Rational(3, 2)

print(f"y = {y}")
print(f"y' = {y_prime}")
print(f"y'' = {y_double_prime}")
print(f"κ(x) = {simplify(kappa)}")
print(f"κ(0) = {kappa.subs(x, 0)} (maximum curvature at vertex)")
print(f"κ(1) = {simplify(kappa.subs(x, 1))}")

# Circle y² + x² = r² => y = √(r²-x²)
r = symbols('r', positive=True)
y_circle = sqrt(r**2 - x**2)
y1 = diff(y_circle, x)
y2 = diff(y_circle, x, 2)
kappa_circle = simplify(Abs(y2) / (1 + y1**2)**Rational(3, 2))
print(f"\nCircle: κ = {kappa_circle} (constant = 1/r)")

# ---------------------------------------------------------------------------
# Example 2: Parametric Curve Curvature
# κ = |x'y'' - y'x''| / (x'² + y'²)^(3/2)
# ---------------------------------------------------------------------------

print("\n=== Parametric Curve Curvature ===")

# Ellipse: x = a·cos(t), y = b·sin(t)
a, b = symbols('a b', positive=True)
x_t = a * cos(t)
y_t = b * sin(t)

dx = diff(x_t, t)
dy = diff(y_t, t)
ddx = diff(x_t, t, 2)
ddy = diff(y_t, t, 2)

kappa_param = simplify(Abs(dx * ddy - dy * ddx) / (dx**2 + dy**2)**Rational(3, 2))
print(f"Ellipse: x = a·cos(t), y = b·sin(t)")
print(f"κ(t) = {kappa_param}")

# ---------------------------------------------------------------------------
# Example 3: Arc Length
# ---------------------------------------------------------------------------

print("\n=== Arc Length ===")

# Arc length of circle: x = R·cos(t), y = R·sin(t), t ∈ [0, 2π]
R = symbols('R', positive=True)
x_c = R * cos(t)
y_c = R * sin(t)

ds = sqrt(diff(x_c, t)**2 + diff(y_c, t)**2)
arc = integrate(ds, (t, 0, 2*pi))
print(f"Circle (radius R): arc length = {simplify(arc)} = 2πR ✓")

# Arc length of parabola y = x² from x=0 to x=1
x = symbols('x')
y = x**2
arc_parabola = integrate(sqrt(1 + diff(y, x)**2), (x, 0, 1))
print(f"Parabola y=x² from 0 to 1: arc length = {arc_parabola}")
print(f"  ≈ {float(arc_parabola):.6f}")

# Helix: x = cos(t), y = sin(t), z = t, t ∈ [0, 2π]
z_t = t
ds_helix = sqrt(diff(cos(t), t)**2 + diff(sin(t), t)**2 + diff(z_t, t)**2)
arc_helix = integrate(ds_helix, (t, 0, 2*pi))
print(f"Helix arc length (one turn): {simplify(arc_helix)}")

# ---------------------------------------------------------------------------
# Example 4: Frenet-Serret Frame (for 3D curves)
# ---------------------------------------------------------------------------

print("\n=== Frenet-Serret Frame (Helix) ===")

# Helix: r(t) = (cos t, sin t, t)
r_vec = Matrix([cos(t), sin(t), t])

# Tangent vector T = r'/|r'|
r_prime = r_vec.diff(t)
speed = simplify(r_prime.norm())
T_vec = simplify(r_prime / speed)
print(f"Tangent T = {T_vec.T}")

# Normal vector N = T'/|T'|
T_prime = T_vec.diff(t)
T_prime_norm = simplify(T_prime.norm())
N_vec = simplify(T_prime / T_prime_norm)
print(f"Normal N = {N_vec.T}")

# Binormal B = T × N
B_vec = simplify(T_vec.cross(N_vec))
print(f"Binormal B = {B_vec.T}")

# Curvature and torsion
kappa_3d = simplify(T_prime_norm / speed)
print(f"Curvature κ = {kappa_3d}")

# ---------------------------------------------------------------------------
# Example 5: Surface Curvature (Gaussian Curvature of a sphere)
# For a surface z = f(x,y), Gaussian curvature K = (fxx*fyy - fxy²)/((1+fx²+fy²)²)
# ---------------------------------------------------------------------------

print("\n=== Gaussian Curvature ===")
x, y = symbols('x y')

# Sphere: z = √(R²-x²-y²)
R = symbols('R', positive=True)
z = sqrt(R**2 - x**2 - y**2)

zx = diff(z, x)
zy = diff(z, y)
zxx = diff(z, x, 2)
zyy = diff(z, y, 2)
zxy = diff(z, x, y)

K = simplify((zxx * zyy - zxy**2) / (1 + zx**2 + zy**2)**2)
print(f"Sphere z = √(R²-x²-y²)")
print(f"Gaussian curvature K = {K}")
print(f"K = 1/R² (constant, as expected for a sphere)")
