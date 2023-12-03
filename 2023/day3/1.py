file = open("input", "r")

lines = file.readlines()
MAX_X = len(lines[0])
MAX_Y = len(lines)
SYMBOLS = "!@#$%^&*-+=/"
answer = 0


def check_perimeter(x, y, number):
    for y2 in range(3):
        y2 += y - 1
        if y2 < 0 or y2 > MAX_Y - 1:
            continue
        for x2 in range(len(number) + 2):
            x2 += x - 1
            if x2 < 0 or x2 > MAX_X:
                continue
            if lines[y2][x2] in SYMBOLS:
                return True
    return False


for i in range(len(lines)):
    line = lines[i]
    first_col_num_pos = None
    col_nums = ""

    for j in range(len(line)):
        char = line[j]

        if char.isdigit():
            col_nums += char
            if not first_col_num_pos:
                first_col_num_pos = j

        else:
            if not first_col_num_pos:
                continue
            if check_perimeter(first_col_num_pos, i, col_nums):
                answer += int(col_nums)

            # Reset values
            col_nums = ""
            first_col_num_pos = None

print(answer)
