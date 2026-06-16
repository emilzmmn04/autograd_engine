# A 2x2 matrix: [[a, b], [c, d]]
matrix_a = [[1, 2], 
            [3, 4]]

matrix_b = [[5, 6], 
            [7, 8]]

def multiply_matrices(A, B):
    # Create a result matrix filled with zeros
    result = [[0, 0], [0, 0]]
    
    # Iterate through rows of A
    for i in range(len(A)):
        # Iterate through columns of B
        for j in range(len(B[0])):
            # Iterate through rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

print(multiply_matrices(matrix_a, matrix_b))
