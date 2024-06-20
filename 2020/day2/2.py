file = open("input", "r")
amountValid = 0

for line in file:
    mainSplit = line.split(":")
    infoSplit = mainSplit[0].split(" ")
    infoNumbers = infoSplit[0].split("-")

    text = mainSplit[1].replace(" ", "")
    letter = infoSplit[1]
    num1 = int(infoNumbers[0])
    num2 = int(infoNumbers[1])

    bool1 = text[num1-1] == letter
    bool2 = text[num2-1] == letter

    if not bool1 == bool2:
        amountValid += 1

print(amountValid)
