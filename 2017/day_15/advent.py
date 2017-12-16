GEN_A_FACTOR = 16807
GEN_B_FACTOR = 48271

GEN_A_MULTIPLE = 4
GEN_B_MULTIPLE = 8

def calc_next(last, factor, multiple = 0):
    if multiple == 0:
        return (last * factor) % 2147483647
    else:
        while True:
            last = (last * factor) % 2147483647
            if last % multiple == 0:
                break
        return last

def part1(gen_a_last, gen_b_last):
    matches = 0

    for n in range(0, 40000000):
        gen_a_last = calc_next(gen_a_last, GEN_A_FACTOR)
        gen_b_last = calc_next(gen_b_last, GEN_B_FACTOR)

        gen_a_bin = "{0:b}".format(gen_a_last)
        gen_b_bin = "{0:b}".format(gen_b_last)

        if gen_a_bin[-16:] == gen_b_bin[-16:]:
            matches += 1
    print("part1 matches: ", matches)

def part2(gen_a_last, gen_b_last):
    matches = 0

    for n in range(0, 5000000):
        gen_a_last = calc_next(gen_a_last, GEN_A_FACTOR, GEN_A_MULTIPLE)
        gen_b_last = calc_next(gen_b_last, GEN_B_FACTOR, GEN_B_MULTIPLE)

        gen_a_bin = "{0:b}".format(gen_a_last)
        gen_b_bin = "{0:b}".format(gen_b_last)

        if gen_a_bin[-16:] == gen_b_bin[-16:]:
            matches += 1
    print("part2 matches: ", matches)

part1(277, 349)
part2(277, 349)