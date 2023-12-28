file = open("input", "r")

grid = []
galaxy_locations = []


def find_galaxy_locations():
    global galaxy_locations
    galaxy_locations = []
    for _row_i, _row in enumerate(grid):
        for _col_i, _col in enumerate(_row):
            if _col == "#":
                galaxy_locations.append([_row_i, _col_i])


def check_row_is_empty(check_row_i):
    for _r in grid[check_row_i]:
        if _r == "#":
            return False
    return True


def check_column_is_empty(check_column_i):
    for _c in grid:
        if _c[check_column_i] == "#":
            return False
    return True


for line in file:
    line = line.replace("\n", "")
    grid.append(line)

find_galaxy_locations()
answer = 0
for galaxy_i, galaxy in enumerate(galaxy_locations):

    if galaxy_i == len(galaxy_locations)-1:
        break

    for galaxy2 in galaxy_locations[galaxy_i+1::]:
        distance = 0
        y_locations = [galaxy[0], galaxy2[0]]
        y_locations.sort()
        x_locations = [galaxy[1], galaxy2[1]]
        x_locations.sort()

        for y in range(y_locations[0], y_locations[1]):
            if check_row_is_empty(y):
                distance += 1_000_000
            else:
                distance += 1

        for x in range(x_locations[0], x_locations[1]):
            if check_column_is_empty(x):
                distance += 1_000_000
            else:
                distance += 1

        answer += distance

print(answer)
