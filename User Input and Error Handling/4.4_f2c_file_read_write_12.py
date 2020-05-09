from numpy import array
infile = open('Fdeg.dat', 'r')

z = []
for line in infile:
    numbers_str = line.split()
    z1 = [str(z) for z in numbers_str]
    z.append(z1)
infile.close()

F = []
count = 3
while count <= 8:
    F.append(float(z[count][2]))
    count += 1
F = array(F)
C = (5 / 9) * (F - 32)

infile = open('FdegCdeg.dat', 'w')

count = 0
while count <= len(C) -1:
    infile.write(str(F[count])), infile.write(' ')
    infile.write(str(C[count])), infile.write('\n')
    count += 1
infile.close()
