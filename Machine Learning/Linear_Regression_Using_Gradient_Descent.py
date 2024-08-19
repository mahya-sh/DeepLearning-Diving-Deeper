import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        y_hat = X @ theta 
        error = y_hat - y.reshape(-1,1)  
        gradient = (X.T @ error) / m  
        theta -= alpha * gradient  
    
    return np.round(theta.flatten(), 4)
