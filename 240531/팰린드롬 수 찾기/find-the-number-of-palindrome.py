num1, num2 = map(int, input().split())

min_num = str(num1)
max_num = str(num2)
numbers= []

for cur_max_pos in range(len(min_num), len(max_num) + 1):
    cur_numbers = []
    cur_number = [0 for _ in range(cur_max_pos)]
    left_index = 0
    right_index = cur_max_pos - 1
    while left_index < right_index:
        for cur_pos_num in range(0, 10):
            cur_number[left_index], cur_number[right_index] = cur_pos_num, cur_pos_num
            cur_numbers.append(cur_number.copy())
        left_index += 1
        right_index -= 1
    if cur_max_pos % 2 == 1:
        for nums in cur_numbers:
            for cur_pos_num in range(0, 10):
                nums[cur_max_pos // 2] = cur_pos_num
                numbers.append(nums.copy())
    else:
        numbers.extend(cur_numbers)
    
print(sum(1 for nums in numbers if int(min_num) <= int(''.join(map(str, nums))) <= int(max_num)))