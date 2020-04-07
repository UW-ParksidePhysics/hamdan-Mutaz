### Part a ###
def trapezint1(f, a, b, actual_area):
    A = ((b - a) / 2) * (f(a) + f(b))
    print("Area under the curve =", A)
    error = abs(A) - actual_area
    print("Error =", error)
    return trapezint1


### Part b ###
from math import sin, cos, pi


def f(x):
    f = cos(x)
    return f


a = 0
b = pi
actual_area = 0
trapezint1(f, a, b, actual_area)


def f(x):
    f = sin(x)
    return f


a = 0
b = pi
actual_area = 2
trapezint1(f, a, b, actual_area)


def f(x):
    f = sin(x)
    return f


a = 0
b = (pi / 2)
actual_area = 1
trapezint1(f, a, b, actual_area)
print()


### Part c ###
def trapezint2(f, a, b, actual_area):
    c = b / 2
    A = ((c - a) / 2) * (f(a) + f(c)) + ((b - c) / 2) * (f(c) + f(b))
    print("Area under the curve =", A)
    error = abs(A) - actual_area
    print("Error =", error)
    return trapezint2


def f(x):
    f = cos(x)
    return f


a = 0
b = pi
actual_area = 0
trapezint2(f, a, b, actual_area)


def f(x):
    f = sin(x)
    return f


a = 0
b = pi
actual_area = 2
trapezint2(f, a, b, actual_area)


def f(x):
    f = sin(x)
    return f


a = 0
b = (pi / 2)
actual_area = 1
trapezint2(f, a, b, actual_area)
print()


### Part d ###
def trapezint(f, a, b, n, actual_area):
    x = a
    A = 0
    w = 0
    h = (b - a) / n

    while w <= n:
        del_a = (f(a + (w * h)) + f(a + (w + 1) * h)) * (h / 2)
        A = A + del_a
        x = x + h
        w = w + 1
    print("Area under the curve =", A)
    error = abs(A) - actual_area
    print("Error =", error)
    return trapezint


### Part e ###
def test_trapezint():
    def f(x):
        f = cos(x)
        return f


    a = 0
    b = pi
    actual_area = 0
    trapezint(f, a, b, 10, actual_area)


    def f(x):
        f = sin(x)
        return f


    a = 0
    b = pi
    actual_area = 2
    trapezint(f, a, b, 10, actual_area)


    def f(x):
        f = sin(x)
        return f


    a = 0
    b = (pi / 2)
    actual_area = 1
    trapezint(f, a, b, 10, actual_area)
    return test_trapezint


test_trapezint()
