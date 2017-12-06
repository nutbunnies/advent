correct = 0
file = open("input.txt", "r")
for line in file:
    passphrase = map(str.strip, line.split())
    list_pass = list(passphrase)
    set_pass = set(list_pass)

    if len(list_pass) == len(set_pass):
        correct += 1
file.close()

print("correct: {}".format(correct))
print()


correct = 0
file = open("input.txt", "r")
for line in file:
    passphrase = map(lambda s: "".join(sorted(s.strip())), line.split())

    list_pass = list(passphrase)
    set_pass = set(list_pass)

    if len(list_pass) == len(set_pass):
        correct += 1
file.close()

print("correct: {}".format(correct))