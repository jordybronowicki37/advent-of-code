file = open("input", "r")

line = file.readline().replace("\n", "")
original_nums = [int(n) for n in line.split(",")]
target = 19690720

for noun in range(100):
    for verb in range(100):
        nums = original_nums.copy()
        current_index = 0
        nums[1] = noun
        nums[2] = verb

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

        if target == nums[0]:
            print(100 * noun + verb)
            exit()

