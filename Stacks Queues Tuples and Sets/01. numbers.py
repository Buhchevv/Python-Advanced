set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

functions = {
    "Add First": lambda x: [set1.add(el) for el in x],
    "Remove First": lambda x: [set1.discard(el) for el in x],
    "Add Second": lambda x: [set2.add(el) for el in x],
    "Remove Second": lambda x: [set2.discard(el) for el in x],
    "Check Subset": lambda: print(True) if set1.issubset(set2) or set2.issubset(set1) else print(False),
}

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if data:
        functions[command](int(x) for x in data)
    else:
        functions[command]()
print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')



# Example Inputs 

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
