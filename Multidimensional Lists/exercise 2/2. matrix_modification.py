size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command = input().split()
    if command[0] == 'END':
        for row in matrix:
            for el in row:
                print(el, end=' ')
            print()
        break
    row = int(command[1])
    col = int(command[2])
    number = int(command[3])
    if row > len(matrix) - 1 or col > len(matrix[row]) or row < 0 or col < 0:
        print("Invalid coordinates")
        continue
    elif command[0] == 'Add':
        matrix[row][col] += number
    elif command[0] == 'Subtract':
        matrix[row][col] -= number

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END