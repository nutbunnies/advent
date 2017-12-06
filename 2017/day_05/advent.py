commands = []
file = open("input.txt", "r")
for line in file:
    commands.append(int(line.strip()))
file.close()

commands = [0, 3, 0, 1, -3]

jump_ct = 0
pos = 0
while True:
    jump_ct += 1
    offset = commands[pos]

    #part 2
    if offset >= 3:
        commands[pos] -= 1
    else:
        commands[pos] += 1

    #part 1
    # commands[pos] += 1

    pos = pos + offset
    if pos >= len(commands) or pos < 0:
        break

print("jump count: {}".format(jump_ct))
