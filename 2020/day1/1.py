file = open("input", "r")
lijst = []

for line in file:
    lijst.append(int(line))

for i in lijst:
    for j in lijst:
        if i + j == 2020:
            print(i*j)

