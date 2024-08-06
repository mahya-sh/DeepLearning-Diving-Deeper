import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #returns a python list after reshaping by using numpy's tolist() method
    return np.array(a).reshape(new_shape).tolist()