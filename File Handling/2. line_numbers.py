from string import punctuation

with open("C:/Users/Antonio/Python Advanced/files/text.txt", "r") as text_file:
    text = text_file.readlines()

output_file = open("C:/Users/Antonio/Python Advanced/files/text.txt", "w")

for i in range(len(text)):
    row = text[i]

    letters = 0
    marks = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i + 1}: {''.join(row[:-1])} ({letters})({marks})\n")


output_file.close()