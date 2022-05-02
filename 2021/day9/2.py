file = open("input", "r")
basins_sizes = []
all_coords = []

class Coord:
    def __init__(self, height):
        self.height = height
        self.checked = height == 9
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def check(self):
        global basins_sizes
        if not self.checked:
            self.checked = True
            amount = 1

            # check neighbors
            if self.top:
                amount += self.top.check()
            if self.right:
                amount += self.right.check()
            if self.bottom:
                amount += self.bottom.check()
            if self.left:
                amount += self.left.check()

            return amount
        return 0


previous_line = []
for line in file:
    line = line.replace("\n", "")
    current_line = []

    for i in range(len(line)):
        num = line[i]
        coord = Coord(int(num))

        # Define left
        if len(current_line) > 0:
            previous_coord = current_line[-1]
            coord.left = previous_coord
            previous_coord.right = coord

        # Define top
        if len(previous_line) > 0:
            top_coord = previous_line[i]
            coord.top = top_coord
            top_coord.bottom = coord

        current_line.append(coord)
        all_coords.append(coord)

    previous_line = current_line

for i in all_coords:
    size = i.check()
    if size > 0:
        basins_sizes.append(size)

basins_sizes.sort()
result = 0
for i in basins_sizes[-3:]:
    if result == 0:
        result = i
    else:
        result *= i
print(result)
