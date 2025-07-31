def add_matrices(matrix1, matrix2):
    # Check if dimensions match
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Dimensions do not match
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    # Example matrices
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix2 = [
        [7, 8, 9],
        [10, 11, 12]
    ]

    print("Matrix 1:")
    print_matrix(matrix1)

    print("\nMatrix 2:")
    print_matrix(matrix2)

    result = add_matrices(matrix1, matrix2)

    if result:
        print("\nSum of matrices:")
        print_matrix(result)
    else:
        print("Error: Matrices dimensions do not match.")

if __name__ == "__main__":
    main()
