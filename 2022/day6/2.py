file = open("input", "r")

marker = []
line = file.readline()

for i in range(len(line)):
    marker.append(line[i])

    if len(marker) == 15:
        marker.remove(marker[0])

    if len(marker) == 14:
        if len(set(marker)) == 14:
            print(i + 1)
            break
