### Playground to test various modules

from Final_Review_1 import two_column_text_read

data = two_column_text_read("volumes_energies.dat")

print("DATA")
print(data)
print("")

from Final_Review_2 import univariate_statistics

statistics = univariate_statistics(data)

print("STATISTICS")
print(statistics)
print("")

from Final_Review_3 import quadratic_fit

quadratic_coefficients = quadratic_fit(data)

print("QUADRATIC_COEFFICIENTS")
print(quadratic_coefficients)
print("")

from Final_Review_4 import fit_curve_array

fit_curve = fit_curve_array(quadratic_coefficients, statistics[2], statistics[3], 100)

print("FIT_CURVE")
print(fit_curve)
print("")

from Final_Review_5 import plot_data_with_fit

plot_data_with_fit(data, fit_curve, 1, 3)  # data_format & fit_format can be anyone of 1=R, 2=B, or 3=Y
