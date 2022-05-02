file = open("input", "r")
lines = []


def search_o2_line():
    copy = lines.copy()
    for i in range(12):
        common = most_common(copy)
        if len(copy) == 1:
            return copy[0]
        o = common[i]
        if o[0] > o[1]:
            copy = list(filter(lambda x: (x[i] == "0"), copy))
        else:
            copy = list(filter(lambda x: (x[i] == "1"), copy))
    return copy[0]


def search_co2_scrubber_line():
    copy = lines.copy()
    for i in range(12):
        common = most_common(copy)
        if len(copy) == 1:
            return copy[0]
        o = common[i]
        if o[0] <= o[1]:
            copy = list(filter(lambda x: (x[i] == "0"), copy))
        else:
            copy = list(filter(lambda x: (x[i] == "1"), copy))
    return copy[0]


def most_common(lijstje):
    common = {}
    for i in range(12):
        common[i] = {0: 0, 1: 0}
    for j in lijstje:
        for i in range(len(j)):
            bit = int(j[i])
            common[i][bit] += 1
    return common


for line in file:
    line = line.replace("\n", "")
    lines.append(line)

print(int(search_o2_line(), 2) * int(search_co2_scrubber_line(), 2))
