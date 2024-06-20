file = open("input", "r")
previousValue = 0
increases = 0
slider = []

for line in file:
    if len(slider) == 3:
        previousValue = sum(slider)
        slider.pop(0)
        slider.append(int(line))
        if previousValue < sum(slider):
            increases += 1
    else:
        slider.append(int(line))

print(increases)
