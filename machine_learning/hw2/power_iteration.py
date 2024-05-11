import numpy as np


def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    r = np.random.rand(data.shape[0])
    for _ in range(num_steps):
        r = (data @ r) / np.linalg.norm(data @ r)
    eigenvalue = ((data @ r) / r)[0]
    return float(eigenvalue), r
