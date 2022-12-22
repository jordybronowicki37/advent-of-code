file = open("input", "r")

marker = []
line = file.readline()

for i in range(len(line)):
    marker.append(line[i])

    if len(marker) == 5:
        marker.remove(marker[0])

    if len(marker) == 4:
        if len(set(marker)) == 4:
            print(i + 1)
            break
