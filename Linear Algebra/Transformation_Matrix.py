import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	P= np.linalg.inv(C) @ B
	return P
##This P matrix can be used to transform any vector coordinates from the B basis to the C basis.
