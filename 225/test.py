import sympy as sp

def picard_solver():
    # User inputs
    equation = input("Enter the differential equation (in terms of y and x): ")
    initial_condition = input("Enter the initial condition of y: ")
    n = int(input("Enter the number of iterations: "))

    # Parsing equation and initial condition
    y, x = sp.symbols('y x')
    equation = sp.sympify(equation)
    initial_condition = sp.sympify(initial_condition)

    # Iteration
    expansion = initial_condition
    for i in range(n):
        expansion = sp.integrate(equation.subs(y, expansion), x) + initial_condition
        print(f"Iteration {i+1}(y{i+1}): {expansion}")

    # User input for x value
    x_value = float(input("Enter an x value to substitute into the last iteration: "))
    final_result = expansion.subs(x, x_value)
    print(f"Expansion at x = {x_value}: {final_result}")

picard_solver()
