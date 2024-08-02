def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    
    if mode == "column":
        means = []
        for j in range(number_of_columns):
            column_sum = sum(matrix[i][j] for i in range(number_of_rows))
            column_mean = column_sum / number_of_rows
            means.append(column_mean)
    
    elif mode == "row":
        means = []
        for i in range(number_of_rows):
            row_sum = sum(matrix[i][j] for j in range(number_of_columns))
            row_mean = row_sum / number_of_columns
            means.append(row_mean)
    
    
    return means
