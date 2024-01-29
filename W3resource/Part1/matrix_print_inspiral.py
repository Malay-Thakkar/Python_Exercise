def print_spiral(matrix):
    while matrix:
        # Print the first row
        print(matrix.pop(0), end=" ")

        # Print the last column
        if matrix and matrix[0]:
            for row in matrix:
                print(row.pop(), end=" ")

        # Print the last row in reverse
        if matrix:
            print(matrix.pop()[::-1], end=" ")

        # Print the first column in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                print(row.pop(0), end=" ")

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print_spiral(matrix)
