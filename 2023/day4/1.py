file = open("input", "r")

answer = 0

for line in file:
    line = line.replace("\n", "")
    data = line.split(": ")[1].split(" | ")
    winning_numbers = list(filter(None, data[0].split(" ")))
    my_numbers = list(filter(None, data[1].split(" ")))
    points = 0

    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    answer += points

print(answer)
