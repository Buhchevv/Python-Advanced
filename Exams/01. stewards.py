from collections import deque
seats = input().split(", ")
first_numbers = deque(map(int, input().split(", ")))
second_numbers = deque(map(int, input().split(", ")))

rotations = 0
founded_seats = 0
matched_seats = []

while True:
    if rotations == 10 or founded_seats == 3:
        break
    if first_numbers and second_numbers:
        current_first_num = first_numbers.popleft()
        current_second_num = second_numbers.pop()
        result = current_first_num + current_second_num
        first_num_concate = str(current_first_num) + chr(result)
        second_num_concate = str(current_second_num) + chr(result)
        for seat in [first_num_concate, second_num_concate]:
            if seat in matched_seats:
                break
            if seat in seats:
                seats.remove(seat)
                matched_seats.append(seat)
                founded_seats += 1
                break
        else:
            first_numbers.append(current_first_num)
            second_numbers.appendleft(current_second_num)
        rotations += 1

print(f"Seat matches: {', '.join(str(x) for x in matched_seats)}")

print(f"Rotations count: {rotations}")


