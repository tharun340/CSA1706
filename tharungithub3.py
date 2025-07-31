def transpose_matrix(matrix):
    # Transpose by swapping rows with columns
    return [list(row) for row in zip(*matrix)]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Original Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transposed)

if __name__ == "__main__":
    main()
