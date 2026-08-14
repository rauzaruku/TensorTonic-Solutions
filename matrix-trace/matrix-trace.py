import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    total = 0
    for i in range(A.shape[0]):
        total += A[i,i]
    return total
    pass
