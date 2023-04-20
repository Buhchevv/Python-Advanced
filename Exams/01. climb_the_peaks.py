textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))

healing_items = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}
created_items = {}

while textiles and medicaments:
    textile = textiles.pop(0)
    medicament = medicaments.pop()

    if textile + medicament in healing_items.values():
        for item, cost in healing_items.items():
            if cost == textile + medicament:
                if item in created_items:
                    created_items[item] += 1
                else:
                    created_items[item] = 1
                break
    elif textile + medicament > healing_items['MedKit']:
        if 'MedKit' in created_items:
            created_items['MedKit'] += 1
        else:
            created_items['MedKit'] = 1
        remaining = textile + medicament - healing_items['MedKit']
        while medicaments and medicaments[-1] < remaining:
            remaining -= medicaments.pop()
        if medicaments:
            medicaments[-1] += remaining
    else:
        medicaments[-1] += 10

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item in sorted(created_items, key=lambda x: (-created_items[x], x)):
    print(f"{item} - {created_items[item]}")

if medicaments:
    print("Medicaments left:", ", ".join(str(x) for x in reversed(medicaments)))
if textiles:
    print("Textiles left:", ", ".join(str(x) for x in textiles))
