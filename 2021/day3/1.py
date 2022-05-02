file = open("input", "r")
common = {}
gamma = ""
epsilon = ""

for i in range(12):
    common[i] = {0:0, 1:0}

for line in file:
    line = line.replace("\n", "")
    for i in range(len(line)):
        bit = int(line[i])
        common[i][bit] += 1

for i in common.keys():
    o = common[i]
    if o[0] < o[1]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
