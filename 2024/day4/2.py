file = open("input", "r")

words = ["MAS", "SAM"]
lines = []
amount = 0

for line in file:
    line = line.replace("\n", "")
    lines.append(line)

height = len(lines)
width = len(lines[0])

for y in range(len(lines)):
    line = lines[y]
    if y == height - 2:
        break
    for x in range(len(line)):
        if x == width - 2:
            break


        # Diagonal right
        rightActive = False
        verticalRight = ""
        for l in range(3):
            verticalRight += lines[y+l][x+l]
        if verticalRight in words:
            rightActive = True
        # Diagonal left
        leftActive = False
        verticalLeft = ""
        for l in range(3):
            verticalLeft += lines[y+l][x+2-l]
        if verticalLeft in words:
            leftActive = True

        if leftActive and rightActive:
            amount += 1

print(amount)
