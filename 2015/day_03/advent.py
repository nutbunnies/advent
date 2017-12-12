from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

commands = []
with open('input.txt', 'r') as data:
    for command in data.read().strip():
        commands.append(command)


def visited(commands, visited):
    pos = Point(0, 0)
    visited.add(pos)
    for command in commands:
        if command == ">":
            pos = Point(pos.x + 1, pos.y)
        elif command == "<":
            pos = Point(pos.x - 1, pos.y)
        elif command == "^":
            pos = Point(pos.x, pos.y + 1)
        elif command == "v":
            pos = Point(pos.x, pos.y - 1)
        else:
            print("WTF: can't handle: ", command)
        visited.add(pos)
    return visited


print("total house visited: ", len(visited(commands, set())))

# commands = "^v^v^v^v^v"
robovisited = visited(commands[::2], set())
bothvisited = visited(commands[1::2], robovisited)
print("robosanta + normalsanta visited: ", len(bothvisited))
