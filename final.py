import matplotlib.pyplot as plt
import statistics as st
import generate_matrix as gm
import lowest_eigenvectors_12 as le
import univariate_statistics_12 as us
import fit_curve_array_12
import quadratic_fit_12 as qf
from equations_of_state import eos
import numpy as np
import two_column_text_read_12 as tct


filename = 'Pt.Fm-3m.GGA-PBE.volumes_energies.dat'
display_Graph = True
eos = 'birch-murnaghan'
potential_name = 'square'
number_of_dimensions = 110
potential_parameter = 100



# 1.
def parse_file_name(filename):
    to_parse = filename.split('.')
    CS, CSS, AA = to_parse[0:3]
    print(to_parse[0:3])
    return CS, CSS, AA


#

CS, CSS, AA = parse_file_name(filename)
data = tct.two_column_text_read12(filename)
print('Data Read In:')
print(data)

# 3.
data1 = data/2
print(data1)


# 4.
statistics = us.univariate_statistics(data)
print('Statistics of Data from File:')
print(statistics)

# 5.
quadratic_coefficients = qf.quadratic_fit(data)
print('Quadratic Coefficients of Revised Data:')
print(quadratic_coefficients)

# 6.

un_data = zip(*data)
data = list(un_data)
print("DATA", data)
volumes = data[0]
energies = data[1]


#7

def convert_units(value_to_convert_from, units_of_value_converted_from, unit_to_convert_to):
    if units_of_value_converted_from == 'cubic bohr/atom':
        value_in_requested_units = value_to_convert_from * 0.148185

    elif units_of_value_converted_from == 'rydberg/atom':
        value_in_requested_units = value_to_convert_from * 13.606
        #
    elif units_of_value_converted_from == 'rydberg/cubic bohr':
        value_in_requested_units = value_to_convert_from / 29421.0265
    else:
        value_in_requested_units = unit_to_convert_to
    return value_in_requested_units


# 8.

data = np.array(data)

data = data / 2
volumes = np.array(volumes)
volumes = volumes / 2
energies = np.array(energies)
energies = energies / 2

# stuggled on this part alot just dont know how to put the pieces together



plt.xlabel(r' $V$  [eV/atom] ')
plt.ylabel(r' $E$  [$\AA^3$/atom] ')


#julia helped answer alot of my questions for this final,as well as paul. I used alot of the code i saw in the help sessions this is the best i can do 
