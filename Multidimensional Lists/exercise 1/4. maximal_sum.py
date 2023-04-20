rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_rows = matrix[row][col:col + 3]
        second_rows = matrix[row + 1][col:col + 3]
        third_rows = matrix[row + 2][col:col + 3]

        current_sum = sum(first_rows) + sum(second_rows) + sum(third_rows)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_rows, second_rows, third_rows]

print(f"Sum = {max_sum}")
[print(*biggest_matrix[row]) for row in range(3)]