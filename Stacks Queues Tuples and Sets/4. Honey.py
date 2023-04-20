from collections import deque


def calculate_honey(bee, operator, nectar):
    collected_nectar = 0
    if operator == '+':
        collected_nectar = bee + nectar
    elif operator == '-':
        collected_nectar = bee - nectar
    elif operator == '/':
        if bee == 0 or nectar == 0:
            exit()
        else:
            collected_nectar = bee / nectar
    elif operator == '*':
        collected_nectar = bee * nectar

    return abs(collected_nectar)


working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        first_operator = symbols.popleft()
        if first_operator == '/' and last_nectar == 0:
            continue
        total_honey += calculate_honey(first_bee, first_operator, last_nectar)
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")