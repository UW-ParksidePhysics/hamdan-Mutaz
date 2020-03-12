from math import pi

m = 0.43  # kg
g = 9.81  # m / s^2

CD = 0.2  # Drag Coefficient
ρ = 1.2  # kg / m^3
a = 0.11  # 11 cm = 0.11 m (SI units)
A = pi * (a ** 2)  # m^2

for V in range(10, 120+1, 110):  # km/h

    print("")

    Fd = 0.5 * CD * ρ * A * (V ** 2)
    Fg = m * g
    Ratio = Fd / Fg

    if V == 10:
        print("~~~Soft Kick~~~")
    if V == 120:
        print("~~~Hard Kick~~~")

    print("Drag Force = ", Fd, "N")
    print("Gravity Force = ", Fg, "N")
    print("Ratio of Drag to Gravity Forces:", Ratio)
