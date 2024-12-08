file = open("input", "r")

valid_placements = 0
guard_starting = []
obstructions = []
width = 0
height = 0

for line in file:
    line = line.replace("\n", "")
    width = len(line)
    for j in range(len(line)):
        if line[j] == "#":
            obstructions.append((height, j))
        if line[j] == "^":
            guard_starting = (height, j)
    height += 1


obstructions = tuple(obstructions)


def check_for_loops(obstructions):
    global guard_starting

    guard = guard_starting
    facing = "north"
    visited = set()

    while True:
        if facing == "north":
            item = None
            rel_obs = filter(lambda pos: pos[1] == guard[1] and pos[0] < guard[0], obstructions)
            for rel_ob in rel_obs:
                if not item or item[0] < rel_ob[0]:
                    item = rel_ob
            if not item:
                # draw to border
                return False
            # draw to obs
            for i in range(guard[0], item[0], -1):
                visit = (i, guard[1], facing)
                if visit in visited:
                    return True
                visited.add(visit)
                guard = [i, guard[1]]
            facing = "east"

        if facing == "east":
            item = None
            rel_obs = filter(lambda pos: pos[0] == guard[0] and pos[1] > guard[1], obstructions)
            for rel_ob in rel_obs:
                if not item or item[1] > rel_ob[1]:
                    item = rel_ob
            if not item:
                # draw to border
                return False
            # draw to obs
            for i in range(guard[1], item[1]):
                visit = (guard[0], i, facing)
                if visit in visited:
                    return True
                visited.add(visit)
                guard = [guard[0], i]
            facing = "south"

        if facing == "south":
            item = None
            rel_obs = filter(lambda pos: pos[1] == guard[1] and pos[0] > guard[0], obstructions)
            for rel_ob in rel_obs:
                if not item or item[0] > rel_ob[0]:
                    item = rel_ob
            if not item:
                # draw to border
                return False
            # draw to obs
            for i in range(guard[0], item[0]):
                visit = (i, guard[1], facing)
                if visit in visited:
                    return True
                visited.add(visit)
                guard = [i, guard[1]]
            facing = "west"

        if facing == "west":
            item = None
            rel_obs = filter(lambda pos: pos[0] == guard[0] and pos[1] < guard[1], obstructions)
            for rel_ob in rel_obs:
                if not item or item[1] < rel_ob[1]:
                    item = rel_ob
            if not item:
                # draw to border
                return False
            # draw to obs
            for i in range(guard[1], item[1], -1):
                visit = (guard[0], i, facing)
                if visit in visited:
                    return True
                visited.add(visit)
                guard = [guard[0], i]
            facing = "north"


for y in range(height):
    for x in range(width):
        new_obs = (y, x)
        if new_obs in obstructions:
            continue

        new_obstructions = tuple([*obstructions, new_obs])
        if check_for_loops(new_obstructions):
            valid_placements += 1

print(valid_placements)
