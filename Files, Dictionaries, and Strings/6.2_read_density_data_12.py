import matplotlib.pyplot as mp
mp.style.use('seaborn-whitegrid')
from numpy import array
infile = open('density_water.txt', 'r')

z = []
for line in infile:
    if not line.startswith('#'):
        if not line.startswith('\n'):
            numbers_str = line.split()
            z1 = [float(z) for z in numbers_str]
            z.append(z1)
infile.close()

un_z = zip(*z)
z = list(un_z)


x = z[0]
y = z[1]

mp.plot(x, y,  'o', color='blue')
mp.show()
###
###
###

infile = open('density_air.txt', 'r')

z = []
for line in infile:
    if not line.startswith('#'):
        if not line.startswith('\n'):
            numbers_str = line.split()
            z1 = [float(z) for z in numbers_str]
            z.append(z1)
infile.close()

un_z = zip(*z)
z = list(un_z)


x = z[0]
y = z[1]

mp.plot(x, y,  'o', color='red')
mp.xlabel("Temperature in Celsius Degrees")
mp.ylabel("Density in kg/m^3")
mp.show()
