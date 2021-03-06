from functools import reduce
import math

input_lengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
input_arry = list(range(0, 256))

# input_lengths = [3, 4, 1, 5]
# input_arry = [0, 1, 2, 3, 4]

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
    hsh = knot_hash(64, list(range(0, 256)), convert_lengths(list(val)))
    hsh_ord = []
    for n in range(0, 256, 16):
        hsh_ord.append(reduce(lambda i, j: i ^ j, hsh[n:n+16]))
    # print(part2_xord)
    return "".join(list(map(lambda x: "%0.2x" % x, hsh_ord)))

# arry = knot_hash(1, input_arry.copy(), input_lengths.copy())
# # print("after: ", arry)
# print("checksum: ", arry[0] * arry[1])

# part2_arry = knot_hash(64, input_arry.copy(), convert_lengths(input_lengths.copy()))
# # print(part2_arry)
# # print("----")

# part2_xord = []
# for n in range(0, 256, 16):
#     part2_xord.append(reduce(lambda i, j: i ^ j, part2_arry[n:n+16]))
# # print(part2_xord)
# print("".join(list(map(lambda x: "%0.2x" % x, part2_xord))))

# print(hex_knot_hash(input_lengths.copy()))
print()
print(hex_knot_hash(map(ord, list(""))))
print("a2582a3a0e66e6e86e3812dcb672a272")
print()
print(hex_knot_hash("AoC 2017"))
print("33efeb34ea91902bb2f59c9920caa6cd")
