file = open("input", "r")
temp = []
fish = []
score = 0


class School:
    def __init__(self, num, size):
        self.num = num
        self.size = size

    def age(self):
        global fish
        if self.num == 0:
            self.num = 6
            fish.append(School(8, self.size))
        else:
            self.num -= 1


def collapse():
    global fish
    temp_fishes = []
    for x in range(9):
        temp_fishes.append(School(x, 0))
    for x in fish:
        temp_fishes[x.num].size += x.size
    fish = temp_fishes.copy()


for line in file:
    line = line.replace("\n", "")
    temp = line.split(",")

for i in range(7):
    amount = temp.count(str(i))
    fish.append(School(i, amount))

for i in range(256):
    for j in range(len(fish)):
        fish[j].age()
    collapse()

for i in fish:
    score += i.size

print(score)
