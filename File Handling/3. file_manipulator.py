import os

while True:
    command, *data = input().split("-")

    if command == "Create":
        file = open(f"C:/Users/Antonio/Python Advanced/files/{data[0]}", "w")
        file.close() 
    elif command == "Add":
        with open(f"C:/Users/Antonio/Python Advanced/files/{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")
    elif command == "Replace":
        try:
            with open(f"C:/Users/Antonio/Python Advanced/files/{data[0]}", "r") as file:
                text = file.read()

            text = text.replace(data[1], data[2])

            with open(f"C:/Users/Antonio/Python Advanced/files/{data[0]}", "w") as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"C:/Users/Antonio/Python Advanced/files/{data[0]}")
        except FileNotFoundError:
            print("An error occurred!")
    elif command == "End":
        break
