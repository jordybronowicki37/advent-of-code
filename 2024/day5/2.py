file = open("input", "r")

answer = 0
rules = []
has_read_rules = False


def check_update(update):
    global rules
    for i in range(len(update)):
        page = update[i]
        pre_page = update[:i]
        for rule in rules:
            if rule[0] == page and rule[1] in pre_page:
                return False
    return True


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
    update_failed = not check_update(update)

    if update_failed:
        while not check_update(update):
            for i in range(len(update)):
                page = update[i]
                pre_page = update[:i]
                for j in range(len(rules)):
                    rule = rules[j]
                    if rule[0] == page and rule[1] in pre_page:
                        k = pre_page.index(rule[1])
                        update[k] = rule[0]
                        update[i] = rule[1]
                        break

    if update_failed:
        answer += update[int((len(update)-1) / 2)]

print(answer)
