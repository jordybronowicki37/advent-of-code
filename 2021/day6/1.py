file = open("input", "r")
fish = []

for line in file:
    line = line.replace("\n", "")
    nums = line.split(",")
    for i in nums:
        fish.append(int(i))

for _ in range(80):
    new = []
    copy = fish.copy()
    for i in range(len(fish)):
        age = fish[i]
        if age == 0:
            new.append(8)
            copy[i] = 6
        else:
            copy[i] = age - 1
    fish = copy.copy()
    fish.extend(new)

print(len(fish))
