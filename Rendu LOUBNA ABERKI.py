# ==========================================================
# Linear Diophantine Equation Solver
# Equation form: a·x + b·y = c
# Author: (LOUBNA ABERKI)
# ==========================================================

def extended_Pgcd(a, b):
    """Extended Euclidean Algorithm.
    Returns (g, x, y) such that a*x + b*y = g = Pgcd(a, b)
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_Pgcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

def solve_diophantine(a, b, c):
    """Solves a·x + b·y = c and returns (has_solution, g, x0, y0)"""
    g, x0, y0 = extended_Pgcd(abs(a), abs(b))
    if c % g != 0:
        return (False, g, None, None)

    # Scale the solution
    x0 *= c // g
    y0 *= c // g

    # Adjust signs if a or b are negative
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0

    return (True, g, x0, y0)

# ==========================================================
# MAIN PROGRAM
# ==========================================================
print("=== Linear Diophantine Equation Solver ===")
print("Equation: a·x + b·y = c")
print("-------------------------------------------")

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
except ValueError:
    print("⚠️ Please enter valid integers.")
    exit()

has_sol, g, x0, y0 = solve_diophantine(a, b, c)

print("\n-------------------------------------------")
if not has_sol:
    print(f"No integer solution exists because Pgcd(a,b) = {g} does not divide c = {c}.")
else:
    print("✅  Solutions exist!")
    print(f"Pgcd(a, b) = {g}")
    print(f"One particular solution: x0 = {x0}, y0 = {y0}")
    print("\nGeneral solution:")
    print(f"    x = {x0} + ({b//g})·k")
    print(f"    y = {y0} - ({a//g})·k")
    print("where k ∈ ℤ (any integer).")

    # Verification
    check = a * x0 + b * y0
    print(f"\nVerification: {a}·({x0}) + {b}·({y0}) = {check}")

print("-------------------------------------------")
