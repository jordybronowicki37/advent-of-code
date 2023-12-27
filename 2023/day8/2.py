# DOES NOT WORK, yet
file = open("input", "r")

instructions = ""
nodes = []
current_nodes = []
steps = 0


class Node:
    def __init__(self, values):
        self.n = values[0]
        self.l = values[1]
        self.r = values[2]


def find_node(v):
    for n in nodes:
        if n.n == v:
            return n


def check_all_nodes_on_finish():
    for _cn in current_nodes:
        if _cn.n[2] != "Z":
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
            current_nodes.append(nn)
        nodes.append(nn)

for nc in nodes:
    nc.l = find_node(nc.l)
    nc.r = find_node(nc.r)

while True:
    finished = False
    for i in instructions:
        if steps % 1_000_000 == 0:
            print(steps // 1_000_000)
        steps += 1
        for cni, cn in enumerate(current_nodes):
            next_node = ""
            if i == "R":
                next_node = cn.r
            else:
                next_node = cn.l

            current_nodes[cni] = next_node
        if check_all_nodes_on_finish():
            finished = True
            break

    if finished:
        break

print(steps)
