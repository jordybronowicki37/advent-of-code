file = open("input", "r")
num_safe = 0


def check_numbers(numbers):
    isIncreasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    isDecreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    if not isIncreasing and not isDecreasing:
        return False

    prev_value = None
    for number in numbers:
        if prev_value is None:
            prev_value = number
            continue
        if abs(prev_value - number) > 3:
            return False
        prev_value = number

    return True


for line in file:
    line = line.replace("\n", "")
    numbers = [int(i) for i in line.split(" ")]
    for i in range(len(numbers)):
        partial = numbers.copy()
        partial.pop(i)
        result = check_numbers(partial)
        if result:
            num_safe += 1
            break

print(num_safe)
