import eel
from sympy import symbols, sympify, integrate, latex


@eel.expose
def function_to_latex_integral(f, a, b):
    expr = sympify(f)
    ans = latex(expr)
    return f'\\int_{{%s}}^{{%s}} %s\\ dx' % (a, b, ans)


@eel.expose
def integrate_function(f, a, b):
    x = symbols('x')
    expr = sympify(f)
    ans = latex(integrate(expr, (x, a, b)))
    return ans


eel.init('frontend', allowed_extensions=['.js', '.html'])
eel.start('main.html')
