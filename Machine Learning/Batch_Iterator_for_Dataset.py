import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    batches = []
    n_samples = len(X)
    for i in range(0, n_samples, batch_size):
        batch_X = X[i:i + batch_size]
        if y is not None:
            batch_y = y[i:i + batch_size]
            batches.append((batch_X.tolist(), batch_y.tolist()))
        else:
            batches.append(batch_X.tolist())
    return batches
