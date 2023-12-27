file = open("input", "r")

grid = []
route = []
direction = "down"
y = 0
x = 0

for line in file:
    line = line.replace("\n", "")
    if "S" in line:
        y = len(grid)
        x = line.index("S")
    grid.append(line)

while grid[y][x] != "S" or len(route) == 0:
    route.append([y, x])
    pipe = ""
    if direction == "up":
        y -= 1
        pipe = grid[y][x]
        if pipe == "|":
            continue
        elif pipe == "F":
            direction = "right"
        elif pipe == "7":
            direction = "left"

    elif direction == "right":
        x += 1
        pipe = grid[y][x]
        if pipe == "-":
            continue
        elif pipe == "J":
            direction = "up"
        elif pipe == "7":
            direction = "down"

    elif direction == "down":
        y += 1
        pipe = grid[y][x]
        if pipe == "|":
            continue
        elif pipe == "L":
            direction = "right"
        elif pipe == "J":
            direction = "left"

    elif direction == "left":
        x -= 1
        pipe = grid[y][x]
        if pipe == "-":
            continue
        elif pipe == "F":
            direction = "down"
        elif pipe == "L":
            direction = "up"

print(len(route) / 2)
