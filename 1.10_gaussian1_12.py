from math import sqrt, pi, exp

m = 0
s = 2
x = 1

f = (1 / (sqrt(2 * pi) * s)) * exp(-0.5 * ((x - m) / s) ** 2)

print("f(x) = ", f)
