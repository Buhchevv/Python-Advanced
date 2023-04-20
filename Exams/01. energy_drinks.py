from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

max_caffeine = 300
initial_caffeine = 0
stamats_caffeine = 0
result = 0

while milligrams_of_caffeine and energy_drinks:
    mg_caffeine = milligrams_of_caffeine.pop()
    energy_drink = energy_drinks.popleft()

    result = stamats_caffeine
    stamats_caffeine = result + (mg_caffeine * energy_drink)

    if stamats_caffeine > max_caffeine:
        stamats_caffeine = result
        stamats_caffeine -= 30
        if stamats_caffeine < 0:
            stamats_caffeine = 0
        result = stamats_caffeine
        energy_drinks.append(energy_drink)

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")



