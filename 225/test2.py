from sympy import symbols, sympify, simplify

def taylor_series_equation(eq, x, y0, x0, y_prime, y_prime_prime):
    # Substitute y0 and x0 in y_prime
    y_prime = y_prime.subs([(x, x0), ('y', y0)])

    # Simplify the expression for y_prime
    y_prime = simplify(y_prime)

    # Substitute y0, x0, and y_prime in y_prime_prime
    y_prime_prime = y_prime_prime.subs([(x, x0), ('y', y0), ('y_prime', y_prime)])

    # Simplify the expression for y_prime_prime
    y_prime_prime = simplify(y_prime_prime)

    # Simplify the Taylor series expansion
    expansion = y0 + (x - x0) * y_prime + ((x - x0)**2 / 2) * y_prime_prime

    return expansion


# Example usage
x = symbols('x')
y = symbols('y')
eq_str = input("Enter the equation (in terms of x and y): ")
eq = sympify(eq_str)

x0 = float(input("Enter the initial value for x: "))
y0 = float(input("Enter the initial value for y: "))

# Specify the derivatives
y_prime_str = input("Enter the first derivative (in terms of x, y, and y_prime): ")
y_prime = sympify(y_prime_str)

y_prime_prime_str = input("Enter the second derivative (in terms of x, y, and y_prime): ")
y_prime_prime = sympify(y_prime_prime_str)

# Generate the Taylor series expansion
expansion = taylor_series_equation(eq, x, y0, x0, y_prime, y_prime_prime)

# Simplify the expansion by performing basic arithmetic operations
simplified_expansion = simplify(expansion)

print(f"Simplified Taylor series expansion: {simplified_expansion}")

# Specify the values for which to evaluate the expansion
x_values_str = input("Enter the values of x (comma-separated): ")
x_values = [float(x) for x in x_values_str.split(",")]

# Evaluate the Taylor series expansion at the given values
for x_val in x_values:
    y_val = simplified_expansion.subs([(x, x_val)])
    print(f"At x = {x_val}, y = {y_val}")
