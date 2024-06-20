import math

file = open("input", "r")
answer = 0


def calculate_fuel(f):
    return math.floor(f/3)-2


for line in file:
    line = line.replace("\n", "")
    num = int(line)
    fuel = calculate_fuel(num)
    answer += fuel

print(answer)
