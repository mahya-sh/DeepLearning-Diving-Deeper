import numpy as np
def make_diagonal(x):
	n = len(x)
	m = np.zeros((n,n))
	for i in range(n):
		m[i][i] = x[i]
		i +=1
	return m
