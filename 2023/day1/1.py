file = open("input", "r")

cvs = []
answer = 0


for line in file:
    line = line.replace("\n", "")
    d = ""
    for i in range(len(line)):
        j = line[i]
        if j.isdigit():
            d = j
            break

    for i in range(len(line)):
        l = line[len(line)-i-1]
        if l.isdigit():
            d = d + l
            break
    cvs.append(d)

for cv in cvs:
    answer = answer + int(cv)

print(answer)
