print("Fahrenheit", "   ", "Approx Celsius", "   ", "Celsius")

Fahrenheit = 0
while Fahrenheit <= 100:
    Celsius = (Fahrenheit - 32) * (5 / 9)
    Approx_Celsius = (Fahrenheit - 30) / 2
    print(Fahrenheit, "           ", Approx_Celsius, "     ", Celsius)
    Fahrenheit = Fahrenheit + 10
