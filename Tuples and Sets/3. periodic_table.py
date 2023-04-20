number_of_elements = int(input())
set1 = set()
for _ in range(number_of_elements):
    for el in input().split():
        set1.add(el)

print(*set1, sep='\n')
# 4
# Ce O
# Mo O Ce
# Ee
# Mo