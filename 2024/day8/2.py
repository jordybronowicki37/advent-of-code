file = open("input", "r")

width = 0
height = 0
all_antinodes = set()
all_antennas = set()
antennas = {}


def check_coord_out_of_bounds(coord):
    global width, height
    return coord[0] < 0 or coord[0] >= width or coord[1] < 0 or coord[1] >= height


for line in file:
    width = len(line)
    line = line.replace("\n", "")
    for x in range(len(line)):
        v = line[x]
        if v != ".":
            antenna_coord = (height, x)
            all_antennas.add(antenna_coord)
            if v in antennas:
                antennas.get(v).append(antenna_coord)
            else:
                antennas[v] = [antenna_coord]
    height += 1


for frequency in antennas.keys():
    values = antennas.get(frequency)
    for current_antenna in values:
        for check_antenna in values:
            if current_antenna == check_antenna:
                continue

            y_dif = check_antenna[0] - current_antenna[0]
            x_dif = check_antenna[1] - current_antenna[1]


            new_coord = (current_antenna[0]-y_dif, current_antenna[1]-x_dif)
            while not check_coord_out_of_bounds(new_coord):
                all_antinodes.add(new_coord)
                new_coord = (new_coord[0]-y_dif, new_coord[1]-x_dif)

print(len({*all_antinodes, *all_antennas}))
