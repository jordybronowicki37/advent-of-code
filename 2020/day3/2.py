def slopingForest(right, down):
    file = open("2inputdyllan.txt", "r")
    trees = 0
    line_num = 0

    for line in file:
        if line_num >= down and line_num % down == 0:
            index = int(((line_num / down) * right) % 31)
            if line[index] == '#':
                trees += 1

        line_num += 1
    file.close()
    return trees


r1d1 = slopingForest(1, 1)
r3d1 = slopingForest(3, 1)
r5d1 = slopingForest(5, 1)
r7d1 = slopingForest(7, 1)
r1d2 = slopingForest(1, 2)

print(r1d1)
print(r3d1)
print(r5d1)
print(r7d1)
print(r1d2)

print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)
