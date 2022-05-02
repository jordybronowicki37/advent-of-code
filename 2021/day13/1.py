file = open("input", "r")
coords = set([])
folds = []


def make_fold_on(fold):
    new_coords = set([])
    for i in coords.copy():
        x = int(i.split(",")[0])
        y = int(i.split(",")[1])
        direction = fold.split("=")[0]
        fold_coord = int(fold.split("=")[1])

        if direction == "x":
            if x > fold_coord:
                difference = x-fold_coord
                x = x - (2*difference)
        else:
            if y > fold_coord:
                difference = y-fold_coord
                y = y - (2*difference)

        new_coords.add(str(x) + "," + str(y))
    return new_coords


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

print(len(coords))
print(len(make_fold_on(folds[0])))
