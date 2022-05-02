file = open("input", "r")
flashes = 0
steps = 0
octos = []

class Octo:
    def __init__(self, power):
        self.power = power
        self.flashed = False
        self.n = None
        self.ne = None
        self.e = None
        self.se = None
        self.s = None
        self.sw = None
        self.w = None
        self.nw = None

    def step(self):
        global flashes
        if not self.flashed:
            self.power += 1
            if self.power > 9:
                self.flashed = True
                self.power = 0
                flashes += 1

                neighbors = [self.n, self.ne, self.e, self.se, self.s, self.sw, self.w, self.nw]
                for neighbor in neighbors:
                    if neighbor:
                        neighbor.step()


previous_row = []
for line in file:
    line = line.replace("\n", "")

    current_row = []
    for i in line:
        octo = Octo(int(i))

        # set left
        if len(current_row) > 0:
            octo.w = current_row[-1]
            current_row[-1].e = octo

        # set top
        if len(previous_row) > 0:
            index = len(current_row)

            # set middle
            octo.n = previous_row[index]
            previous_row[index].s = octo

            # set left
            if index > 0:
                octo.nw = previous_row[index-1]
                previous_row[index - 1].se = octo

            # set right
            if index < 9:
                octo.ne = previous_row[index+1]
                previous_row[index + 1].sw = octo

        current_row.append(octo)
        octos.append(octo)

    previous_row = current_row


while flashes < 100:
    flashes = 0
    for i in octos:
        i.flashed = False

    for i in octos:
        i.step()

    steps += 1

print(steps)
