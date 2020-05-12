"""
Read in two columns of data from a text file of arbitrary length
    Module name:
        two_column_text_read
    Parameters:
        filename: str
        Name of file to be read in.
    Returns:
        data: ndarray, shape (2, M)
        x-y data read in from file. M is the number of data points.
    Raises:
        OSError
        When filename cannot be found for reading.
"""


def two_column_text_read(filename):
    import numpy as np
    from os import path

    if path.exists(filename):
        x = []
        y = []
        
        infile = open(filename, 'r')
        for line in infile:
            coords = line.split()
            x.append(float(coords[0]))
            y.append(float(coords[1]))
        infile.close()
        
        x, y = np.array(x), np.array(y)
        
        # data = np.array(list(zip(x, y)))
        data = np.vstack((x, y)).T

        return data
    else:
        return print("OSError: filename cannot be found for reading.")


if __name__ == '__main__':
    print(two_column_text_read(sys.argv[1]))    


""" __Paul__ """
