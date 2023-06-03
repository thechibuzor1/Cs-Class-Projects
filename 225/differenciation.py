from sympy import symbols, diff

def differentiate_equation(expr, var='x'):
    x = symbols(var)
    diff_expr = diff(expr, x)
    return diff_expr

# Differentiate the equation y = x^3 + 2x^2 - 5x + 1 with respect to x
equation = 'x**3 + 2*x**2 - 5*x + 1'
differentiated_equation = differentiate_equation(equation)
print(differentiated_equation)

