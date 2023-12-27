file = open("input", "r")

history_lines = []
answer = 0


def check_all_zeros(l):
    for i in l:
        if i != 0:
            return False
    return True


for line in file:
    line = line.replace("\n", "").split(" ")
    history_lines.append(list(map(int, line)))

for hl in history_lines:
    entire_history = [hl]

    while not check_all_zeros(entire_history[-1]):
        new_line = []
        for i, a in enumerate(entire_history[-1]):
            if i == 0:
                continue
            new_line.append(a - entire_history[-1][i-1])
        entire_history.append(new_line)

    new_num = 0
    for j in range(len(entire_history)):
        new_num = entire_history[-j-1][0] - new_num
    answer += new_num

print(answer)
