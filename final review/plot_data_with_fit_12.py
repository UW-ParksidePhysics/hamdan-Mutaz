"""
Create a combined scatter and curve plot for the data and the fit polynomial, respectively, using Pyplot's plot function
    Module name:
        plot_data_with_fit
    Parameters:
        data: ndarray, shape(2, M)
        x-y data that was fit. M is the number of data points.
        fit_curve: ndarray, shape(2, N)
        x-y data created by the coeffecients of the fit function.
            N is the number of function evaluation points (usually much greater than M).
        data_format: str, optional
        Optional formatting specification for the style of the scatter plot data points.
            Default is ''.  See Pyplot's plot for specifications.
        fit_format: str, optional
        Optional formatting specification for the curve of the fit function. Default is ''.
            See Pyplot's plot for specifications.
    Returns:
        combined_plot
        A list of Line2D objects representing the plotted data. This is the default return type from Pyplot's plot.
"""


def plot_data_with_fit(data, fit_curve, data_format=0, fit_format=0):
    import matplotlib.pyplot as plt
    import numpy as np

    un_data = zip(*data)
    data = list(un_data)
    a_x1, a_y1 = np.array(data[0]), np.array(data[1])

    un_fit_curve = zip(*fit_curve)
    fit_curve = list(un_fit_curve)
    a_x2, a_y2 = np.array(fit_curve[0]), np.array(fit_curve[1])
    if data_format == 1:
        plt.plot(a_x1, a_y1, 'r')
    elif data_format == 2:
        plt.plot(a_x1, a_y1, 'b')
    elif data_format == 3:
        plt.plot(a_x1, a_y1, 'y')
    else:
        plt.plot(a_x1, a_y1)

    if fit_format == 1:
        plt.plot(a_x2, a_y2, 'r')
    elif fit_format == 2:
        plt.plot(a_x2, a_y2, 'b')
    elif fit_format == 3:
        plt.plot(a_x2, a_y2, 'y')
    else:
        plt.plot(a_x2, a_y2)

    plt.xlabel("Volume")
    plt.ylabel("Energy")
    return plt.show()
