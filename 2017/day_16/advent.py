from datetime import datetime

DANCER_SIZE = 16
dancers = [chr(n) for n in range(97, 97+DANCER_SIZE)]

with open("input.txt") as file:
    commands = file.read().strip().split(",")

def run_commands(commands, dancers):
    for command in commands:
        if command[0] == 's':
            i = int("".join(command[1:]))
            dancers = dancers[-i:] + dancers[0:(DANCER_SIZE - i)]
        elif command[0] == 'x':
            pos = command[1:].split("/")
            a = int(pos[0])
            b = int(pos[1])
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif command[0] == 'p':
            pos = command[1:].split("/")
            a = dancers.index(pos[0])
            b = dancers.index(pos[1])
            dancers[a], dancers[b] = dancers[b], dancers[a]
        # print("command: {:>8s}, status: {}".format(command, dancers))
    return dancers

def iterate(commands, dancers, ct):
    seen = []
    for n in range(0, ct):
        if "".join(dancers) in seen:
            return seen[ct % n]
        seen.append("".join(dancers))
        dancers = run_commands(commands, dancers)
    return "".join(dancers)

print("part1: ", "".join(run_commands(commands, dancers[:])))
print("part2: ", iterate(commands, dancers[:], 1_000_000_000))
