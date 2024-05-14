num_of_numbers, target_num = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적합 만들기
# cumulative_sum = list(itertools.accumulate(numbers))
cumulative_sum_arr = []
current_sum = 0
for num in numbers:
    current_sum += num
    cumulative_sum_arr.append(current_sum)

difference_value_with_target_num = 10001
for except_num1_index in range(num_of_numbers):
    sum_except_num1 = cumulative_sum_arr[-1] - numbers[except_num1_index]
    for except_num2_index in range(except_num1_index + 1, num_of_numbers):
        difference_value_with_target_num = min(difference_value_with_target_num, abs(target_num - (sum_except_num1 - numbers[except_num2_index])))

print(difference_value_with_target_num)