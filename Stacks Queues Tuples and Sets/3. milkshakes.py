from collections import deque

chocolates = deque([int(x) for x in input().split(', ')])
cups_of_milk = deque([int(x) for x in input().split(', ')])
chocolate_milkshakes = 0

while True:
    if chocolate_milkshakes == 5 or not chocolates or not cups_of_milk:
        break
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop()
        cups_of_milk.popleft()
        chocolate_milkshakes += 1
    else:
        reverse_cup = cups_of_milk.popleft()
        cups_of_milk.append(reverse_cup)
        reverse_cup = 0
        chocolates[-1] -= 5
if chocolate_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
