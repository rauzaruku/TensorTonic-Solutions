import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A =  np.array(A)

    m, n = A.shape
    result = np.zeros((n,m))

    for i in range(n):
        for j in range(m):
            result[i,j] = A[j,i]
    return result
    pass
