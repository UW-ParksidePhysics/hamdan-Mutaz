from math import pi, log

for M in range(47, 67+1, 20):  # Mass in g

    print("")

    ρ = 1.038  # Density in g * cm^-3
    c = 3.7  # Specific Heat Capacity in J * g^-1 * K^-1
    K = 5.4 * (10 ** -3)  # Thermal Conductivity in W * cm^-1 * K^-1
    Tw = 100  # Temperature in C
    Ty = 70  # Temperature in C
    To = 20  # Temperature in C

    Numerator = ((M ** (2 / 3)) * c * (ρ ** (1 / 3)))
    Denominator = (K * (pi ** 2) * (((4 * pi) / 3) ** (2/3)))
    Temperatures = (To - Tw) / (Ty - Tw)
    t = (Numerator / Denominator) * (log(0.76 * Temperatures))  # Time in seconds

    if M == 47:
        print("~~~Small Egg~~~")
    if M == 67:
        print("~~~Large Egg~~~")

    print("Time necessary for center of egg to reach Ty =", t, "Seconds")
