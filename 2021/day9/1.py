file = open("input", "r")
basins_sizes = []
all_coords = []

class Coord:
    def __init__(self, height):
        self.height = height
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def check(self):
        global basins_sizes
        im_lowest = False
        heights = [self.height]

        # check neighbors
        if self.top:
            heights.append(self.top.height)
        if self.right:
            heights.append(self.right.height)
        if self.bottom:
            heights.append(self.bottom.height)
        if self.left:
            heights.append(self.left.height)

        heights.sort()
        if heights[0] == self.height and not heights[1] == self.height:
            low_points.append(self)


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
    i.check()

result = 0
for i in basins_sizes:
    result += i.height+1
print(result)
