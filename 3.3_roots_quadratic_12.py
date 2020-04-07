### The Easy Way ###

from numpy import roots

a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

Q = [a, b, c]
R = roots(Q)

print(R)
print()

### The 'Fun' Way ###

from math import sqrt

D2 = b ** 2 - 4 * a * c
if a == 0:
    print('a Cannot Equal Zero')

if D2 >= 0:
    D = sqrt(D2)
    x1 = (-b - D) / (2 * a)
    x2 = (2 * c) / (-b - D)
    R = [x1, x2]
    print("test_roots_float")
    print(R)

elif D2 < 0:
    D2 = -D2
    D = (sqrt(D2) / (2 * a))
    b2 = -b / (2 * a)
    print("test_roots_complex")
    print(b2, "+", D, "j", b2, "-", D, "j")
