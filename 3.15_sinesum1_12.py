from math import sin, pi


def S(t, n, T):
    r_sum = 0
    for i in range(1, n + 1):
        Add = (1 / ((2 * i) - 1)) * sin((2 * ((2 * i) - 1) * pi * t) / T)
        r_sum = r_sum + Add
    S_t_n = (4 / pi) * r_sum
    return S_t_n


def f(t, T):
    if 0 < t < T / 2:
        f = 1
    elif t == T / 2:
        f = 0
    elif T / 2 < t < T:
        f = -1
    return f


y = [1, 3, 5, 10, 30, 100]
x = [0.01, 0.25, 0.49]

T = 2 * pi
print("  ", 0.01, "               ", 0.25, "               ", 0.49)
for n in y:
    row = []
    for a in x:
        t = a * T
        row.append(f(t, T) - S(t, n, T))
    print(n, row)

# The table seems to produce less error when a = 0.25 and when n = 30
