def f(x, a, b, c, n):
    return a * x**n + b * x + c


def bisection_method(arg):
    a, b, c, n, r, s = arg
    tolerance = 1e-6
    max_iterations = 1000

    if f(r, a, b, c, n) * f(s, a, b, c, n) >= 0:
        raise ValueError("The initial solutions do not bracket the root.")

    for i in range(max_iterations):
        x = (r + s) / 2
        if abs(f(x, a, b, c, n)) < tolerance:
            return round(x, 6)
        if f(x, a, b, c, n) * f(r, a, b, c, n) < 0:
            s = x
        else:
            r = x

    raise ValueError(
        "Bisection method did not converge within the maximum number of iterations.")


def newton_raphson_method(arg):
    a, b, c, n, r = arg
    tolerance = 1e-6
    max_iterations = 1000

    def f_prime(x):
        return n * a * x**(n-1) + b

    x = r

    for i in range(max_iterations):
        delta_x = f(x, a, b, c, n) / f_prime(x)
        x = x - delta_x
        if abs(delta_x) < tolerance:
            return round(x, 6)

    raise ValueError(
        "Newton-Raphson method did not converge within the maximum number of iterations.")


def secant_method(arg):
    a, b, c, n, r, s = arg
    tolerance = 1e-6
    max_iterations = 1000

    for i in range(max_iterations):
        x = r - f(r, a, b, c, n) * (r - s) / \
            (f(r, a, b, c, n) - f(s, a, b, c, n))
        if abs(f(x, a, b, c, n)) < tolerance:
            return round(x, 6)
        s = r
        r = x

    raise ValueError(
        "Secant method did not converge within the maximum number of iterations.")


def solve_transcendental_equation(method, arg):
    if method == "bisection":
        return bisection_method(arg)
    elif method == "newton-raphson":
        return newton_raphson_method(arg)
    elif method == "secant":
        return secant_method(arg)
    else:
        raise ValueError("Invalid method choice.")


def main():
    method = input(
        "Select a method (bisection, newton-raphson, secant): ").lower()

    equation = input("Equation: ")

    if method == "newton-raphson":
        arg_str = input(
            "Enter the values for a, b, c, n, r (comma or space-separated): ")
    else:
        arg_str = input(
            "Enter the values for a, b, c, n, r, s (comma or space-separated): ")
    arg_str = arg_str.replace("[", "").replace("]", "")
    initial_solution = input("Initial Solutions: ")
    arg = [int(x) for x in arg_str.replace(",", " ").split()]
    try:
        result = solve_transcendental_equation(method, arg)
        print("Value of x:", result)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
