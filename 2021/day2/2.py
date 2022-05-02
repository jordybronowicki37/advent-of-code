file = open("2input", "r")
depth = 0
forward = 0
aim = 0

for line in file:
    split = line.split(" ")

    if split[0] == "forward":
        forward += int(split[1])
        depth += aim*int(split[1])
    elif split[0] == "down":
        aim += int(split[1])
    elif split[0] == "up":
        aim -= int(split[1])

print(depth*forward)
