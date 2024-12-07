import re

file = open("input", "r")
result = 0

for line in file:
    line = line.replace("\n", "")
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)

    for match in matches:
        nums = match.replace("mul(", "").replace(")", "").split(",")
        result += int(nums[0]) * int(nums[1])

print(result)
