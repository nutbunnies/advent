floor = 0
basement_pos = -1

with open('input.txt', 'r') as data:
    commands = data.read()
    for n in range(0, len(commands)):
        if commands[n] == "(":
            floor += 1
        elif commands[n] == ")":
            floor -= 1

        if floor == -1 and basement_pos == -1:
            basement_pos = n

print("final floor: ", floor)
print("first basement position: ", basement_pos + 1)