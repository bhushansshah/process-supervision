"""
SymPy for Multivariable Calculus
==================================
Demonstrates partial derivatives, gradients, multiple integrals,
Jacobians, and Lagrange multipliers.

Relevant domain: Calculus > Integral Calculus > Multi-variable
"""

from sympy import (symbols, diff, integrate, sin, cos, exp, sqrt, pi,
                   Matrix, simplify, solve, Eq, Rational, oo, log,
                   Abs, Function, hessian)

x, y, z, t, r, theta, phi = symbols('x y z t r theta phi')

# ---------------------------------------------------------------------------
# Example 1: Partial Derivatives and Gradient
# ---------------------------------------------------------------------------

print("=== Partial Derivatives and Gradient ===")

f = x**2*y + y**3 - 2*x*z + z**2
print(f"f(x,y,z) = {f}")

grad = Matrix([diff(f, x), diff(f, y), diff(f, z)])
print(f"∇f = {grad.T}")

# Evaluate gradient at a point
point = {x: 1, y: 2, z: -1}
grad_at_point = grad.subs(point)
print(f"∇f(1, 2, -1) = {grad_at_point.T}")

# ---------------------------------------------------------------------------
# Example 2: Hessian Matrix
# ---------------------------------------------------------------------------

print("\n=== Hessian Matrix ===")
f = x**2 + y**2 - 4*x - 6*y + 13
H = hessian(f, [x, y])
print(f"f(x,y) = {f}")
print(f"Hessian H =\n{H}")

# Evaluate at critical points
critical = solve([diff(f, x), diff(f, y)], [x, y])
print(f"Critical points: {critical}")

# For this simple function, critical is a dict
if isinstance(critical, dict):
    cp_x, cp_y = critical[x], critical[y]
    H_val = H.subs([(x, cp_x), (y, cp_y)])
    det_H = H_val.det()
    print(f"  At ({cp_x}, {cp_y}): det(H) = {det_H}, H₁₁ = {H_val[0,0]}")
    if det_H > 0 and H_val[0, 0] > 0:
        print(f"    → Local minimum, f = {f.subs([(x, cp_x), (y, cp_y)])}")
    elif det_H > 0 and H_val[0, 0] < 0:
        print(f"    → Local maximum")
    elif det_H < 0:
        print(f"    → Saddle point")
else:
    for cp in critical:
        H_val = H.subs([(x, cp[0]), (y, cp[1])])
        det_H = H_val.det()
        det_num = float(det_H) if det_H.is_number else det_H
        h11_num = float(H_val[0, 0]) if H_val[0, 0].is_number else H_val[0, 0]
        print(f"  At {cp}: det(H) = {det_H}, H₁₁ = {H_val[0,0]}")
        if isinstance(det_num, float) and isinstance(h11_num, float):
            if det_num > 0 and h11_num > 0:
                print(f"    → Local minimum")
            elif det_num > 0 and h11_num < 0:
                print(f"    → Local maximum")
            elif det_num < 0:
                print(f"    → Saddle point")

# ---------------------------------------------------------------------------
# Example 3: Double Integrals
# ---------------------------------------------------------------------------

print("\n=== Double Integrals ===")

# ∫∫ xy dA over [0,1] × [0,2]
result = integrate(x*y, (x, 0, 1), (y, 0, 2))
print(f"∫₀¹ ∫₀² xy dy dx = {result}")

# Area of a region: ∫∫ 1 dA over disk x²+y² ≤ 1 (using polar)
area = integrate(r, (r, 0, 1), (theta, 0, 2*pi))
print(f"Area of unit disk (polar): {area}")

# Volume under z = 4 - x² - y² above xy-plane
# Using polar: z = 4 - r², integrate r from 0 to 2
vol = integrate((4 - r**2) * r, (r, 0, 2), (theta, 0, 2*pi))
print(f"Volume under z = 4-x²-y²: {vol}")

# ---------------------------------------------------------------------------
# Example 4: Triple Integrals
# ---------------------------------------------------------------------------

print("\n=== Triple Integrals ===")

# ∫∫∫ xyz dV over [0,1]³
result = integrate(x*y*z, (x, 0, 1), (y, 0, 1), (z, 0, 1))
print(f"∫₀¹∫₀¹∫₀¹ xyz dz dy dx = {result}")

# Volume of sphere using spherical coordinates
# ∫∫∫ ρ²sin(φ) dρ dφ dθ
rho = symbols('rho', positive=True)
R = symbols('R', positive=True)
V_sphere = integrate(rho**2 * sin(phi), (rho, 0, R), (phi, 0, pi), (theta, 0, 2*pi))
print(f"Volume of sphere (spherical coords): {V_sphere}")

# ---------------------------------------------------------------------------
# Example 5: Jacobian
# ---------------------------------------------------------------------------

print("\n=== Jacobian ===")

# Polar coordinates: x = r·cos(θ), y = r·sin(θ)
x_polar = r * cos(theta)
y_polar = r * sin(theta)

J = Matrix([[diff(x_polar, r), diff(x_polar, theta)],
            [diff(y_polar, r), diff(y_polar, theta)]])
jacobian_det = simplify(J.det())
print(f"Polar coords Jacobian matrix:\n{J}")
print(f"|J| = {jacobian_det}")

# Spherical coordinates
x_sph = rho * sin(phi) * cos(theta)
y_sph = rho * sin(phi) * sin(theta)
z_sph = rho * cos(phi)

J_sph = Matrix([
    [diff(x_sph, rho), diff(x_sph, phi), diff(x_sph, theta)],
    [diff(y_sph, rho), diff(y_sph, phi), diff(y_sph, theta)],
    [diff(z_sph, rho), diff(z_sph, phi), diff(z_sph, theta)]
])
jac_sph = simplify(J_sph.det())
print(f"\nSpherical coords |J| = {jac_sph}")

# ---------------------------------------------------------------------------
# Example 6: Lagrange Multipliers
# Minimize f(x,y) = x² + y² subject to g(x,y) = x + y - 1 = 0
# ---------------------------------------------------------------------------

print("\n=== Lagrange Multipliers ===")

lam = symbols('lambda')
f = x**2 + y**2
g = x + y - 1

# ∇f = λ∇g
L = f - lam * g  # Lagrangian
eqs = [diff(L, x), diff(L, y), diff(L, lam)]

sol = solve(eqs, [x, y, lam])
print(f"Minimize f = x² + y² subject to x + y = 1")
print(f"Solution: x = {sol[x]}, y = {sol[y]}, λ = {sol[lam]}")
print(f"Minimum value: f = {f.subs(sol)}")

# ---------------------------------------------------------------------------
# Example 7: Divergence and Curl
# ---------------------------------------------------------------------------

print("\n=== Divergence and Curl ===")

Fx = x**2 * y
Fy = y**2 * z
Fz = z**2 * x

div_F = diff(Fx, x) + diff(Fy, y) + diff(Fz, z)
print(f"F = ({Fx}, {Fy}, {Fz})")
print(f"div(F) = ∇·F = {div_F}")

curl_F = Matrix([diff(Fz, y) - diff(Fy, z),
                  diff(Fx, z) - diff(Fz, x),
                  diff(Fy, x) - diff(Fx, y)])
print(f"curl(F) = ∇×F = {curl_F.T}")
