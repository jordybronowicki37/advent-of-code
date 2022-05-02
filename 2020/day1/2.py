file = open("2input", "r")

lijst = []

for line in file:
    lijst.append(int(line))

for i in lijst:
    for j in lijst:
        for k in lijst:
            if i+j+k == 2020:
                print(i*j*k)

