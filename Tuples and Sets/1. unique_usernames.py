n = int(input())
usernames = set()

for i in range(n):
    username = input()
    usernames.add(username)

for el in usernames:
    print(el)
