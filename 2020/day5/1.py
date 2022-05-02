file = open("1input", "r")
highest = 0


def getRow(value):
    value = value.replace("F", "0").replace("B", "1")
    return int(value, 2)


def getSeat(value):
    value = value.replace("L", "0").replace("R", "1")
    return int(value, 2)


for line in file:
    row = getRow(line[:7])
    seat = getSeat(line[7:])
    id = (row * 8) + seat
    if id > highest:
        highest = id

print(highest)
