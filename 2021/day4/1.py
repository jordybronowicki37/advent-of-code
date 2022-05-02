file = open("input", "r")
first = True
cards = []
numbers = []
last_num = 0
temp = []


class BingoNumber:
    def __init__(self, num):
        self.num = num
        self.checked = False

    def __str__(self):
        return self.num + self.checked


class Card:
    def __init__(self, bingoNumbers):
        self.numbers_horizontal = []
        self.numbers_vertical = [[], [], [], [], []]
        for i in bingoNumbers:
            temp = []
            for j in i:
                temp.append(BingoNumber(j))
            self.numbers_horizontal.append(temp)

        for i in self.numbers_horizontal:
            for j in range(len(i)):
                self.numbers_vertical[j].append(i[j])

    def check(self):
        for i in self.numbers_horizontal:
            amount = 0
            for j in i:
                if j.checked:
                    amount += 1
            if amount == 5:
                return True

        for i in self.numbers_vertical:
            amount = 0
            for j in i:
                if j.checked:
                    amount += 1
            if amount == 5:
                return True

        return False

    def check_card(self, num):
        for i in self.numbers_horizontal:
            for j in i:
                if j.num == num:
                    j.checked = True


for line in file:
    line = line.replace("\n", "")
    if first:
        numbers = line.split(",")
    elif line == "":
        cards.append(Card(temp))
        temp = []
    else:
        nums = line.split(" ")
        nums = list(filter(lambda x: not x == "", nums))
        temp.append(nums)
    first = False


def play():
    global numbers, last_num
    for i in numbers:
        for j in cards:
            j.check_card(i)
            if j.check():
                last_num = int(i)
                return j


winner = play()
score = 0

for x in winner.numbers_horizontal:
    for y in x:
        if not y.checked:
            score += int(y.num)

print(score * last_num)
