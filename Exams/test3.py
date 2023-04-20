from collections import deque

textiles = deque([int(x) for x in input().split(" ")])
medicaments = deque([int(x) for x in input().split(" ")])

created_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    if textiles and medicaments:
        current_textile = textiles.popleft()
        current_medicament = medicaments.pop()

        result = current_textile + current_medicament

        if result == 30:
            created_items["Patch"] += 1
        elif result == 40:
            created_items["Bandage"] += 1
        elif result >= 100:
            created_items["MedKit"] += 1
            if result > 100:
                result -= 100
                if medicaments:
                    element = medicaments.pop()
                    medicaments.append(element + result)
        else:
            medicaments.append(current_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    if not medicaments:
        print("Medicaments are empty.")

if created_items:
    items_created = {k: v for k, v in sorted(created_items.items(), key=lambda item: (-item[1], item[0]))}
    for item_name, amount_created in items_created.items():
        if amount_created > 0:
            print(f"{item_name} - {amount_created}")

if medicaments:
    print("Medicaments left: " + ', '.join(map(str, medicaments[::-1])))
if textiles:
    print("Textiles left: " + ', '.join(map(str, textiles)))
