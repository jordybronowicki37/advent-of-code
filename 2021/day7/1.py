file = open("input", "r")
positions = []
smallest = 9999999999


def try_position(coord):
    global positions
    sum_fuel = 0

    for i in positions.copy():
        sum_fuel += abs(i - coord)

    return sum_fuel


for line in file:
    line = line.split(",")
    for i in line:
        positions.append(int(i))

for i in range(max(positions)):
    num = try_position(i)
    if num < smallest:
        smallest = num

print(smallest)
