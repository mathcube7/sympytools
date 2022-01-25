from sympy import expand, Integral, diff
import sympy


class Path:
    """Represent an integration path in some metric space."""

    def __init__(self, name, funcs, limits):
        """ Constructs Path.

        Parameters
        ----------
        name: str
            The symbol to use represent path in SymPy expressions
        funcs: dict
            The parametrization.
        limits: tuple
            The parameter and its range (param, from, to)

        Examples
        --------

        Unit circle in the xy-plane:

        circle = Path('C', {x: cos(t),y: sin(t)},
                         (t, 0, 2*pi))

        Unit circle in the complex plane:

        circle = Path('C', {z: exp(i*t), (t, 0, 2*pi)}

        """
        self.name = name
        self.funcs = funcs
        self.limits = limits
        start, end = [{var: self.funcs[var].subs(self.limits[0], self.limits[k_])
                       for var in funcs.keys()}
                      for k_ in (1, 2)]

        self.closed = start == end


class LineIntegral(sympy.Expr):
    """A general line integral."""

    def __init__(self, integrand, var, path):
        self.path = path

        Ii = Integral(integrand, var).transform(
            var, path.funcs[var]).subs(path.funcs)

        self.parametrized = Integral(Ii.args[0], path.limits)
        self.unparamatrized = Integral(integrand, var)

    def doit(self):
        return self.parametrized.doit()

    def _latex(self, printer):
        args = [printer._print(arg)
                for arg in [self.path.name,
                            self.unparamatrized.args[0],
                            self.unparamatrized.args[1][0]
                            ]]
        if self.path.closed:
            return r"\oint_{%s} %s \, d%s" % tuple(args)

        return r"\int_{%s} %s \, d%s" % tuple(args)


class ContourIntegral(LineIntegral):
    """An integral over a function of a complex variable."""

    def __init__(self, integrand, var, path):
        """ Constructs CountourIntegral

             \int_C f(z) dz

            for contour C.

        Parameters
        ----------
        integrand: SymPy expression
        var: SymPy symbol
            the complex integration variable
        path: Path
            the contour along which to integrate
        """
        self.unparamatrized = Integral(integrand, var)
        z = path.funcs[var]
        para = path.limits[0]
        dz = diff(z, para)
        integrand = integrand.subs(var, path.funcs[var]) * dz
        self.parametrized = Integral(integrand, path.limits)


def factor_out(expr, fac):
    return fac * expand(expr / fac)

