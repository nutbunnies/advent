input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
# input = "0  2   7   0"

banks = list(map(int, input.split()))

history = []

while banks not in history:
    history.append(banks.copy())

    pos = banks.index(max(banks))
    distibute_val = banks[pos]
    banks[pos] = 0
    while distibute_val > 0:
        pos += 1
        if pos >= len(banks):
            pos = pos - len(banks)
        banks[pos] += 1
        distibute_val -= 1

print("loop detected at: {}".format(len(history)))
last_answer = len(history)

goal = banks.copy()
history.append(banks.copy())
current_count = history.count(goal)

while history.count(goal) < (current_count + 2):
    history.append(banks.copy())

    pos = banks.index(max(banks))
    distibute_val = banks[pos]
    banks[pos] = 0
    while distibute_val > 0:
        pos += 1
        if pos >= len(banks):
            pos = pos - len(banks)
        banks[pos] += 1
        distibute_val -= 1

print("last loop detected at: {}".format(len(history) - last_answer - 2))