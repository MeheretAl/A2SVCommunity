def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    row = len(matrix)
    column = len(matrix[0])
    new_matrix = [[0] * row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix