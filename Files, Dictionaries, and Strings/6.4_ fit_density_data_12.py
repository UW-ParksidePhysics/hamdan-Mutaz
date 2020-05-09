import matplotlib.pyplot as mp
mp.style.use('seaborn-whitegrid')
from numpy import array, poly1d, polyfit

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

mp.plot(x, y, 'r-')
mp.plot(x, y,  'o', color='red')

# First degree polynomial
deg = 1
coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print(p)
y_fitted = p(x)
mp.plot(x, y_fitted, 'b-')
# Second degree polynomial
deg = 2
coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print(p)
y_fitted = p(x)
mp.plot(x, y_fitted, 'y-')
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

mp.plot(x, y, 'r-')
mp.plot(x, y,  'o', color='red')

# First degree polynomial
deg = 1
coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print(p)
y_fitted = p(x)
mp.plot(x, y_fitted, 'b-')
# Second degree polynomial
deg = 2
coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print(p)
y_fitted = p(x)
mp.plot(x, y_fitted, 'y-')

mp.xlabel("Temperature in Celsius Degrees")
mp.ylabel("Density in kg/m^3")
mp.show()
