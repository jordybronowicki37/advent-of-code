file = open("input", "r")

# Rock:     A, X
# Paper:    B, Y
# Scissors: C, Z

score = 0

for line in file:
    line = line.replace("\n", "")

    opponent = line[0]
    response = line[2]

    if response == "X":
        score += 1
    elif response == "Y":
        score += 2
    elif response == "Z":
        score += 3

    if (opponent == "A" and response == "Z") or \
            (opponent == "B" and response == "X") or \
            (opponent == "C" and response == "Y"):
        score += 0
    elif (opponent == "A" and response == "X") or \
            (opponent == "B" and response == "Y") or \
            (opponent == "C" and response == "Z"):
        score += 3
    elif (opponent == "A" and response == "Y") or \
            (opponent == "B" and response == "Z") or \
            (opponent == "C" and response == "X"):
        score += 6

print(score)
