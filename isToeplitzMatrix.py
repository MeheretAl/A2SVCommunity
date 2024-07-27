def isToeplitzMatrix(matrix : list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > 0 and j > 0:
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        
    return True

mat = [[66], 
       [16]]
mat2 = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2],
]
print(isToeplitzMatrix(mat2))

'''
    [1,2,3,4]
    [2,1,3,4]
    [1,2,3,4]


'''