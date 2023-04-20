size = 6
matrix = [input().split() for _ in range(size)]
start_position = list(map(int, input().strip("(").strip(")").split(", ")))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break
    row = directions[command[1]][0] + start_position[0]
    col = directions[command[1]][1] + start_position[1]

    if not (0 <= row < size and 0 <= col < size):
        break
    position = matrix[row][col]
    start_position = [row, col]

    if command[0] == 'Create':
        value = command[2]
        if position == '.':
            matrix[row][col] = value
        else:
            continue

    elif command[0] == 'Update':
        value = command[2]
        if position.isalnum():
            matrix[row][col] = value
        else:
            continue

    elif command[0] == 'Read':
        if position.isalnum():
            print(position)
        else:
            continue
    elif command[0] == 'Delete':
        if position.isalnum():
            matrix[row][col] = '.'
            start_position = [row, col]
        else:
            continue

for row in matrix:
    print(' '.join(row))