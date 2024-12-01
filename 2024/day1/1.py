file = open("input", "r")
left_list = []
right_list = []
total_distance = 0

for line in file:
    line = line.replace("\n", "")
    numbers = line.split("   ")
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    left = left_list[i]
    right = right_list[i]
    distance = abs(right - left)
    total_distance += distance

print(total_distance)
