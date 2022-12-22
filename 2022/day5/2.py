file = open("input", "r")

doneLoadingLayout = False
stacks = [[] for _ in range(9)]
instructions = []

for line in file:
    line = line.replace("\n", "")

    if not doneLoadingLayout:
        if line == "":
            doneLoadingLayout = True
            continue

        for i in range(len(line)):
            if line[i] == " " or line[i] == "[" or line[i] == "]" or line[i].isdigit():
                continue

            stackNum = (i - 1) // 4
            stacks[stackNum].append(line[i])
        continue

    line = line.replace(" ", "")
    line = line.replace("move", "")
    line = line.replace("from", "-")
    line = line.replace("to", "-")
    instructions.append(line)

for stack in stacks:
    stack.reverse()

for instr in instructions:
    split = instr.split("-")
    amount = int(split[0])
    frm = int(split[1]) - 1
    to = int(split[2]) - 1

    crates = stacks[frm][-amount:]
    stacks[frm] = stacks[frm][:-amount]
    stacks[to].extend(crates)

print("".join([j[-1] for j in stacks]))
