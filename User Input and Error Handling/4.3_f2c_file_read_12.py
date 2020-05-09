infile = open('temperature_data.dat', 'r')

z = []
for line in infile:
    numbers_str = line.split()
    z1 = [str(z) for z in numbers_str]
    z.append(z1)
infile.close()
z = z[3][2]
z = float(z)

F = z


def C(F):
    C = (5 / 9) * (F - 32)
    return C


print("Temperature in Celsius degrees =", C(F))
