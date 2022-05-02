file = open("input", "r")
coords = {}


def insert_coord(coord):
    c = coords.get(coord)
    if c:
        coords[coord] = c+1
    else:
        coords[coord] = 1


for line in file:
    line = line.replace("\n", "")
    coords_new = line.replace(" -> ", ",")
    coords_split = coords_new.split(",")

    x1 = int(coords_split[0])
    y1 = int(coords_split[1])
    x2 = int(coords_split[2])
    y2 = int(coords_split[3])

    if x1 == x2:
        if y2 > y1:
            for i in range(y2 - y1 + 1):
                insert_coord(str(x1)+","+str(y1+i))
        else:
            for i in range(y1 - y2 + 1):
                insert_coord(str(x1)+","+str(y2+i))

    elif y1 == y2:
        if x2 > x1:
            for i in range(x2 - x1 + 1):
                insert_coord(str(x1+i)+","+str(y1))
        else:
            for i in range(x1 - x2 + 1):
                insert_coord(str(x2+i)+","+str(y1))

    else:
        # start links onder
        if y1 < y2 and x1 < x2:
            for i in range(y2 - y1 + 1):
                co = str(x1+i)+","+str(y1+i)
                insert_coord(co)
        # start rechts onder
        elif y1 < y2 and x1 > x2:
            for i in range(y2 - y1 + 1):
                co = str(x1-i)+","+str(y1+i)
                insert_coord(co)
        # start links boven
        elif y1 > y2 and x1 < x2:
            for i in range(y1 - y2 + 1):
                co = str(x1+i)+","+str(y1-i)
                insert_coord(co)
        # start rechts boven
        else:
            for i in range(y1 - y2 + 1):
                co = str(x1-i)+","+str(y1-i)
                insert_coord(co)

coords_copy = coords.copy()
for i in coords_copy.keys():
    if coords[i] == 1:
        coords.pop(i)

print(len(coords))
