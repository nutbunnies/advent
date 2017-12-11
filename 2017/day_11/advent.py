input = ""
file = open("input.txt", "r")
for line in file:
    input += line
file.close()
input = input.strip()

class HexNode(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return HexNode(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def distance(self, other):
        return (abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)) / 2

    def move(self, direction):
        return {
            "se": HexNode(+1, -1,  0),
            "ne": HexNode(+1,  0, -1),
            "n": HexNode( 0, +1, -1),
            "nw": HexNode(-1, +1,  0),
            "sw": HexNode(-1,  0, +1),
            "s": HexNode( 0, -1, +1),
        }[direction] + self

node = HexNode(0, 0, 0)
max_distance = 0
for movement in input.split(","):
    node = node.move(movement)
    max_distance = max(node.distance(HexNode(0, 0, 0)), max_distance)

distance = node.distance(HexNode(0, 0, 0))
print("distance: {}".format(distance))
print("max distance: {}".format(max_distance))
