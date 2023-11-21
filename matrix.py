n = 4
def generate_spiral_matrix(matrix):
    matrix = [[0] * n for _ in range(n)]
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    current_number = 1
    while current_number <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = current_number
            current_number += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = current_number
            current_number += 1
        right -= 1
        for i in range(right, left - 1, - 1):
            matrix[bottom][i] = current_number
            current_number += 1
        bottom -= 1
        for i in range(bottom, top - 1, - 1):
            matrix[i][left] = current_number
            current_number += 1
        left += 1
    return matrix

susamomgus = generate_spiral_matrix(n)

for row in susamomgus:
    print(*row)

