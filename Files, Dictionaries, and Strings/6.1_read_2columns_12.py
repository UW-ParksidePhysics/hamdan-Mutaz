import matplotlib.pyplot as mp
from numpy import array
infile = open('xy.txt', 'r')

z = []
for line in infile:
    numbers_str = line.split()
    z1 = [float(z) for z in numbers_str]
    z.append(z1)
infile.close()

un_z = zip(*z)
z = list(un_z)

x = z[0]
y = z[1]

a_x = array(x)
a_y = array(y)

mp.plot(a_x, a_y)
mp.show()

print("Maximum of y =", max(y))
print("Minimum of y =", min(y))
