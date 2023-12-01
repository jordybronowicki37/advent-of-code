file = open("input", "r")

cvs = []
answer = 0


def check_starts_with(input: str):
    if input.startswith("one"):
        return "1"
    elif input.startswith("two"):
        return "2"
    elif input.startswith("three"):
        return "3"
    elif input.startswith("four"):
        return "4"
    elif input.startswith("five"):
        return "5"
    elif input.startswith("six"):
        return "6"
    elif input.startswith("seven"):
        return "7"
    elif input.startswith("eight"):
        return "8"
    elif input.startswith("nine"):
        return "9"
    elif input.startswith("zero"):
        return "0"
    else:
        return ""


def check_ends_with(input: str):
    if input.endswith("one"):
        return "1"
    elif input.endswith("two"):
        return "2"
    elif input.endswith("three"):
        return "3"
    elif input.endswith("four"):
        return "4"
    elif input.endswith("five"):
        return "5"
    elif input.endswith("six"):
        return "6"
    elif input.endswith("seven"):
        return "7"
    elif input.endswith("eight"):
        return "8"
    elif input.endswith("nine"):
        return "9"
    elif input.endswith("zero"):
        return "0"
    else:
        return ""


for line in file:
    line = line.replace("\n", "")
    d = ""
    for i in range(len(line)):
        j = line[i::]
        if j[0].isdigit():
            d = j[0]
            break
        jc = check_starts_with(j)
        if jc != "":
            d = d + jc
            break

    for i in range(len(line)):
        l = line[slice(0, len(line)-i, 1)]
        if l[len(l)-1].isdigit():
            d = d + l[len(l)-1]
            break
        lc = check_ends_with(l)
        if lc != "":
            d = d + lc
            break
    cvs.append(d)

for cv in cvs:
    answer = answer + int(cv)

print(answer)
