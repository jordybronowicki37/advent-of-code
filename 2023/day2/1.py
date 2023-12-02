file = open("input", "r")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
answer = 0

for line in file:
    line = line.replace("\n", "")
    game_cubes_split = line.split(": ")
    game_id = int(game_cubes_split[0].replace("Game ", ""))
    condition_failed = False

    for cube_set in game_cubes_split[1].split("; "):
        cubes = cube_set.split(", ")
        amount_red = 0
        amount_green = 0
        amount_blue = 0

        for cube in cubes:
            cube_amount_color = cube.split(" ")
            if cube_amount_color[1] == "red":
                amount_red += int(cube_amount_color[0])
            elif cube_amount_color[1] == "green":
                amount_green += int(cube_amount_color[0])
            elif cube_amount_color[1] == "blue":
                amount_blue += int(cube_amount_color[0])

        if amount_red > MAX_RED or amount_green > MAX_GREEN or amount_blue > MAX_BLUE:
            condition_failed = True
            break
    if not condition_failed:
        answer += game_id

print(answer)
