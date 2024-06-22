file = open("input", "r")
line = file.readline().replace("\n", "").split("-")
under_bound = int(line[0])
upper_bound = int(line[1])
amount = 0


def check_double_number(number):
    num = 0
    amount = 0
    for digit in str(number):
        if digit == num:
            amount += 1
        elif amount == 2:
            return True
        else:
            num = digit
            amount = 1
    return amount == 2


def check_increasing_number(number):
    last_num = 0
    for digit in str(number):
        digit = int(digit)
        if digit >= last_num:
            last_num = digit
        else:
            return False
    return True


for i in range(under_bound, upper_bound):
    if not check_increasing_number(i):
        continue
    if not check_double_number(i):
        continue
    amount += 1

print(amount)
