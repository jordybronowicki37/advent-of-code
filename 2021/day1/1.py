file = open("input", "r")
previousValue = 0
increases = 0

for line in file:
    number = int(line)
    if number > previousValue:
        increases += 1
    previousValue = number

print(increases-1)
