from collections import namedtuple
from collections import defaultdict

input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

input = ""
file = open("input.txt", "r")
for line in file:
    input += line
file.close()
input = input.strip()

Command = namedtuple('Command', ['register', 'direction', 'amount', 'condition_register', 'condition', 'condition_value'])

commands = []
for line in input.split("\n"):
    parts = line.split()
    commands.append(Command(parts[0], parts[1], int(parts[2]), parts[4], parts[5], int(parts[6])))

registers = defaultdict(int)
highest_val = 0

for command in commands:
    validation = "{} {} {}".format(registers[command.condition_register], command.condition, command.condition_value)
    if eval(validation):
        if command.direction == 'inc':
            registers[command.register] += command.amount
        elif command.direction == 'dec':
            registers[command.register] -= command.amount
        else:
            print("UNKNOWN: {}".format(command.direction))

        if registers[command.register] > highest_val:
            highest_val = registers[command.register]

print(registers)
max_val = 0
## TODO research better way to get value iter from defaultdict so max() works
for item in registers.items():
    if item[1] > max_val:
        max_val = item[1]

print(max_val)
print(highest_val)