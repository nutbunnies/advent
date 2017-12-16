from functools import reduce
import math

def knot_hash(iterations, arry, lengths):
    skip_size = 0
    current_pos = 0
    arry_len = len(arry)

    for times in range(0, iterations):
        for length in lengths:
            for n in range(0, math.floor(length / 2)):
                swap_a = (n + current_pos) % arry_len
                swap_b = (current_pos + length - n - 1) % arry_len

                a = arry[swap_a]
                b = arry[swap_b]
                arry[swap_b] = a
                arry[swap_a] = b

            current_pos += length + skip_size
            if current_pos > len(arry):
                current_pos = current_pos % len(arry)
            skip_size += 1
    return arry

def convert_lengths(lst):
    return list(map(ord, list(map(str, lst)))) + [17, 31, 73, 47, 23]

def hex_knot_hash(val):
    hsh = knot_hash(64, list(range(0, 256)), convert_lengths(val))
    hsh_ord = []
    for n in range(0, 256, 16):
        hsh_ord.append(reduce(lambda i, j: i ^ j, hsh[n:n+16]))
    return "".join(list(map(lambda x: "%0.2x" % x, hsh_ord)))

total = 0
grid = []
for n in range(0, 128):
    # hsh = hex_knot_hash("flqrgnkx-{}".format(n))
    hsh = hex_knot_hash("vbqugkhl-{}".format(n))
    bin_rep = bin(int(hsh, 16))[2:]
    grid.append(list(map(int, list("{:>0128}".format(bin_rep)))))
    total += sum(map(int, list(bin_rep)))

print("total: ", total)

def get_value(x, y):
    if x < 0 or y < 0:
        return 0
    try:
        return grid[y][x]
    except:
        return 0

def mark_neighbors(x, y, val):
    if get_value(x, y) == 1:
        grid[y][x] = val
        for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            mark_neighbors(dx, dy, val)

groups = set()
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == 1:
            groups.add((x,y))
            mark_neighbors(x, y, (x,y))

print("group count: ", len(groups))
