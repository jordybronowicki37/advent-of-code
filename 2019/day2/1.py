file = open("input", "r")

current_index = 0

line = file.readline().replace("\n", "")
nums = [int(n) for n in line.split(",")]

nums[1] = 12
nums[2] = 2

while True:
    opcode = nums[current_index]
    if opcode == 99:
        break
    elif opcode == 1:
        index_input1 = nums[current_index + 1]
        index_input2 = nums[current_index + 2]
        index_output = nums[current_index + 3]
        nums[index_output] = nums[index_input1] + nums[index_input2]
    elif opcode == 2:
        index_input1 = nums[current_index + 1]
        index_input2 = nums[current_index + 2]
        index_output = nums[current_index + 3]
        nums[index_output] = nums[index_input1] * nums[index_input2]
    else:
        raise AttributeError()

    current_index += 4

print(nums[0])
