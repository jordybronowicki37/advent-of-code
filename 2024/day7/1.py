import itertools as it

file = open("input", "r")

answer = 0

for line in file:
    line = line.replace("\n", "").split(": ")
    expect_result = int(line[0])
    numbers = [int(n) for n in line[1].split(" ")]

    operants_amount = len(numbers) - 1
    operants_options = it.product(["+", "*"], repeat=operants_amount)
    for operants in operants_options:
        actual_result = numbers[0]
        for v in range(len(operants)):
            op = operants[v]
            if op == "+":
                actual_result += numbers[v+1]
            else:
                actual_result *= numbers[v+1]
        if expect_result == actual_result:
            answer += actual_result
            break

print(answer)
