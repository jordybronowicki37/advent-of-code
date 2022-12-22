file = open("input", "r")

amount = 0

for line in file:
    line = line.replace("\n", "")
    line = line.replace(",", "-")
    split = line.split("-")

    e1s1 = int(split[0])
    e1s2 = int(split[1])
    e2s1 = int(split[2])
    e2s2 = int(split[3])

    if e1s1 <= e2s1 and e1s2 >= e2s2:
        amount += 1
    elif e1s1 >= e2s1 and e1s2 <= e2s2:
        amount += 1

print(amount)
