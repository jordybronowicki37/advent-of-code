file = open("1input", "r")
amountValid = 0

for line in file:
    mainSplit = line.split(":")
    infoSplit = mainSplit[0].split(" ")
    infoNumbers = infoSplit[0].split("-")

    text = mainSplit[1].replace(" ", "")
    letter = infoSplit[1]
    min = int(infoNumbers[0])
    max = int(infoNumbers[1])
    occurences = text.count(letter)

    if min <= occurences <= max:
        amountValid += 1

print(amountValid)
