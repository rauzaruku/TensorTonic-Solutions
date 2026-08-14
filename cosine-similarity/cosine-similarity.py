import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    A = np.linalg.norm(a)
    B = np.linalg.norm(b)
    result = np.dot(a,b)

    if A == 0 or B == 0:
        return 0.0
        
    return float(result/(A*B))
    
    pass