import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1,1) #column vector with n number of training examples
    theta = np.linalg.inv(X.T @ X ) @ X.T @ y
    theta = np.round(theta, 4).flatten().tolist()
    return theta
