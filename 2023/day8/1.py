file = open("input", "r")

instructions = ""
nodes = []
current_node = []
steps = 0


def find_node(node):
    for n in nodes:
        if n[0] == node:
            return n


for line in file:
    line = line.replace("\n", "")

    if instructions == "":
        instructions = line
    elif line == "":
        continue
    else:
        line = line.replace("(", "").replace(")", "").replace(" ", "")
        a = line.split("=")
        b = a[1].split(",")
        c = [a[0], *b]
        if c[0] == "AAA":
            current_node = c
        nodes.append(c)

while True:
    finished = False
    for i in instructions:
        steps += 1
        next_node = ""
        if i == "R":
            next_node = current_node[2]
        else:
            next_node = current_node[1]

        current_node = find_node(next_node)
        if current_node[0] == "ZZZ":
            finished = True
            break

    if finished:
        break

print(steps)
