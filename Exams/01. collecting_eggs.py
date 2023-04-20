from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
piece_of_paper = deque([int(x) for x in input().split(', ')])

BOX_SIZE = 50
filled_boxes = 0

while eggs and piece_of_paper:
    current_egg = eggs.popleft()
    current_piece_of_paper = piece_of_paper.pop()
    current_size = current_egg + current_piece_of_paper

    if current_egg <= 0:
        piece_of_paper.append(current_piece_of_paper)
    elif current_egg == 13:
        swapped_paper = piece_of_paper.popleft()
        piece_of_paper.append(swapped_paper)
        piece_of_paper.appendleft(current_piece_of_paper)
    elif current_size <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in piece_of_paper)}")