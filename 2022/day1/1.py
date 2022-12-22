file = open("input", "r")
elfInventories = [0]
currentElf = 0

for line in file:
    line = line.replace("\n", "")

    if line == "":
        currentElf += 1
        elfInventories.append(0)
        continue

    elfInventories[currentElf] += int(line)

print(max(elfInventories))
