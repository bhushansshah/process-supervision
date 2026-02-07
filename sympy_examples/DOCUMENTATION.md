# SymPy Capabilities for Mathematics — Documentation

This document provides a comprehensive overview of every SymPy example file in this collection,
organized to match the math domain hierarchy. Each file demonstrates specific SymPy capabilities
that can be used as a **tool** for solving mathematical problems programmatically.

---

## Table of Contents

1. [Applied Mathematics](#1-applied-mathematics)
2. [Algebra](#2-algebra)
3. [Linear Algebra](#3-linear-algebra)
4. [Abstract Algebra](#4-abstract-algebra)
5. [Discrete Mathematics](#5-discrete-mathematics)
6. [Geometry](#6-geometry)
7. [Number Theory](#7-number-theory)
8. [Precalculus](#8-precalculus)
9. [Calculus](#9-calculus)
10. [Differential Equations](#10-differential-equations)
11. [Summary: Key SymPy Modules](#11-summary-key-sympy-modules)

---

## 1. Applied Mathematics

### `01_applied_mathematics/01_math_word_problems.py`

**What it does:** Translates natural-language word problems into symbolic equations and solves them automatically.

**Key SymPy features used:**
- `symbols()` — create symbolic variables
- `Eq()` — define equations
- `solve()` — solve systems of equations
- `diff()` — differentiation (for optimization problems)
- `Rational()` — exact fraction arithmetic

**Examples covered:**
| Problem Type | Approach |
|---|---|
| Age word problems | Set up 2 equations, 2 unknowns |
| Distance-Rate-Time | Single variable linear equation |
| Mixture problems | Weighted-average equation |
| Work rate problems | Combined-rate equation |
| Profit maximization | Derivative = 0 for optimization |

**Usefulness as a tool:** Can auto-solve any word problem once translated to equations. Core SymPy function `solve()` handles linear, polynomial, and non-linear systems.

---

### `01_applied_mathematics/02_statistics.py`

**What it does:** Uses SymPy's `sympy.stats` module for probability distributions, expected values, variance, and probability queries.

**Key SymPy features used:**
- `Normal`, `Binomial`, `Poisson`, `Uniform`, `Exponential` — distribution constructors
- `E()` — expected value
- `variance()`, `std()` — spread measures
- `P()` — probability of events
- `density()` — probability mass/density function

**Examples covered:**
- Standard Normal distribution (E, Var, P queries)
- Binomial distribution (discrete events)
- Poisson distribution (rare events)
- Uniform and Exponential distributions
- Symbolic distributions (parameterized by μ, σ)

**Usefulness as a tool:** Can compute exact probabilities and expectations symbolically rather than numerically.

---

### `01_applied_mathematics/03_probability.py`

**What it does:** Covers probability computations including dice, coins, conditional probability, Bayes' theorem, and expected value.

**Key SymPy features used:**
- `Die()`, `Coin()` — finite sample space objects
- `P(event, given)` — conditional probability
- `Bernoulli()` — Bernoulli trials
- Rational arithmetic for exact Bayes' theorem computation

**Examples covered:**
- Dice probability (sums, comparisons)
- Biased coin probability
- Conditional probability P(A|B)
- Bernoulli trials
- Bayes' theorem (medical test example)
- Expected value of a game

---

### `01_applied_mathematics/04_permutations_combinations.py`

**What it does:** Demonstrates counting methods — permutations, combinations, binomial theorem, Pascal's triangle, and advanced counting (multinomial, stars-and-bars).

**Key SymPy features used:**
- `factorial()`, `binomial()` — core counting functions
- `nP()`, `nC()` — permutation/combination helpers
- `expand()` — binomial theorem expansion

**Examples covered:**
- Factorials and symbolic factorial simplification
- P(n,r) permutations
- C(n,r) combinations (including poker hands C(52,5))
- Binomial theorem expansions
- Pascal's triangle
- Stars and bars, multinomial coefficients (MISSISSIPPI arrangements)

---

## 2. Algebra

### `02_algebra/01_integers_fractions_decimals.py`

**What it does:** Demonstrates SymPy's exact arithmetic with integers, fractions, and decimal-fraction conversion.

**Key SymPy features:** `Rational()`, `Integer()`, `gcd()`, `lcm()`, `Abs()`, `nsimplify()`

**Highlights:**
- Exact fraction arithmetic (no floating-point errors)
- Auto-simplification of fractions (24/36 → 2/3)
- Decimal ↔ fraction conversion
- Ordering and comparing fractions
- Absolute value and sign

---

### `02_algebra/02_simple_equations.py`

**What it does:** Solves one-step, two-step, multi-step linear equations and proportions, plus systems of linear equations (2 and 3 variables).

**Key SymPy features:** `solve()`, `Eq()`

**Highlights:**
- Step-by-step complexity progression (one-step → multi-step)
- Proportions (cross multiplication)
- Systems of 2 and 3 linear equations

---

### `02_algebra/03_algebraic_expressions.py`

**What it does:** Manipulates algebraic expressions — expansion, factoring, simplification, collecting terms, partial fractions, and substitution.

**Key SymPy features:** `expand()`, `factor()`, `simplify()`, `collect()`, `cancel()`, `apart()`, `together()`, `subs()`

**Highlights:**
- Expand products like (x+y)^3
- Factor quadratics and cubics
- Simplify rational expressions
- Partial fraction decomposition
- Multi-variable substitution

---

### `02_algebra/04_equations_and_inequalities.py`

**What it does:** Solves linear, quadratic, polynomial, rational, and absolute value equations. Also solves inequalities and non-linear systems.

**Key SymPy features:** `solve()`, `solveset()`, `S.Reals`, `Interval`, `Abs()`

**Highlights:**
- Quadratic formula (both numeric and symbolic)
- Polynomial equations (degree 3, 4)
- Absolute value equations
- Inequality solving (returns interval solutions)
- Non-linear system: circle-line intersection

---

### `02_algebra/05_polynomial_operations.py`

**What it does:** Polynomial-specific operations: arithmetic, division, root-finding, GCD/LCM of polynomials, discriminant, and composition.

**Key SymPy features:** `Poly()`, `div()`, `roots()`, `real_roots()`, `discriminant()`, `gcd()`, `lcm()`

**Highlights:**
- Polynomial inspection (degree, coefficients, leading term)
- Long division with quotient and remainder
- Root-finding (with multiplicities)
- Polynomial GCD/LCM
- Discriminant analysis (real vs. complex roots)
- Polynomial composition f(g(x))

---

### `02_algebra/06_sequences_and_series.py`

**What it does:** Arithmetic/geometric sequences, famous summation formulas, Taylor series, Fibonacci/Lucas, and products.

**Key SymPy features:** `Sum()`, `summation()`, `Product()`, `series()`, `fibonacci()`, `lucas()`

**Highlights:**
- General terms and sum formulas for arithmetic/geometric sequences
- Closed-form sums: Σk, Σk², Σk³
- Infinite geometric series
- Taylor/Maclaurin series for e^x, sin, cos, ln
- Fibonacci and Lucas sequences

---

### `02_algebra/07_quadratic_functions.py`

**What it does:** Analyzes quadratic functions: vertex, axis of symmetry, discriminant, converting to vertex form, Vieta's formulas, and projectile motion application.

**Key SymPy features:** `Poly()`, `discriminant()`, `diff()`, `solve()`

**Highlights:**
- Standard form → vertex form (completing the square)
- Discriminant interpretation
- Vieta's formulas verification
- Projectile motion: max height and ground-hit time

---

### `02_algebra/08_exponential_functions.py`

**What it does:** Covers exponential simplification, solving exponential equations, growth/decay models, half-life, and compound interest.

**Key SymPy features:** `exp()`, `solve()`, `limit()`, `N()`, `powsimp()`

**Highlights:**
- Simplify exponential expressions
- Solve equations like 2^x = 32, e^(2x) = 7
- Exponential growth model with doubling time
- Radioactive decay and Carbon-14 dating
- Compound interest (including continuous compounding via limit)

---

### `02_algebra/09_logarithmic_functions.py`

**What it does:** Demonstrates logarithm properties, expansion/combination, change of base, solving log equations, and applications (pH scale).

**Key SymPy features:** `log()`, `ln()`, `expand_log()`, `logcombine()`, `solve()`

**Highlights:**
- Log base conversion: log(x, base)
- Product, quotient, and power rules
- Combining multiple logs into one
- Solving equations with logarithms
- pH calculation application

---

### `02_algebra/10_complex_numbers.py`

**What it does:** Complex number arithmetic, polar form, Euler's formula, roots of unity, complex equations, and De Moivre's theorem.

**Key SymPy features:** `I`, `re()`, `im()`, `Abs()`, `arg()`, `conjugate()`, `exp(I*theta)`

**Highlights:**
- Full complex arithmetic (+, -, *, /)
- Polar form conversion
- Euler's identity e^(iπ) + 1 = 0
- nth roots of unity
- De Moivre's theorem verification

---

## 3. Linear Algebra

### `03_linear_algebra/01_vectors.py`

**What it does:** Vector operations: dot product, cross product, magnitude, projection, unit vectors, and linear independence.

**Key SymPy features:** `Matrix()`, `.dot()`, `.cross()`, `.norm()`, `CoordSys3D`

**Highlights:**
- Vector arithmetic and scalar multiplication
- Angle between vectors via dot product
- Cross product with perpendicularity verification
- Vector projection formula
- Linear independence check via matrix rank

---

### `03_linear_algebra/02_matrices.py`

**What it does:** Comprehensive matrix operations: creation, arithmetic, determinant, inverse, row reduction (RREF), eigenvalues/eigenvectors, diagonalization, and solving linear systems.

**Key SymPy features:** `Matrix()`, `.det()`, `.inv()`, `.rref()`, `.eigenvals()`, `.eigenvects()`, `.diagonalize()`, `.solve()`, `.nullspace()`, `.columnspace()`

**Highlights:**
- Special matrices (identity, zero, diagonal)
- RREF and rank computation
- Full eigenvalue/eigenvector decomposition
- Matrix diagonalization with verification
- Solving Ax = b
- Null space, column space, row space

---

### `03_linear_algebra/03_determinants.py`

**What it does:** Determinant computation, properties verification, cofactor/adjugate matrices, minors, Cramer's rule, and symbolic determinants.

**Key SymPy features:** `.det()`, `.cofactor_matrix()`, `.adjugate()`, `.minor()`

**Highlights:**
- Determinant properties: det(AB) = det(A)det(B), det(A^T) = det(A)
- Cofactor expansion
- Cramer's rule for solving systems
- Symbolic determinant formulas

---

### `03_linear_algebra/04_linear_transformations.py`

**What it does:** Represents linear transformations as matrices — rotation, scaling, reflection, shear, kernel/image analysis, and change of basis.

**Key SymPy features:** `Matrix()`, `cos()`, `sin()`, `.nullspace()`, `.columnspace()`, `.inv()`

**Highlights:**
- 2D rotation matrix composition (R(α)·R(β) = R(α+β))
- Scaling and shear transformations
- Reflection over arbitrary lines
- Rank-nullity theorem verification
- Change of basis transformation

---

## 4. Abstract Algebra

### `04_abstract_algebra/01_group_theory.py`

**What it does:** Explores permutation groups: cycle notation, composition, symmetric/cyclic/dihedral/alternating groups, subgroups, and Lagrange's theorem.

**Key SymPy features:** `Permutation`, `PermutationGroup`, `SymmetricGroup`, `CyclicGroup`, `DihedralGroup`, `AlternatingGroup`

**Highlights:**
- Permutation composition (non-commutative)
- Group order, generators, abelian/cyclic checks
- S₃, S₄ symmetric groups
- Dihedral groups D₃, D₄
- Subgroup testing and Lagrange's theorem

---

## 5. Discrete Mathematics

### `05_discrete_mathematics/01_combinatorics.py`

**What it does:** Advanced combinatorial functions: integer partitions, Bell numbers, Catalan numbers, Stirling numbers, Bernoulli numbers, harmonic numbers, derangements.

**Key SymPy features:** `npartitions()`, `bell()`, `catalan()`, `stirling()`, `bernoulli()`, `harmonic()`, `subfactorial()`

**Highlights:**
- Integer partitions p(n)
- Bell numbers (set partitions)
- Catalan numbers (parenthesizations, binary trees)
- Stirling numbers of the second kind
- Derangement counting

---

### `05_discrete_mathematics/02_logic.py`

**What it does:** Propositional logic: truth tables, simplification (De Morgan's), normal forms (CNF/DNF), satisfiability (SAT), and logical equivalence.

**Key SymPy features:** `And`, `Or`, `Not`, `Implies`, `Equivalent`, `to_cnf()`, `to_dnf()`, `satisfiable()`, `SOPform()`, `POSform()`

**Highlights:**
- Truth table generation
- De Morgan's law simplification
- CNF and DNF conversion
- SAT solving (finding satisfying assignments)
- Tautology and contradiction detection
- SOP/POS from minterms/maxterms

---

## 6. Geometry

### `06_geometry/01_plane_geometry.py`

**What it does:** Plane geometry: points, distances, lines, angles, triangles, regular polygons, area (shoelace), and geometric predicates.

**Key SymPy features:** `Point`, `Line`, `Segment`, `Triangle`, `RegularPolygon`, `Polygon`

**Highlights:**
- Distance and midpoint computation
- Angle between lines, parallel/perpendicular checks
- Triangle properties (area, perimeter, centroid, circumcenter, incenter, orthocenter)
- Regular polygon area, perimeter, interior angle, apothem
- Collinearity and point-in-polygon tests

---

### `06_geometry/02_circles.py`

**What it does:** Circle geometry: equations, tangent lines, circle-line intersections, circle-circle intersections, inscribed/circumscribed circles, arc length, and sector area.

**Key SymPy features:** `Circle`, `Line`, `Triangle.incircle`, `Triangle.circumcircle`

**Highlights:**
- Circle from center+radius or 3 points
- Point-circle relationship (inside/on/outside)
- Tangent line computation from external points
- Intersection algorithms
- Incircle and circumcircle of triangles

---

### `06_geometry/03_triangulations.py`

**What it does:** Triangle-specific geometry: Law of Cosines, Law of Sines, Heron's formula, triangle centers, Euler line, and similarity testing.

**Key SymPy features:** `Triangle`, `acos()`, `asin()`, `sqrt()`

**Highlights:**
- Law of Cosines for side/angle computation
- Law of Sines
- Heron's formula for area from three sides
- All four triangle centers with Euler line verification
- Similarity testing and scale factor

---

### `06_geometry/04_solid_geometry.py`

**What it does:** 3D solid geometry formulas: volume and surface area of sphere, cylinder, cone, box, tetrahedron, torus, pyramid, plus volume via revolution integration.

**Key SymPy features:** Symbolic expressions with `pi`, `sqrt`, `Rational`, `integrate()`

**Highlights:**
- All standard solid formulas (symbolic)
- Numeric evaluation at specific dimensions
- Volume of revolution (disk method) for sphere derivation
- Space diagonal of rectangular prism

---

### `06_geometry/05_differential_geometry.py`

**What it does:** Curvature of plane curves, parametric curve curvature, arc length computation, Frenet-Serret frame for 3D curves, and Gaussian curvature.

**Key SymPy features:** `diff()`, `integrate()`, `sqrt()`, `Matrix`, symbolic differentiation

**Highlights:**
- Curvature formula κ = |y''|/(1+y'²)^(3/2)
- Ellipse curvature (parametric)
- Arc length of circle, parabola, helix
- Tangent, Normal, Binormal vectors (TNB frame)
- Gaussian curvature of a sphere = 1/R²

---

## 7. Number Theory

### `07_number_theory/01_prime_numbers.py`

**What it does:** Primality testing, prime generation, prime counting π(n), primorial, Sieve of Eratosthenes, twin primes, Goldbach verification, and Mersenne primes.

**Key SymPy features:** `isprime()`, `prime()`, `primerange()`, `nextprime()`, `prevprime()`, `primepi()`, `primorial()`, `sieve`

**Highlights:**
- Fast primality testing for large numbers
- Prime generation in ranges
- Twin prime enumeration
- Goldbach conjecture verification
- Mersenne prime detection

---

### `07_number_theory/02_factorization.py`

**What it does:** Integer factorization, divisor enumeration, perfect numbers, Euler's totient function φ(n), Möbius function, and highly composite numbers.

**Key SymPy features:** `factorint()`, `divisors()`, `divisor_count()`, `divisor_sigma()`, `totient()`, `mobius()`

**Highlights:**
- Prime factorization with formatted output
- All divisors with count and sum
- Perfect number detection (6, 28, 496, 8128)
- Totient properties: φ(p)=p-1, Σφ(d)=n
- Highly composite number enumeration

---

### `07_number_theory/03_congruences.py`

**What it does:** Modular arithmetic, modular inverse, Chinese Remainder Theorem (CRT), Fermat's little theorem, Euler's theorem, primitive roots, and linear congruences.

**Key SymPy features:** `mod_inverse()`, `crt()`, `totient()`, `primitive_root()`, `is_primitive_root()`

**Highlights:**
- Modular arithmetic operations
- Modular inverse with verification
- CRT for solving simultaneous congruences
- Fermat's little theorem verification
- Primitive root computation

---

### `07_number_theory/04_gcd_lcm.py`

**What it does:** GCD and LCM computation, fundamental identity (GCD×LCM = a×b), extended Euclidean algorithm (Bézout's identity), coprime testing, and applications.

**Key SymPy features:** `gcd()`, `lcm()`, `gcdex()`, `factorint()`

**Highlights:**
- GCD/LCM of pairs and multiple numbers
- Bézout coefficients (extended Euclidean algorithm)
- GCD via prime factorization
- Application: simplifying fractions

---

## 8. Precalculus

### `08_precalculus/01_functions.py`

**What it does:** Function analysis: evaluation, domain finding, composition, inverse functions, piecewise functions, even/odd testing, and zero-finding.

**Key SymPy features:** `Lambda()`, `solveset()`, `Piecewise()`, `Abs()`, `simplify()`

**Highlights:**
- Symbolic function evaluation f(a+1)
- Domain analysis (excluded values, inequality constraints)
- Function composition f(g(x)) and g(f(x))
- Inverse function computation via solve
- Even/odd classification

---

### `08_precalculus/02_limits.py`

**What it does:** Computing limits: basic, at infinity, one-sided, famous limits, indeterminate forms (0/0, ∞/∞, 0·∞, 1^∞, 0^0), and squeeze theorem.

**Key SymPy features:** `limit(expr, var, point, dir)`

**Highlights:**
- Automatic L'Hopital's rule application
- All indeterminate forms handled
- One-sided limits with '+' and '-' direction
- Famous limits: sin(x)/x, (1+1/x)^x = e

---

### `08_precalculus/03_trigonometric_functions.py`

**What it does:** Exact trig values, identity verification, simplification, solving trig equations, inverse trig functions, and degree-radian conversion.

**Key SymPy features:** `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `trigsimp()`, `expand_trig()`, `solveset()`

**Highlights:**
- Exact values table (π/6, π/4, π/3, etc.)
- Double angle and sum formulas
- Trig simplification engine
- Solving trig equations (returns general solutions with n∈Z)
- Inverse trig function evaluation

---

## 9. Calculus

### `09_calculus/01_derivatives.py`

**What it does:** Differentiation: basic rules, product/quotient rule, chain rule, higher-order derivatives, implicit differentiation, and partial derivatives.

**Key SymPy features:** `diff(expr, var, order)`, `Derivative()`, `Function()`, `solve()`

**Highlights:**
- All basic derivative rules
- Chain rule (automatic)
- Higher-order derivatives up to 6th order
- Implicit differentiation (x²+y²=25)
- Partial derivatives with mixed-partial equality verification

---

### `09_calculus/02_applications_of_derivatives.py`

**What it does:** Optimization (critical points, second derivative test), related rates, tangent lines, Newton's method, Taylor polynomials, and L'Hopital's rule.

**Key SymPy features:** `diff()`, `solve()`, `limit()`, `series()`, `Function()`

**Highlights:**
- Critical point classification (min/max/saddle)
- Optimization: minimize surface area of a box
- Related rates: sliding ladder
- Tangent line equation
- Newton's method iteration
- Taylor polynomial approximation error

---

### `09_calculus/03_integrals.py`

**What it does:** Indefinite and definite integration, area between curves, volume of revolution (disk and shell methods), improper integrals, average value, and arc length.

**Key SymPy features:** `integrate(expr, var)`, `integrate(expr, (var, a, b))`, `oo`

**Highlights:**
- Basic antiderivatives
- Definite integrals with exact results
- Area between curves
- Volume of revolution (disk and shell)
- Improper integrals (including Gaussian integral √π)
- Arc length computation

---

### `09_calculus/04_techniques_of_integration.py`

**What it does:** Integration techniques: u-substitution, integration by parts, trigonometric integrals, partial fractions, trigonometric substitution, and the Gaussian integral.

**Key SymPy features:** `integrate()`, `apart()`, `simplify()`

**Highlights:**
- All techniques handled automatically by SymPy
- Partial fractions decomposition before integration
- Trig integrals: sin²(x), cos²(x), sec³(x)
- Trig substitution: 1/√(1-x²), √(4-x²)
- Full Gaussian integral: ∫₋∞^∞ e^(-x²) dx = √π

---

### `09_calculus/05_multivariable_calculus.py`

**What it does:** Partial derivatives, gradient, Hessian matrix, double/triple integrals, Jacobians (polar/spherical), Lagrange multipliers, divergence, and curl.

**Key SymPy features:** `diff()`, `integrate()`, `hessian()`, `Matrix()`, `solve()`

**Highlights:**
- Gradient vector computation
- Hessian for critical point classification
- Double integrals in polar coordinates
- Triple integrals in spherical coordinates
- Jacobian determinant derivation
- Lagrange multipliers optimization
- Divergence and curl of vector fields

---

## 10. Differential Equations

### `10_differential_equations/01_odes.py`

**What it does:** Solves ODEs: separable, linear, IVP, second-order (homogeneous and non-homogeneous), harmonic oscillator, damped oscillator, exact, and Bernoulli equations.

**Key SymPy features:** `dsolve()`, `classify_ode()`, `checkodesol()`, `Function()`, `Derivative()`

**Highlights:**
- Automatic ODE classification
- General solutions with arbitrary constants C₁, C₂
- Initial value problems (IVP) with specific solutions
- Harmonic oscillator y''+ω²y=0
- Damped oscillator
- Solution verification

---

### `10_differential_equations/02_pdes.py`

**What it does:** Solves first-order PDEs and verifies solutions of classic PDEs (heat equation, wave equation, Laplace equation).

**Key SymPy features:** `pdsolve()`, `classify_pde()`, `checkpdesol()`, `diff()`

**Highlights:**
- First-order PDE solving (transport equation)
- Heat equation solution verification
- Wave equation: d'Alembert solution verification
- Laplace equation: harmonic function verification
- Gaussian curvature connection

---

## 11. Summary: Key SymPy Modules

| Module | Purpose | Math Domains |
|---|---|---|
| `sympy.core` | Symbols, numbers, basic ops | All |
| `sympy.solvers` | Equation solving | Algebra, Precalculus |
| `sympy.simplify` | Expression simplification | All |
| `sympy.polys` | Polynomial manipulation | Algebra |
| `sympy.matrices` | Linear algebra | Linear Algebra |
| `sympy.geometry` | Geometric objects | Geometry |
| `sympy.ntheory` | Number theory functions | Number Theory |
| `sympy.combinatorics` | Permutations, groups | Abstract Algebra, Combinatorics |
| `sympy.stats` | Probability & statistics | Applied Math, Probability |
| `sympy.logic` | Boolean algebra, SAT | Discrete Math, Logic |
| `sympy.calculus` | Limits, continuity | Precalculus, Calculus |
| `sympy.integrals` | Integration | Calculus |
| `sympy.series` | Sequences, Taylor series | Algebra, Calculus |
| `sympy.vector` | Vector calculus | Linear Algebra, Calculus |
| `sympy.diffgeom` | Differential geometry | Geometry |
| `sympy.solvers.ode` | ODE solving | Differential Equations |
| `sympy.solvers.pde` | PDE solving | Differential Equations |

---

## Quick Start

```bash
# Install SymPy
pip install sympy

# Run any example
python sympy_examples/01_applied_mathematics/01_math_word_problems.py
python sympy_examples/09_calculus/01_derivatives.py
```

## File Structure

```
sympy_examples/
├── 01_applied_mathematics/
│   ├── 01_math_word_problems.py
│   ├── 02_statistics.py
│   ├── 03_probability.py
│   └── 04_permutations_combinations.py
├── 02_algebra/
│   ├── 01_integers_fractions_decimals.py
│   ├── 02_simple_equations.py
│   ├── 03_algebraic_expressions.py
│   ├── 04_equations_and_inequalities.py
│   ├── 05_polynomial_operations.py
│   ├── 06_sequences_and_series.py
│   ├── 07_quadratic_functions.py
│   ├── 08_exponential_functions.py
│   ├── 09_logarithmic_functions.py
│   └── 10_complex_numbers.py
├── 03_linear_algebra/
│   ├── 01_vectors.py
│   ├── 02_matrices.py
│   ├── 03_determinants.py
│   └── 04_linear_transformations.py
├── 04_abstract_algebra/
│   └── 01_group_theory.py
├── 05_discrete_mathematics/
│   ├── 01_combinatorics.py
│   └── 02_logic.py
├── 06_geometry/
│   ├── 01_plane_geometry.py
│   ├── 02_circles.py
│   ├── 03_triangulations.py
│   ├── 04_solid_geometry.py
│   └── 05_differential_geometry.py
├── 07_number_theory/
│   ├── 01_prime_numbers.py
│   ├── 02_factorization.py
│   ├── 03_congruences.py
│   └── 04_gcd_lcm.py
├── 08_precalculus/
│   ├── 01_functions.py
│   ├── 02_limits.py
│   └── 03_trigonometric_functions.py
├── 09_calculus/
│   ├── 01_derivatives.py
│   ├── 02_applications_of_derivatives.py
│   ├── 03_integrals.py
│   ├── 04_techniques_of_integration.py
│   └── 05_multivariable_calculus.py
├── 10_differential_equations/
│   ├── 01_odes.py
│   └── 02_pdes.py
└── DOCUMENTATION.md
```

## Total: 30 example files covering 10 math domains
