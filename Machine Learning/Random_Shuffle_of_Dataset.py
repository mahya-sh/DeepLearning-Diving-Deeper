import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)
    
    permutation = np.random.permutation(len(y))
    X_shuffled = X[permutation]
    y_shuffled = y[permutation]
    
    #idx = np.arange(X.shape[0])
    #np.random.shuffle(idx)
    
    return X_shuffled, y_shuffled
