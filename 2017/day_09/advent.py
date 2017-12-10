import re

input = ""
file = open("input.txt", "r")
for line in file:
    input += line
file.close()
input = input.strip()

inputs = [
    (r"{}", 1),
    (r"{{{}}}", 6),
    (r"{{},{}}", 5),
    (r"{{{},{},{{}}}}", 16),
    (r"{<a>,<a>,<a>,<a>}", 1),
    (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
]

GARBAGE_START = "<"
GARBAGE_END = ">"
def remove_garbage(str):
    garbage_removed = 0
    in_garbage = False
    cleaned_str = ""
    for i in range(0, len(str)):
        if in_garbage and str[i] == GARBAGE_END:
            in_garbage = False
        elif not in_garbage and str[i] == GARBAGE_START:
            in_garbage = True
        elif not in_garbage:
            cleaned_str += str[i]
        elif in_garbage:
            garbage_removed += 1

    print("total garbage: ", garbage_removed)
    return cleaned_str

GROUP_START = "{"
GROUP_END = "}"
def count_depth(str):
    total = 0
    current_depth_val = 0
    for i in range(0, len(str)):
        if str[i] == GROUP_START:
            current_depth_val += 1
        elif str[i] == GROUP_END:
            total += current_depth_val
            current_depth_val -= 1
    return total

for test in inputs:
    minus_bangs = re.sub(r"\!.", "", test[0])
    minus_garbage = remove_garbage(minus_bangs)
    minus_commas = re.sub(r",", "", minus_garbage)
    # print(test[0])
    # print(minus_garbage)
    # print(minus_commas)
    print("{} should be {}".format(count_depth(minus_commas), test[1]))
    print()


print("------")

input_without_bangs = re.sub(r"\!.", "", input)
input_without_garbage = remove_garbage(input_without_bangs)
input_without_commas = re.sub(r",", "", input_without_garbage)
print("nest value: ", count_depth(input_without_commas))

