file = open("input", "r")

# Rock:     A
# Paper:    B
# Scissors: C

# Lose: X
# Draw: Y
# Win:  Z

score = 0

for line in file:
    line = line.replace("\n", "")

    opponent = line[0]
    response = line[2]

    if response == "X":
        score += 0
    elif response == "Y":
        score += 3
    elif response == "Z":
        score += 6

    # Rock
    if (opponent == "A" and response == "Y") or \
            (opponent == "B" and response == "X") or \
            (opponent == "C" and response == "Z"):
        score += 1
    # Paper
    elif (opponent == "A" and response == "Z") or \
            (opponent == "B" and response == "Y") or \
            (opponent == "C" and response == "X"):
        score += 2
    # Scissors
    elif (opponent == "A" and response == "X") or \
            (opponent == "B" and response == "Z") or \
            (opponent == "C" and response == "Y"):
        score += 3

print(score)
