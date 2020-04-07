import time

v0 = int(input("What value is v0? "))
t = 0
g = 9.81


def y(t):
    y = (v0 * t) - (0.5 * g * (t ** 2))
    return y


End = int((2 * v0 / g))
print("t values", "   ", "y(t) values")
for t in range(0, End + 1):  # Set this line to be inactive, and set the other # lines to be active for while
# while t <= (2 * v0 / g):
    print(round(t, 2), "          ", y(t))
    time.sleep(0.3)
#   t = t + 1

if v0 == 0:
    0
else:
    print(round((2 * v0 / g), 5), "    ", y(2 * v0 / g))
