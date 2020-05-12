"""
Fit a quadratic polynomial to a two row Numpy array of x-y data using Numpy's polyfit function
    Module name:
        quadratic_fit
    Parameters:
        data: ndarray, shape (2, M)
        x-y data to be fit. M is the number of data points.
    Returns:
        quadratic_coefficients: ndarray, shape (3,)
        Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
"""


def quadratic_fit(data):
    from numpy import polyfit

    un_data = zip(*data)
    data_2 = list(un_data)

    quadratic_coefficients = polyfit(data_2[0], data_2[1], 2)
    return quadratic_coefficients


if __name__ == '__main__':
    print(quadratic_fit(sys.argv[1]))
