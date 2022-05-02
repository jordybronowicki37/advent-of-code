file = open("input", "r")
score = 0

for line in file:
    line = line.replace("\n", "")
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    points = [3, 57, 1197, 25137]
    previous_chars = []

    for i in line:
        if i in opening:
            previous_chars.append(i)
        else:
            previous = previous_chars[-1]
            index_open = opening.index(previous)
            index_close = closing.index(i)

            if index_open == index_close:
                previous_chars.pop(-1)
            else:
                score += points[index_close]
                break

print(score)
