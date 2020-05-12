"""
Calculate statistical characteristics of a data set
    Module name:
        univariate_statistics
    Parameters:
        data: ndarray, shape(2, M)
        x-y data to be characterized. M is the number of data points.
    Returns:
        statistics: ndarray, shape (6,)
        Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    Raises:
        IndexError
        When data array has inapproriate dimensions (!=2 rows, or <=1 column).
"""


def univariate_statistics(data):
    from math import sqrt
    from numpy import std
    un_data = zip(*data)
    data = list(un_data)
    try:
        minimum_x_value = min(data[0])  # Minimum x-value
        maximum_x_value = max(data[0])  # Maximum x-value
    except IndexError:
        if not len(data) == 2:
            print("Need only two columns")
    try:
        minimum_y_value = min(data[1])  # Minimum y-value
        maximum_y_value = max(data[1])  # Maximum y-value
    except IndexError:
        if len(data[0]) or len(data[1]) <=1:
            print("Need more than two data points")

    # Mean
    Sum = sum(data[0]) + sum(data[1])
    Len = len(data[0]) + len(data[1])
    mean = Sum / Len

    # Standard deviation
    standard_deviation = std(data)

    # Statistics
    statistics = [mean, standard_deviation,
                  minimum_x_value, maximum_x_value,
                  minimum_y_value, maximum_y_value]
    return statistics


if __name__ == '__main__':
    print(univariate_statistics(sys.argv[1]))
