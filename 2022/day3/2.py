file = open("input", "r")

group = []
badges = []
score = 0

for line in file:
    line = line.replace("\n", "")

    group.append(line)

    if len(group) == 3:
        for b in group[0]:
            if b in group[1] and b in group[2]:
                badges.append(b)
                group = []
                break


for i in badges:
    asc = ord(i)

    if 64 < asc < 91:
        score += asc - 38
    elif 96 < asc < 123:
        score += asc - 96

print(score)
