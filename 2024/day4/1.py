file = open("input", "r")

words = ["XMAS", "SAMX"]
lines = []
amount = 0

for line in file:
    line = line.replace("\n", "")
    lines.append(line)

height = len(lines)
width = len(lines[0])

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        # Horizontal
        if width - x >= 4:
            if line[x:x + 4] in words:
                amount += 1
        # Vertical
        if height - y >= 4:
            vertical = "".join([a[x] for a in lines[y:y + 4]])
            if vertical in words:
                amount += 1
        # Diagonal right
        if width - x >= 4 and height - y >= 4:
            verticalRight = ""
            for l in range(4):
                verticalRight += lines[y+l][x+l]
            if verticalRight in words:
                amount += 1
        # Diagonal left
        if x >= 3 and height - y >= 4:
            verticalLeft = ""
            for l in range(4):
                verticalLeft += lines[y+l][x-l]
            if verticalLeft in words:
                amount += 1

print(amount)
