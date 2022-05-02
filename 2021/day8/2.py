file = open("input", "r")
output = 0


def check_wires(tips, digits):
    global output
    zero = ""
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""

    num235 = []
    num069 = []

    for i in tips:
        i = "".join(sorted(i))
        if len(i) == 2:
            one = i
        elif len(i) == 3:
            seven = i
        elif len(i) == 4:
            four = i
        elif len(i) == 5:
            num235.append(i)
        elif len(i) == 6:
            num069.append(i)
        elif len(i) == 7:
            eight = i
        else:
            print("huh?")

    # find 3
    for i in range(len(num235)):
        t = 0
        for j in num235[i]:
            if j in seven:
                t += 1
        if t == 3:
            three = num235[i]
            break
    num235.remove(three)

    # find 6
    for i in num069:
        t = 0
        for j in i:
            if j in seven:
                t += 1
        if t == 2:
            six = i
            break
    num069.remove(six)

    # find 0, 9
    for i in num069:
        amount_of_4_matching = 0
        for j in num235:
            t = 0
            for k in j:
                if k in i:
                    t += 1
            if t == 4:
                amount_of_4_matching += 1
        if amount_of_4_matching == 2:
            zero = i
            break
    num069.remove(zero)
    nine = num069[0]

    # find 2,5
    for i in num235:
        t = 0
        for j in i:
            if j in nine:
                t += 1
        if t == 5:
            five = i
    num235.remove(five)
    two = num235[0]

    display = ""

    for i in digits:
        i = "".join(sorted(i))
        if i == zero:
            display += "0"
        elif i == one:
            display += "1"
        elif i == two:
            display += "2"
        elif i == three:
            display += "3"
        elif i == four:
            display += "4"
        elif i == five:
            display += "5"
        elif i == six:
            display += "6"
        elif i == seven:
            display += "7"
        elif i == eight:
            display += "8"
        elif i == nine:
            display += "9"
        else:
            print("niet herkend")

    output += int(display)


for line in file:
    line = line.replace("\n", "")
    check_wires(line.split(" | ")[0].split(" "), line.split(" | ")[1].split(" "))

print(output)
