from collections import deque


def bomb_creating(effect, casing):
    bombs_created = {}
    materials_table = {
        'Datura Bombs': 40,
        'Cherry Bombs': 60,
        'Smoke Decoy Bombs': 120
    }
    while effect and casing:
        current_effect = effect.popleft()
        current_casing = casing.pop()
        result = current_effect + current_casing
        for bomb, material in materials_table.items():
            if result == material:
                if bomb in bombs_created.keys():
                    bombs_created[bomb] += 1
                bombs_created[bomb] += 1
        if result:
            pass


def print_func():
    pass


bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casing = deque([int(x) for x in input().split(', ')])

bomb_creating(bomb_effect, bomb_casing)
