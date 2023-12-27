import sys
import threading

sys.setrecursionlimit(100000)
threading.stack_size(200000000)


def all_code():
    file = open("input", "r")

    grid = []
    route = []
    direction = "down"
    y = 0
    x = 0

    # Load grid
    for line in file:
        line = line.replace("\n", "")
        if "S" in line:
            y = len(grid)
            x = line.index("S")
        grid.append(line)

    # Find route
    while grid[y][x] != "S" or len(route) == 0:
        route.append([y, x])
        pipe = ""
        if direction == "up":
            y -= 1
            pipe = grid[y][x]
            if pipe == "|":
                continue
            elif pipe == "F":
                direction = "right"
            elif pipe == "7":
                direction = "left"

        elif direction == "right":
            x += 1
            pipe = grid[y][x]
            if pipe == "-":
                continue
            elif pipe == "J":
                direction = "up"
            elif pipe == "7":
                direction = "down"

        elif direction == "down":
            y += 1
            pipe = grid[y][x]
            if pipe == "|":
                continue
            elif pipe == "L":
                direction = "right"
            elif pipe == "J":
                direction = "left"

        elif direction == "left":
            x -= 1
            pipe = grid[y][x]
            if pipe == "-":
                continue
            elif pipe == "F":
                direction = "down"
            elif pipe == "L":
                direction = "up"

    # Add the first node to the end
    route.append(route[0])

    def find_cell_in_route(y, x):
        for _r in route:
            if _r[0] == y and _r[1] == x:
                return True
        return False

    # Clear grid
    new_grid = []
    for row_i, row in enumerate(grid):
        new_row = ""
        for cell_i, cell in enumerate(row):
            if find_cell_in_route(row_i, cell_i):
                new_row += cell
            else:
                new_row += "."
        new_grid.append(new_row)
    grid = new_grid

    # Extend route coords
    for nri, nr in enumerate(route):
        route[nri] = [nr[0] * 2, nr[1] * 2]

    def check_value_between_nodes(y, x):
        for cvri, cvr in enumerate(route):
            if cvri == 0:
                continue
            rv1 = route[cvri - 1]
            rv2 = cvr
            same_y = rv1[0] == rv2[0] and rv1[0] == y
            same_x = rv1[1] == rv2[1] and rv1[1] == x

            if same_y:
                if (rv1[1] + rv2[1]) / 2 == x:
                    return True
            elif same_x:
                if (rv1[0] + rv2[0]) / 2 == y:
                    return True
        return False

    # Extend grid
    new_grid = []
    height = len(grid)
    width = len(grid[0])
    for hi in range(height):
        new_filled_row = ""
        for nfc in grid[hi]:
            new_filled_row += nfc + " "
        new_grid.append(new_filled_row)
        new_row = list(" " for _ in range(width * 2))
        new_grid.append(new_row)
    grid = new_grid

    # Fill grid gaps
    new_grid = []
    for f_row_i, f_row in enumerate(grid):
        new_row = ""
        for f_cell_i, f_cell in enumerate(f_row):
            # Skip existing value locations and intermediate points
            if (f_row_i % 2 == 0 and f_cell_i % 2 == 0) or (f_row_i % 2 == 1 and f_cell_i % 2 == 1):
                new_row += grid[f_row_i][f_cell_i]
                continue
            if check_value_between_nodes(f_row_i, f_cell_i):
                new_row += "V"
            else:
                new_row += " "
        new_grid.append(new_row)
    grid = new_grid

    # Find the inside of the route
    visited_nodes = set()
    grid_height = len(grid)
    grid_width = len(grid[0])

    def marching_cube(y, x):
        visited_nodes.add(f"{y},{x}")
        if grid[y][x] not in ". ":
            return

        if y != 0 and f"{y - 1},{x}" not in visited_nodes:
            marching_cube(y - 1, x)
        if x != 0 and f"{y},{x - 1}" not in visited_nodes:
            marching_cube(y, x - 1)
        if y != grid_height - 1 and f"{y + 1},{x}" not in visited_nodes:
            marching_cube(y + 1, x)
        if x != grid_width - 1 and f"{y},{x + 1}" not in visited_nodes:
            marching_cube(y, x + 1)

    marching_cube(0, 0)

    answer = 0
    for ans_y_i, ans_y in enumerate(grid):
        for ans_x_i, ans_x in enumerate(ans_y):
            if ans_x == "." and f"{ans_y_i},{ans_x_i}" not in visited_nodes:
                answer += 1
    print(answer)


thread = threading.Thread(target=all_code)
thread.start()
