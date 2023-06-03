import time
import sympy as sp
from sympy import symbols, sympify, simplify

# Function to find the root of an equation using the bisection method


def bisection(f, a, b, tol=1e-6, max_iter=100):
    start_time = time.time()
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        print("Error: Function values at interval endpoints have the same sign.")
        return None
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            print("Root found:", c)
            print("--- %s runtime in seconds ---" %
                  (time.time() - start_time))
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    print("Error: Maximum number of iterations reached.")
    return None

# Function to find the root of an equation using the Newton-Raphson method


def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    start_time = time.time()
    for i in range(max_iter):
        fx = f(x0)
        if abs(fx) < tol:

            print("Root found:", x0)
            print("--- %s runtime in seconds ---" %
                  (time.time() - start_time))
            return x0
        f_prime_x = f_prime(x0)
        if f_prime_x == 0:
            print("Error: Derivative is zero at the current point.")
            return None
        x0 = x0 - fx / f_prime_x
    print("Error: Maximum number of iterations reached.")
    return None

# Function to find the root of an equation using the secant method


def secant(f, x0, x1, tol=1e-6, max_iter=100):
    start_time = time.time()
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:

            print("Root found:", x1)
            print("--- %s runtime in seconds ---" %
                  (time.time() - start_time))
            return x1
        if fx1 == fx0:
            print("Error: Function values at the current points are the same.")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0 = x1
        x1 = x2
    print("Error: Maximum number of iterations reached.")
    return None

# Function to solve an ordinary differential equation using the Taylor series method


def taylor_series_equation(eq, x, y0, x0, y_prime, y_prime_prime, y_prime_prime_prime, y_prime_prime_prime_prime):
    # Substitute y0 and x0 in y_prime
    y_prime = y_prime.subs([(x, x0), ('y', y0)])

    # Simplify the expression for y_prime
    y_prime = simplify(y_prime)

    # Substitute y0, x0, and y_prime in y_prime_prime
    y_prime_prime = y_prime_prime.subs(
        [(x, x0), ('y', y0), ('y_prime', y_prime)])

    # Simplify the expression for y_prime_prime
    y_prime_prime = simplify(y_prime_prime)

    # Substitute y0, x0, y_prime, and y_prime_prime in y_prime_prime_prime
    y_prime_prime_prime = y_prime_prime_prime.subs(
        [(x, x0), ('y', y0), ('y_prime', y_prime), ('y_prime_prime', y_prime_prime)])

    # Simplify the expression for y_prime_prime_prime
    y_prime_prime_prime = simplify(y_prime_prime_prime)

    # Substitute y0, x0, y_prime, y_prime_prime, and y_prime_prime_prime in y_prime_prime_prime_prime
    y_prime_prime_prime_prime = y_prime_prime_prime_prime.subs(
        [(x, x0), ('y', y0), ('y_prime', y_prime), ('y_prime_prime', y_prime_prime), ('y_prime_prime_prime', y_prime_prime_prime)])

    # Simplify the expression for y_prime_prime_prime_prime
    y_prime_prime_prime_prime = simplify(y_prime_prime_prime_prime)

    # Simplify the Taylor series expansion
    expansion = y0 + (x - x0) * y_prime + ((x - x0)**2 / 2) * y_prime_prime + ((x - x0)
                                                                               ** 3 / 6) * y_prime_prime_prime + ((x - x0)**4 / 24) * y_prime_prime_prime_prime

    return expansion


# Function to solve an ordinary differential equation using the Picard method


def picard_solver():
    # User inputs
    equation = input("Enter the differential equation (in terms of y and x): ")
    initial_condition = input("Enter the initial condition of y: ")
    n = int(input("Enter the number of iterations: "))

    start_time = time.time()
    # Parsing equation and initial condition
    y, x = sp.symbols('y x')
    equation = sp.sympify(equation)
    initial_condition = sp.sympify(initial_condition)

    # Iteration
    expansion = initial_condition
    for i in range(n):
        expansion = sp.integrate(equation.subs(
            y, expansion), x) + initial_condition
        print(f"Iteration {i+1}(y{i+1}): {expansion}")

    print("--- %s runtime in seconds ---" %
          (time.time() - start_time))

    # User input for x value
    x_value = float(
        input("Enter an x value to substitute into the last iteration: "))
    final_result = expansion.subs(x, x_value)
    print(f"Expansion at x = {x_value}: {final_result}")

# Function to solve an ordinary differential equation using Euler's method


def euler(f, x0, y0, h, num_steps):
    start_time = time.time()
    x = x0
    y = y0
    print(f"x0 = {x}, y0 = {y}")
    for i in range(num_steps):
        y += h * f(x, y)
        x += h
        print(f"x{i+1} = {x}, y{i+1} = {y}")

    print("--- %s runtime in seconds ---" %
          (time.time() - start_time))
    return y


# Main program
print("Welcome!")
while True:
    print("\nChoose an option:")
    print("1. Find the root of an equation")
    print("2. Solve an ordinary differential equation")
    print("3. Exit")
    option = input("Enter your choice (1, 2, or 3): ")

    if option == "1":
        equation_str = input("Enter the equation (in terms of x): ")
        equation = sp.sympify(equation_str)
        f = sp.lambdify(sp.Symbol('x'), equation)

        print("\nRoot Finding Methods:")
        print("1. Bisection Method")
        print("2. Newton-Raphson Method")
        print("3. Secant Method")
        method = input("Choose a method (1, 2, or 3): ")

        if method == "1":
            a = float(input("Enter the lower bound of the interval: "))
            b = float(input("Enter the upper bound of the interval: "))
            bisection(f, a, b)
        elif method == "2":
            x0 = float(input("Enter the initial guess: "))
            f_prime = sp.lambdify(
                sp.Symbol('x'), equation.diff(sp.Symbol('x')))
            newton_raphson(f, f_prime, x0)
        elif method == "3":
            x0 = float(input("Enter the first initial guess: "))
            x1 = float(input("Enter the second initial guess: "))
            secant(f, x0, x1)
        else:
            print("Invalid method choice.")

    elif option == "2":

        print("\nOrdinary Differential Equation (ODE) Solving Methods:")
        print("1. Taylor Series Method")
        print("2. Picard Method")
        print("3. Euler's Method")
        method = input("Choose a method (1, 2, or 3): ")

        if method == "1":
            print("TAYLOR'S SERIES SOLUTION")
            # Example usage
            x = symbols('x')
            y = symbols('y')
            print(
                "PLEASE NOTE: use ** to indicate power. i.e x^2 should be inputted as x**2.")
            print(
                "PLEASE NOTE: use y_prime to indicate y', y_prime_prime for y'' and soon...")
            print(
                "PLEASE NOTE: add '*' between each multiplying terms. i.e 2x should be inputted as 2*x and xy' as x*y_prime")

            eq_str = input("Enter the equation (in terms of x and y): ")
            eq = sympify(eq_str)

            x0 = float(input("Enter the initial value for x(x0): "))
            y0 = float(input("Enter the initial value for y(y0): "))

            # Specify the derivatives
            y_prime_str = input(
                "Enter the first derivative (in terms of x, y, and y_prime): ")
            y_prime = sympify(y_prime_str)

            y_prime_prime_str = input(
                "Enter the second derivative (in terms of x, y, and y_prime): ")
            y_prime_prime = sympify(y_prime_prime_str)

            y_prime_prime_prime_str = input(
                "Enter the third derivative (in terms of x, y, y_prime, and y_prime_prime): ")
            y_prime_prime_prime = sympify(y_prime_prime_prime_str)

            y_prime_prime_prime_prime_str = input(
                "Enter the fourth derivative (in terms of x, y, y_prime, y_prime_prime, and y_prime_prime_prime): ")
            y_prime_prime_prime_prime = sympify(y_prime_prime_prime_prime_str)
            start_time = time.time()
            # Generate the Taylor series expansion
            expansion = taylor_series_equation(
                eq, x, y0, x0, y_prime, y_prime_prime, y_prime_prime_prime, y_prime_prime_prime_prime)

            # Simplify the expansion by performing basic arithmetic operations
            simplified_expansion = simplify(expansion)

            print(
                f"Simplified Taylor series expansion: {simplified_expansion}")
            print("--- %s runtime in seconds ---" % (time.time() - start_time))

            # Specify the values for which to evaluate the expansion
            x_values_str = input("Enter the values of x (comma-separated): ")
            x_values = [float(x) for x in x_values_str.split(",")]

            # Evaluate the Taylor series expansion at the given values
            for x_val in x_values:
                y_val = simplified_expansion.subs([(x, x_val)])
                print(f"At x = {x_val}, y = {y_val}")

        elif method == "2":
            print("PICARD METHOD")
            picard_solver()
        elif method == "3":
            equation_str = input(
                "Enter the differential equation (in terms of x and y): ")
            equation = sp.sympify(equation_str)
            f = sp.lambdify((sp.Symbol('x'), sp.Symbol('y')), equation)
            x0 = float(input("Enter the initial value of x(x0): "))
            y0 = float(input("Enter the initial value of y(y0): "))
            h = float(input("Enter the step size(h): "))
            num_steps = int(input("Enter the number of steps(yn): "))
            euler(f, x0, y0, h, num_steps)
        else:
            print("Invalid method choice.")

    elif option == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please choose again.")
