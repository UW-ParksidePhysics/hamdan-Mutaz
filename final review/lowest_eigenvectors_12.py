"""
Identify eigenvectors with smallest K eigenvalues given input matrix using NumPy's eig function
    Module name:
        lowest_eigenvectors
    Parameters:
        square_matrix: ndarray, shape(M, M)
        Matrix to be characterized. Must be a square matrix of M rows and M columns where M is >=1.
        number_of_eigenvectors: int, optional
        Number of eigenvectors K with eigenvalues to return.  Default is 3.
    Returns:
        eigenvalues: ndarray, shape(K,)
        Array of the K lowest-value eigenvalues ordered from lowest to highest.
        eigenvectors: ndarray, shape(K, M)
        Array of K eigenvectors with M components arranged in order corresponding to their eigenvalues.
        The first index should correspond to the eigenvalue index in the eigenvalues array.
        The order of the components in the eigenvector remains the same as output by NumPy's eig.
"""


def square_matrix():
    from numpy import zeros, linalg, linspace, sqrt, sin, pi, sum, sort
    A = zeros([10, 10])

    n = 0
    while n <= 9:
        A[n, n] = 2
        n = n + 1
    
    n = 0
    while n <= 8:
        A[n, n + 1] = 1
        A[n + 1, n] = 1
        n = n + 1
        
    H = (1 / (2  (1 / 9 * 2))) * A
    print(H)





def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
    from numpy import zeros, linalg, linspace, sqrt, sin, pi, sum, sort, argsort

    M_rows = len(square_matrix)  # Function statement, only works in a function
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("Must be a square matrix of M rows and M columns where M is >=1.")
        count += 1

    (V, D) = linalg.eig(square_matrix)
    ordered_indices = argsort(V)
    
    print(V[ordered_indices[0:number_of_eigenvectors]])
    print(D[ordered_indices[0:number_of_eigenvectors]])
    return


def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
    from numpy import linalg, linspace, sqrt, sin, pi, sum, sort, argsort

    M_rows = len(square_matrix)  # Function statement, only works in a function
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("Must be a square matrix of M rows and M columns where M is >=1.")
        count += 1

    (V, D) = linalg.eig(square_matrix)
    ordered_indices = argsort(V)

    return (V[ordered_indices[0:number_of_eigenvectors]]), (D[ordered_indices[0:number_of_eigenvectors]])