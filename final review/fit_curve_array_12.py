"""
Make fit curve using fit polynomial coefficients, NumPy's polyval, and minimum and maximum x-values
    Module name:
        fit_curve_array
    Parameters:
        quadratic_coefficients: ndarray, shape (3,)
        Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
        minimum_x: float
        Starting value for the fit_curve array.
        maximum_x: float
        Ending value for the fit curve array.
        number_of_points: int, optional
        Number of points N to return for final fit curve. Default is 100.
    Returns:
        fit_curve: ndarray, shape (2, N)
        x-y data created by the coefficients of the fit function. N is the number of function evaluation points.
    Raises:
        ArithmeticError
        When maximum_x < minimum x.
        IndexError
        When number_of_points <= 2.
"""


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):
    import numpy as np
    try:
        x = np.linspace(minimum_x, maximum_x, number_of_points)
    except ArithmeticError:
        if maximum_x < minimum_x:
            print("Max_x less than min_x.")
    
    try:
        y = np.polyval(quadratic_coefficients, x)
    except IndexError:
        if number_of_points <= 2:
            print("Index Error! How dare you!")
     
    # fit_curve = np.array(list(zip(x, y)))
    fit_curve = np.vstack((x, y)).T
    return fit_curve


if __name__ == '__main__':
    print(fit_curve_array(sys.argv[1]))
