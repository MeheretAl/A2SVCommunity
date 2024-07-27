def isToeplitzMatrix(matrix : list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > 0 and j > 0:
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        
    return True