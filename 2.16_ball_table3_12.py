import time

v0 = int(input("What value is v0? "))
t = 0
g = 9.81


def y(t):
    y = (v0 * t) - (0.5 * g * (t ** 2))
    return y


list_t = []
list_y = []
ty1 = []
ty2 = []
End = int((2 * v0 / g))
print("t values", "   ", "y(t) values")
for t in range(0, End + 1):
    list_t.append(t)
    list_y.append(y(t))
    print(round(t, 2), "          ", y(t))
    time.sleep(0.3)


if v0 == 0:
    0
else:
    print(round((2 * v0 / g), 5), "    ", y(2 * v0 / g))
    list_t.append(2 * v0 / g)
    list_y.append(y(2 * v0 / g))

print()

for T, Y in zip(list_t, list_y):
    ty1.append([T, Y])
print(ty1)

ty2.append(list_t)
ty2.append(list_y)
print(ty2)
