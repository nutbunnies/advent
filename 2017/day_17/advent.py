STEPS_PER_INSERT = 371

def print_loop(loop, pos):
    for n in range(0, len(loop)):
        if n == pos:
            print("({}) ".format(loop[n]), end="")
        else:
            print("{} ".format(loop[n]), end="")
    print()

pos = 0
loop = [0]
# print_loop(loop, pos)
for n in range(1, 2018):
    pos = ((pos + STEPS_PER_INSERT) % len(loop)) + 1
    loop.insert(pos, n)
    # print_loop(loop, pos)

print("part 1: ", loop[loop.index(2017) + 1])

#part 2
pos = 0
for n in range(1, 50000001):
    pos = ((pos + STEPS_PER_INSERT) % n) + 1
    if pos == 1:
        val_in_first_pos = n
print("part 2: ", val_in_first_pos)
