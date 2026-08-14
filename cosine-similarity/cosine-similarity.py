import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    result = np.dot(a,b)

    if na == 0 or nb == 0:
        return 0.0
        
    return float(result/(na*nb))
    
    pass