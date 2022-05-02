file = open("input", "r")
coords = set([])
folds = []
last_y_fold = 0
last_x_fold = 0


def make_fold_on(fold):
    global last_x_fold, last_y_fold, coords
    new_coords = set([])
    direction = fold.split("=")[0]
    fold_coord = int(fold.split("=")[1])

    if direction == "x":
        last_x_fold = fold_coord
    else:
        last_y_fold = fold_coord

    for i in coords.copy():
        x = int(i.split(",")[0])
        y = int(i.split(",")[1])

        if direction == "x":
            if x > fold_coord:
                difference = x - fold_coord
                x = x - (2 * difference)
        else:
            if y > fold_coord:
                difference = y - fold_coord
                y = y - (2 * difference)

        new_coords.add(str(x) + "," + str(y))
    return new_coords


def print_diagram():
    global coords
    lines = [" " * last_x_fold for x in range(last_y_fold)]

    for i in coords:
        x = int(i.split(",")[0])
        y = int(i.split(",")[1])
        row = lines[y]
        lines[y] = row[:x] + "x" + row[x + 1:]

    for i in lines:
        print(i)


coords_done = False
for line in file:
    line = line.replace("\n", "")

    if coords_done:
        folds.append(line.replace("fold along ", ""))
        continue

    if line != "":
        coords.add(line)
    else:
        coords_done = True

for i in folds:
    coords = make_fold_on(i)

print_diagram()
