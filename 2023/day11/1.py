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


def check_row_is_empty(check_row):
    for _r in check_row:
        if _r == "#":
            return False
    return True


def check_column_is_empty(check_column):
    for _c in grid:
        if _c[check_column] == "#":
            return False
    return True


for line in file:
    line = line.replace("\n", "")
    grid.append(line)

# Extend grid
new_grid = []
for row_i, row in enumerate(grid):
    new_row = ""
    for col_i, col in enumerate(row):
        if check_column_is_empty(col_i):
            new_row += ".."
        else:
            new_row += col

    new_grid.append(new_row)
    if check_row_is_empty(new_row):
        new_grid.append(new_row)
grid = new_grid

# Find distances
find_galaxy_locations()
answer = 0
for galaxy_i, galaxy in enumerate(galaxy_locations):

    if galaxy_i == len(galaxy_locations)-1:
        break

    for galaxy2 in galaxy_locations[galaxy_i+1::]:
        distance = 0
        distance += abs(galaxy[0] - galaxy2[0])
        distance += abs(galaxy[1] - galaxy2[1])
        answer += distance

print(answer)
