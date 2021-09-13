from sympy import *
import math


def estpi(terms):
    result = 0.0
    for n in range(terms):
        result += (-1.0)**n/(2.0*n+1.0)
    return 4 * result


y = estpi(100)
print(y)

n = 1000000
expr = (1 + 1/n)**n

z = limit(expr, n, math.inf)

print(z)
