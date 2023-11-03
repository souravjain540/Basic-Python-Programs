# bisection method for finding zero points of a function


def f(x):
    return -4 * x + 2


def bisection(a, b, eps):
    while (b - a) > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


print(bisection(0, 1, 0.0001))