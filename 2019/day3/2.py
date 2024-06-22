file = open("input", "r")
intersections = []
lowest_distance = None


def format_coords(raw):
    coords = []
    current_pos_x = 0
    current_pos_y = 0
    steps = 0
    for instruction in raw:
        start_pos = [current_pos_x, current_pos_y]
        direction = instruction[0]
        amount = int(instruction[1:])
        steps += amount
        if direction == "R":
            current_pos_x += amount
        elif direction == "L":
            current_pos_x -= amount
        elif direction == "U":
            current_pos_y += amount
        elif direction == "D":
            current_pos_y -= amount
        end_pos = [current_pos_x, current_pos_y]
        coords.append([start_pos, end_pos, direction, steps])
    return coords


def is_in_between(coord1, coord2, coord3):
    coords_sorted = sorted([coord1, coord2])
    return coords_sorted[0] < coord3 < coords_sorted[1]


line1 = file.readline().replace("\n", "").split(",")
line2 = file.readline().replace("\n", "").split(",")
coords1 = format_coords(line1)
coords2 = format_coords(line2)

for coord in coords1:
    for check in coords2:
        if coord[2] in ["R", "L"]:
            if check[2] in ["R", "L"]:
                continue
            check_hor = is_in_between(check[0][1], check[1][1], coord[0][1])
            check_ver = is_in_between(coord[0][0], coord[1][0], check[0][0])
            if check_hor and check_ver:
                steps = coord[3] - abs(check[1][0] - coord[1][0])
                steps += check[3] - abs(coord[1][1] - check[1][1])
                intersections.append([coord[1][1], check[1][0], steps])

        if coord[2] in ["U", "D"]:
            if check[2] in ["U", "D"]:
                continue
            check_hor = is_in_between(coord[0][1], coord[1][1], check[0][1])
            check_ver = is_in_between(check[0][0], check[1][0], coord[0][0])
            if check_hor and check_ver:
                steps = check[3] - abs(coord[1][0] - check[1][0])
                steps += coord[3] - abs(check[1][1] - coord[1][1])
                intersections.append([check[1][1], coord[1][0], steps])


for inter in intersections:
    distance = inter[2]
    if lowest_distance is None or distance < lowest_distance:
        lowest_distance = distance

print(lowest_distance)
