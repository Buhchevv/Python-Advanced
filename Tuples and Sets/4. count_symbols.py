text = input()
occurrences = {}
counter = 0

for el in text:
    if el not in occurrences:
        occurrences[el] = 0
        occurrences[el] += 1
    elif el in occurrences:
        occurrences[el] += 1

for k, v in sorted(occurrences.items()):
    print(f"{k}: {v} time/s")