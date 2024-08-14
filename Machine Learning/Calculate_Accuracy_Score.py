import numpy as np

def accuracy_score(y_true, y_pred):
    acc = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            acc += 1
    acc = acc / len(y_true)
    ## accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return acc
