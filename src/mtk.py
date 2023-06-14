from sympy import symbols, Eq, solve

# Define the variable x
x = symbols('x')

# Define the equation f(x)
equation = Eq(x**3 + 3*x**2 - 9*x - 7, 0)

# Solve the equation
solutions = solve(equation, x)

# Print the solutions
for solution in solutions:
    print(f"x = {solution}")
 