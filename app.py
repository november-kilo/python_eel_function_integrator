import eel
import sympy as sp


@eel.expose
def integrate_function(f, a, b):
    fx = sp.sympify(f)
    f_latex = sp.latex(fx)
    ans = sp.latex(sp.integrate(fx, (x, a, b)))
    return f'\\int_{{%s}}^{{%s}} %s\\ dx = %s' % (a, b, f_latex, ans)


@eel.expose
def limit_function(f, limit_point):
    fx = sp.sympify(f)
    l = sp.latex(sp.limit(fx, x, limit_point))
    return f'\\lim_{{x\\to %s}} %s = %s' % (limit_point, sp.latex(fx), l)


x = sp.symbols('x')
eel.init('frontend', allowed_extensions=['.js', '.html'])
eel.start('main.html')
