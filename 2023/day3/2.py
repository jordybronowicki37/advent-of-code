file = open("input", "r")

lines = file.readlines()
MAX_X = len(lines[0])
MAX_Y = len(lines)
connected_gears = []


def check_con_to_gr(x, y, number):
    for y2 in range(3):
        y2 += y - 1
        if y2 < 0 or y2 > MAX_Y - 1:
            continue
        for x2 in range(len(number) + 2):
            x2 += x - 1
            if x2 < 0 or x2 > MAX_X:
                continue
            if lines[y2][x2] == "*":
                connected_gears.append([number, [y2, x2]])


for i in range(len(lines)):
    line = lines[i]
    first_col_num_pos = None
    col_nums = ""

    for j in range(len(line)):
        char = line[j]

        if char.isdigit():
            col_nums += char
            if not first_col_num_pos:
                first_col_num_pos = j

        else:
            if not first_col_num_pos:
                continue
            check_con_to_gr(first_col_num_pos, i, col_nums)

            # Reset values
            col_nums = ""
            first_col_num_pos = None

answer = 0
for z in range(len(connected_gears)):
    con_gr = connected_gears[z]
    for z2 in range(len(connected_gears)):
        con_gr2 = connected_gears[z2]
        # Same item
        if z == z2:
            continue
        # Already checked
        if not con_gr[1] or not con_gr2[1]:
            continue
        # If coords
        if con_gr[1][0] == con_gr2[1][0] and con_gr[1][1] == con_gr2[1][1]:
            answer += (int(con_gr[0]) * int(con_gr2[0]))
            con_gr[1] = None

print(answer)
