# DOES NOT WORK, yet
file = open("input", "r")

instructions = ""
nodes = []
start_nodes = []

class Node:
    def __init__(self, values):
        self.n = values[0]
        self.l = values[1]
        self.r = values[2]


def find_node(v):
    for n in nodes:
        if n.n == v:
            return n


def check_node_finished(node):
    if node.n[2] != "Z":
        return False
    return True


for line in file:
    line = line.replace("\n", "")

    if instructions == "":
        instructions = line
    elif line == "":
        continue
    else:
        line = line.replace("(", "").replace(")", "").replace(",", "").replace("=", "").replace("  ", " ").split(" ")
        nn = Node(line)
        if line[0][2] == "A":
            start_nodes.append(nn)
        nodes.append(nn)

for nc in nodes:
    nc.l = find_node(nc.l)
    nc.r = find_node(nc.r)

answer = len(instructions)
for cni, cn in enumerate(start_nodes):
    steps = 0
    while True:
        finished = False
        steps += 1
        for i in instructions:
            next_node = ""
            if i == "R":
                next_node = cn.r
            else:
                next_node = cn.l

            cn = next_node
            if check_node_finished(next_node):
                finished = True
                break

        if finished:
            break

    answer *= steps

print(answer)
