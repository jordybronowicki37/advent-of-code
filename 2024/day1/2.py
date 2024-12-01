file = open("input", "r")
left_list = []
right_list = []
similarity_score = 0

for line in file:
    line = line.replace("\n", "")
    numbers = line.split("   ")
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))


for i in range(len(left_list)):
    left = left_list[i]
    occurrences = right_list.count(left)
    similarity = left * occurrences
    similarity_score += similarity

print(similarity_score)
