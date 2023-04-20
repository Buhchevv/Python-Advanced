size = int(input())

matrix = []
ship_pos = []
ship_taken_damage = 0
destroyed_cruisers = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        ship_pos = [row, matrix[row].index('S')]

while True:
    direction = input()

    matrix[ship_pos[0]][ship_pos[1]] = '-'
    row = ship_pos[0] + directions[direction][0]
    col = ship_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    ship_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = 'S'

    if position == '*':
        ship_taken_damage += 1
        position = '-'
        if ship_taken_damage == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    if position == 'C':
        destroyed_cruisers += 1
        position = '-'
        if destroyed_cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for row in matrix:
    for element in row:
        print(element, end='')
    print()
