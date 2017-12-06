class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def taxicab_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def taxicab_from_origin(self):
        return self.taxicab_distance(Point(0, 0))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

DIRECTIONS = {
    "Up":    Point(0, 1),
    "Down":  Point(0, -1),
    "Left":  Point(-1, 0),
    "Right": Point(1, 0),
}

starting_point = Point(0, 0)

commands = []
file = open("directions.txt", "r")
for line in file:
    commands += map(str.strip, line.split(','))
file.close()

furtherest = Point(0, 0)
pos = Point(0, 0)
points = {
    "A": [],
    "B": [],
}
for command in commands:
    if command == "Start":
        break
    elif command in ["A", "B"]:
        points[command] += [pos,]
        if pos.taxicab_from_origin() > furtherest.taxicab_from_origin():
            furtherest = pos
    else:
        pos = pos + DIRECTIONS[command]

print("furtherest from origin: {}, {}".format(furtherest.taxicab_from_origin(), furtherest))

largest = (0, Point(0, 0), Point(0, 0))
for a_point in points["A"]:
    for b_point in points["B"]:
        if a_point.taxicab_distance(b_point) > largest[0]:
            largest = (a_point.taxicab_distance(b_point), a_point, b_point)

print("biggest A -> B distance: {}, A:{}, B:{}".format(largest[0], largest[1], largest[2]))
