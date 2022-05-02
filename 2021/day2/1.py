file = open("1input", "r")
depth = 0
forward = 0

for line in file:
    split = line.split(" ")

    if split[0] == "forward":
        forward += int(split[1])
    elif split[0] == "down":
        depth += int(split[1])
    elif split[0] == "up":
        depth -= int(split[1])

print(depth*forward)
