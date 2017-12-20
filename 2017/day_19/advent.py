from collections import namedtuple

maze = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+""".splitlines()

with open("input.txt") as file:
    maze = file.read().splitlines()

Point = namedtuple('Point', ['x', 'y'])
Runner = namedtuple('Runner', ['position', 'direction'])

def get_value(point, maze):
    if point.x < 0 or point.y < 0:
        return ""
    try:
        return maze[point.y][point.x]
    except:
        return ""

starting_point = Point(maze[0].index("|"), 0)
maze_runner = Runner(starting_point, 'D')
captured_letters = []

count = 1
while True:
    if maze_runner.direction == 'D':
        new_position = Point(maze_runner.position.x, maze_runner.position.y + 1)
    elif maze_runner.direction == 'U':
        new_position = Point(maze_runner.position.x, maze_runner.position.y - 1)
    elif maze_runner.direction == 'L':
        new_position = Point(maze_runner.position.x - 1, maze_runner.position.y)
    elif maze_runner.direction == 'R':
        new_position = Point(maze_runner.position.x + 1, maze_runner.position.y)

    path = get_value(new_position, maze)

    new_direction = maze_runner.direction
    if path == "+":
        if maze_runner.direction in ['U', 'D']:
            if not get_value(Point(new_position.x + 1, new_position.y), maze) in ["", " "]:
                new_direction = 'R'
            else:
                new_direction = 'L'
        else:
            if not get_value(Point(new_position.x, new_position.y + 1), maze) in ["", " "]:
                new_direction = 'D'
            else:
                new_direction = 'U'
    elif path.isalpha():
        captured_letters.append(path)
    elif path in ["", " "]:
        print("Letterpath: ", "".join(captured_letters))
        print("Count:      ", count)
        break

    maze_runner = Runner(new_position, new_direction)
    count += 1

