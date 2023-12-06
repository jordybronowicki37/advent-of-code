import math

file = open("input", "r")

lines = file.readlines()
time = int("".join(filter(None, lines[0].replace("\n", "").replace("Time:", "").split(" "))))
distance = int("".join(filter(None, lines[1].replace("Distance:", "").split(" "))))
answer = 0

for j in range(time):
    if j % 1000000 == 0:
        print(f"{math.floor(j / time * 100)}%")
    charge_time = j + 1
    race_time = time - charge_time
    if charge_time * race_time > distance:
        answer += 1

print(answer)
