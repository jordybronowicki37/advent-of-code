file = open("1input", "r")
answers = ""
count = 0

for line in file:
    line = line.replace("\n", "")
    if line == "":
        count += len(answers)
        answers = ""
    else:
        for i in line:
            if i not in answers:
                answers += i

print(count)
