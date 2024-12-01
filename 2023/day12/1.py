file = open("input", "r")
answer = 0


def count_batches(spring_group):
    spring_group = list(filter(None, spring_group.split(".")))
    spring_group = [len(a) for a in spring_group]
    return spring_group


for line in file:
    line = line.replace("\n", "").split(" ")
    spring = line[0]
    nums = [int(x) for x in line[1].split(",")]
    all_possible_arrangements = []

    values = [False for _ in range(spring.count("?"))]

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

        for s in spring:
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
    answer += possible_arrangements

print(answer)
