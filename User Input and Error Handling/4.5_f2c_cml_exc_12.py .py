import sys
F = int(sys.argv[1])  # 4.2_f2c_cml_12.py 212


def C(F):
    C = (5 / 9) * (F - 32)
    return C


print("Temperature in Celsius degrees =", C(F))
