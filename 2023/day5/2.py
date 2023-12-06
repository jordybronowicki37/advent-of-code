file = open("input", "r")

seeds = []

mapping_stage = 0
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []


def add_mapping_to_map(mapping):
    if mapping_stage == 0:
        seed_to_soil_map.append(mapping)
    elif mapping_stage == 1:
        soil_to_fertilizer_map.append(mapping)
    elif mapping_stage == 2:
        fertilizer_to_water_map.append(mapping)
    elif mapping_stage == 3:
        water_to_light_map.append(mapping)
    elif mapping_stage == 4:
        light_to_temperature_map.append(mapping)
    elif mapping_stage == 5:
        temperature_to_humidity_map.append(mapping)
    elif mapping_stage == 6:
        humidity_to_location_map.append(mapping)


for line in file:
    line = line.replace("\n", "")

    if line == "":
        continue
    elif line.startswith("seeds: "):
        sg = [int(seed) for seed in line.replace("seeds: ", "").split(" ")]
        for i in range(len(sg)):
            if i % 2 == 1:
                continue
            seeds.append([sg[i], sg[i+1]])
    elif line == "seed-to-soil map:":
        mapping_stage = 0
    elif line == "soil-to-fertilizer map:":
        mapping_stage = 1
    elif line == "fertilizer-to-water map:":
        mapping_stage = 2
    elif line == "water-to-light map:":
        mapping_stage = 3
    elif line == "light-to-temperature map:":
        mapping_stage = 4
    elif line == "temperature-to-humidity map:":
        mapping_stage = 5
    elif line == "humidity-to-location map:":
        mapping_stage = 6
    else:
        add_mapping_to_map([int(n) for n in line.split(" ")])


def convert_using_map(seed_groups, map):
    resulting_group = []
    new_groups = []
    for seed_group in seed_groups:
        group_mapped = False
        for mapping in map:
            mapping_start = mapping[1]
            mapping_end = mapping[1] + mapping[2] - 1
            seed_group_start = seed_group[0]
            seed_group_end = seed_group[0] + seed_group[1] - 1

            # Mapping out of range
            if mapping_end < seed_group_start or mapping_start > seed_group_end:
                continue

            # Mapping includes entire group
            elif seed_group_start >= mapping_start and mapping_end >= seed_group_end:
                resulting_group.append([mapping[0] + seed_group_start - mapping_start, seed_group[1]])

            # Mapping on the start
            elif seed_group_start >= mapping_start and mapping_end < seed_group_end:
                resulting_group.append([mapping[0] + seed_group_start - mapping_start, mapping_end - seed_group_start + 1])
                new_groups.append([mapping_end + 1, seed_group_end - mapping_end])

            # Mapping on the end
            elif seed_group_start < mapping_start and mapping_end >= seed_group_end:
                resulting_group.append([mapping[0], seed_group_end - mapping_start + 1])
                new_groups.append([seed_group_start, mapping_start - seed_group_start])

            # Mapping completely inside
            elif seed_group_start < mapping_start and mapping_end < seed_group_end:
                resulting_group.append([mapping[0], mapping[2]])
                new_groups.append([seed_group_start, mapping_end - seed_group_start])
                new_groups.append([mapping_end + 1, seed_group_end - mapping_end])
            else:
                print("Error")
            group_mapped = True
            break

        # No map has mapped the group
        if not group_mapped:
            resulting_group.append(seed_group)
    if len(new_groups) > 0:
        resulting_group.extend(convert_using_map(new_groups, map))
    return resulting_group


location_results = []
for seed in seeds:
    seed = [seed]
    seed = convert_using_map(seed, seed_to_soil_map)
    seed = convert_using_map(seed, soil_to_fertilizer_map)
    seed = convert_using_map(seed, fertilizer_to_water_map)
    seed = convert_using_map(seed, water_to_light_map)
    seed = convert_using_map(seed, light_to_temperature_map)
    seed = convert_using_map(seed, temperature_to_humidity_map)
    seed = convert_using_map(seed, humidity_to_location_map)
    location_results.extend(seed)

print(min([j[0] for j in location_results]))
