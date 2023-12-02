file = open("input", "r")

answer = 0

for line in file:
    line = line.replace("\n", "")
    game_cubes_split = line.split(": ")
    game_id = int(game_cubes_split[0].replace("Game ", ""))
    condition_failed = False

    required_red = 0
    required_green = 0
    required_blue = 0

    for cube_set in game_cubes_split[1].split("; "):
        cubes = cube_set.split(", ")

        for cube in cubes:
            cube_amount_color = cube.split(" ")
            if cube_amount_color[1] == "red":
                amount_red = int(cube_amount_color[0])
                if amount_red > required_red:
                    required_red = amount_red
            elif cube_amount_color[1] == "green":
                amount_green = int(cube_amount_color[0])
                if amount_green > required_green:
                    required_green = amount_green
            elif cube_amount_color[1] == "blue":
                amount_blue = int(cube_amount_color[0])
                if amount_blue > required_blue:
                    required_blue = amount_blue

    power_of_set = required_red * required_green * required_blue
    answer += power_of_set

print(answer)
