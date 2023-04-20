size = int(input())
racing_number = input()

matrix = []
car_position = [0, 0]
km_passed = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        break
    row = car_position[0] + directions[command][0]
    col = car_position[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    car_position = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '.'

    if position == '.' or position == 'F':
        km_passed += 10
        if position == 'F':
            print(f"Racing car {racing_number} finished the stage!")
            break

    elif position == 'T':
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 'T':
                    car_position = [i, j]
                    matrix[i][j] = '.'
                    km_passed += 30

print(f"Distance covered {km_passed} km.")
matrix[car_position[0]][car_position[1]] = 'C'
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
