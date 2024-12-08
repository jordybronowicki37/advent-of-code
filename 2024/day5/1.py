file = open("input", "r")

answer = 0
rules = []
has_read_rules = False

for line in file:
    line = line.replace("\n", "")

    if line == "":
        has_read_rules = True
        continue

    if not has_read_rules:
        ruleSplit = line.split("|")
        rules.append([int(ruleSplit[0]), int(ruleSplit[1])])
        continue

    update = [int(a) for a in line.split(",")]
    update_failed = False
    for i in range(len(update)):
        if update_failed:
            break
        page = update[i]
        pre_page = update[:i]
        for rule in rules:
            if rule[0] == page and rule[1] in pre_page:
                update_failed = True
                break

    if not update_failed:
        answer += update[int((len(update)-1) / 2)]

print(answer)
