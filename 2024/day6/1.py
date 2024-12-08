file = open("input", "r")

guard = []
facing = "north"
visited = set()
obstructions = []
width = 0
height = 0

for line in file:
    line = line.replace("\n", "")
    width = len(line)
    for j in range(len(line)):
        if line[j] == "#":
            obstructions.append([height, j])
        if line[j] == "^":
            guard = [height, j]
    height += 1

while True:
    item = None
    if facing == "north":
        facing = "east"
        rel_obs = filter(lambda pos: pos[1] == guard[1] and pos[0] < guard[0], obstructions)
        for rel_ob in rel_obs:
            if not item or item[0] < rel_ob[0]:
                item = rel_ob
        if not item:
            # draw to border
            for i in range(guard[0], -1, -1):
                visited.add((i, guard[1]))
            break
        # draw to obs
        for i in range(guard[0], item[0], -1):
            visited.add((i, guard[1]))
            guard = [i, guard[1]]

    elif facing == "east":
        facing = "south"
        rel_obs = filter(lambda pos: pos[0] == guard[0] and pos[1] > guard[1], obstructions)
        for rel_ob in rel_obs:
            if not item or item[1] > rel_ob[1]:
                item = rel_ob
        if not item:
            # draw to border
            for i in range(guard[1], width):
                visited.add((guard[0], i))
            break
        # draw to obs
        for i in range(guard[1], item[1]):
            visited.add((guard[0], i))
            guard = [guard[0], i]

    elif facing == "south":
        facing = "west"
        rel_obs = filter(lambda pos: pos[1] == guard[1] and pos[0] > guard[0], obstructions)
        for rel_ob in rel_obs:
            if not item or item[0] > rel_ob[0]:
                item = rel_ob
        if not item:
            # draw to border
            for i in range(guard[0], height):
                visited.add((i, guard[1]))
            break
        # draw to obs
        for i in range(guard[0], item[0]):
            visited.add((i, guard[1]))
            guard = [i, guard[1]]

    elif facing == "west":
        facing = "north"
        rel_obs = filter(lambda pos: pos[0] == guard[0] and pos[1] < guard[1], obstructions)
        for rel_ob in rel_obs:
            if not item or item[1] < rel_ob[1]:
                item = rel_ob
        if not item:
            # draw to border
            for i in range(guard[1], -1, -1):
                visited.add((guard[0], i))
            break
        # draw to obs
        for i in range(guard[1], item[1], -1):
            visited.add((guard[0], i))
            guard = [guard[0], i]

print(len(visited))
