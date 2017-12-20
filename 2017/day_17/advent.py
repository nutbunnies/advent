import timeit
from collections import deque

STEPS_PER_INSERT = 371

# def print_loop(loop, pos):
#     for n in range(0, len(loop)):
#         if n == pos:
#             print("({}) ".format(loop[n]), end="")
#         else:
#             print("{} ".format(loop[n]), end="")
#     print()

def part1_list():
    pos = 0
    loop = [0]
    # print_loop(loop, pos)
    for n in range(1, 2018):
        pos = ((pos + STEPS_PER_INSERT) % len(loop)) + 1
        loop.insert(pos, n)
        # print_loop(loop, pos)
    return loop[loop.index(2017) + 1]

def part1_deque():
    pos = 0
    loop = deque([0])
    # print_loop(loop, pos)
    for n in range(1, 2019):
        loop.rotate(-STEPS_PER_INSERT)
        loop.append(n)
        # print_loop(loop, pos)
    return loop[loop.index(2017) + 1]

print("timeit list:   ", timeit.timeit(part1_list, number=10000))
print("timeit deque:  ", timeit.timeit(part1_deque, number=10000))

exit(0)

#part 2
pos = 0
for n in range(1, 50000001):
    pos = ((pos + STEPS_PER_INSERT) % n) + 1
    if pos == 1:
        val_in_first_pos = n
print("part 2: ", val_in_first_pos)
