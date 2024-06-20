import math

file = open("input", "r")
answer = 0


def calculate_fuel(f):
    req_fuel = math.floor(f/3)-2
    if req_fuel <= 0:
        return 0
    return calculate_fuel(req_fuel) + req_fuel


for line in file:
    line = line.replace("\n", "")
    num = int(line)
    fuel = calculate_fuel(num)
    answer += fuel

print(answer)
