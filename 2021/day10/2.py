file = open("input", "r")
scores = []

for line in file:
    line = line.replace("\n", "")
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    points = [1, 2, 3, 4]
    previous_chars = []
    corrupted = False

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
                corrupted = True
                break

    if not corrupted:
        score_local = 0
        previous_chars.reverse()

        for i in previous_chars:
            index = opening.index(i)
            score_local *= 5
            score_local += points[index]

        scores.append(score_local)

scores.sort()
print(scores[int(len(scores)/2)])
