file = open("input", "r")
first = True
trees = 0
lines = 0

for line in file:
    if not first:
        index = (lines * 3) % 31
        if line[index] == '#':
            trees += 1

    first = False
    lines += 1

print(trees)
