F = int(input("Temperature in Fahrenheit? "))


def C(F):
    C = (5 / 9) * (F - 32)
    return C


print("Temperature in Celsius degrees =", C(F))
