import math

class Point(object):
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value

    def taxicab_from_origin(self):
        origin = Point(0, 0)
        return abs(self.x - origin.x) + abs(self.y - origin.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {}) : {}".format(self.x, self.y, self.value)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def spiral(n):
    k = math.ceil((math.sqrt(n) - 1) / 2)
    t = 2 * k + 1
    m = t * t
    t = t - 1

    if (n >= m - t):
        return Point(k - (m - n), -k)
    else:
        m = m - t

    if (n >= m - t):
        return Point(-k, -k + (m - n))
    else:
        m = m - t

    if (n >= m - t):
        return Point(-k + (m - n), k)
    else:
        return Point(k, k - (m - n - t))

print()
print("distance 1: {}, expected: 0".format(spiral(1).taxicab_from_origin()))
print("distance 12: {}, expected: 3".format(spiral(12).taxicab_from_origin()))
print("distance 23: {}, expected: 2".format(spiral(23).taxicab_from_origin()))
print("distance 1024: {}, expected: 31".format(spiral(1024).taxicab_from_origin()))
print("distance 347991: {}, expected: ?".format(spiral(347991).taxicab_from_origin()))
print()

target = 347991
num_coords = [
    Point(0, 0, 1),
]

while num_coords[-1].value < target:
    point = spiral(len(num_coords) + 1)
    # print("point: {}".format(point))
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            dp = point + Point(dx, dy)
            # print("checking: {}".format(dp))
            if dp in num_coords:
                # print("found: {}".format(num_coords[num_coords.index(dp)]))
                point.value += num_coords[num_coords.index(dp)].value
    num_coords.append(point)
    # print("**creating: {}".format(point))
    # print()

print(num_coords[-1])
