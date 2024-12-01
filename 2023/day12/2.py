# DOES NOT WORK!

file = open("input", "r")
answer = 0


def count_batches(spring_group):
    spring_group = list(filter(None, spring_group.split(".")))
    spring_group = [len(a) for a in spring_group]
    return spring_group


for li, line in enumerate(file):
    if li % 10 == 0:
        print(f"\r{li/10}%", end="")

    line = line.replace("\n", "").split(" ")
    spring = line[0]
    springs = [spring, f"?{spring}", f"{spring}?"]
    nums = [int(x) for x in line[1].split(",")]
    all_arrangements = []

    for sp in springs:
        values = [False for _ in range(sp.count("?"))]

        first_iteration = True
        possible_arrangements = 0
        while False in values:
            if not first_iteration:
                if not values[0]:
                    values[0] = True
                else:
                    values[0] = False

                    for v2_i, v2 in enumerate(values[1::]):
                        if not v2:
                            values[v2_i+1] = True
                            break
                        values[v2_i+1] = False
            else:
                first_iteration = False

            possible_springs = ""
            unknown_index = 0

            for s in sp:
                if s == "?":
                    if values[unknown_index]:
                        possible_springs += "#"
                    else:
                        possible_springs += "."
                    unknown_index += 1
                else:
                    possible_springs += s

            if nums == count_batches(possible_springs):
                possible_arrangements += 1
        all_arrangements.append(possible_arrangements)

    total_arrangements = 0
    if all_arrangements[0] == 1 and spring[0] in "?#" and spring[-1] in "?#":
        total_arrangements = 1
    elif all_arrangements[0] == all_arrangements[1]:
        total_arrangements = pow(all_arrangements[2], 4)
        total_arrangements *= all_arrangements[0]
    elif all_arrangements[0] == all_arrangements[2]:
        total_arrangements = pow(all_arrangements[1], 4)
        total_arrangements *= all_arrangements[0]
    else:
        if all_arrangements[1] > all_arrangements[2]:
            total_arrangements = pow(all_arrangements[1], 4)
            total_arrangements *= all_arrangements[2]
        else:
            total_arrangements = pow(all_arrangements[2], 4)
            total_arrangements *= all_arrangements[1]
    answer += total_arrangements

print(answer)
