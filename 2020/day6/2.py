file = open("input", "r")
answers = ""
group = []
count = 0

for line in file:
    line = line.replace("\n", "")
    if line == "":
        temp = ""
        group_size = len(group)

        for j in answers:
            amount = 0
            for g in group:
                if j in g:
                    amount += 1
            if amount == group_size:
                temp += j

        count += len(temp)
        answers = ""
        group = []
    else:
        group.append(line)
        for i in line:
            if i not in answers:
                answers += i

print(count)
