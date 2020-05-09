  
def read_constants(filename):
    infile = open(filename, 'r')
    constants = {}
    infile.readline()
    for line in infile:
        if not line.startswith('-'):
            words = line.split()
            constant = float(words[-2])
            if len(words[:-1]) == 4:
                substance = words[0] + ' ' + words[1] + ' ' + words[2]
            elif len(words[:-1]) == 3:
                substance = words[0] + ' ' + words[1]
            else:
                substance = words[0]

            if len(words[:-1]) == 4:
                unit = words[4]
            else:
                unit = words[3]
            constants[substance] = constant
    infile.close()
    return constants


# constants = read_constants('constants.txt')
# print(constants['gravitational constant'])
