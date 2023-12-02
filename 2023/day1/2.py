file = open("input", "r")

cvs = []
answer = 0
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def check_starts_with(input: str):
    for i in range(len(numbers)):
        num = numbers[i]
        if input.startswith(num):
            return str(i)
    return ""


def check_ends_with(input: str):
    for i in range(len(numbers)):
        num = numbers[i]
        if input.endswith(num):
            return str(i)
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
