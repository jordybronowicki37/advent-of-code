import math

file = open("input", "r")

items = []
score = 0

for line in file:
    line = line.replace("\n", "")

    halfLen = math.floor(len(line)/2)

    ruck1 = line[:halfLen]
    ruck2 = line[halfLen:]

    for item in ruck1:
        if item in ruck2:
            items.append(item)
            break

for i in items:
    asc = ord(i)

    if 64 < asc < 91:
        score += asc - 38
    elif 96 < asc < 123:
        score += asc - 96

print(score)
