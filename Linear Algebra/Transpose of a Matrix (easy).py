def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    n = len(a)  # number of rows
    m = len(a[0])  # number of columns
    b = [[0] * n for _ in range(m)]  # initializing b with dimensions m x n

    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]

    return b
## instead of this, the whole code can be replaced by transposed_matrix = [list(i) for i in zip(*a)]
