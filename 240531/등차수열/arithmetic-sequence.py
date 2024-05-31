num_of_numbers = int(input())
numbers = list(map(int, input().split()))
 
max_count_of_arithmetic_sequence = 0

# 1 <= 주어지는 숫자 <= 100
for number in range(1, 101):
    cur_count_of_arithmetic_sequence = 0
    for a_index in range(len(numbers)-1):
        first_num = numbers[a_index]
        for b_index in range(a_index + 1, len(numbers)):
            third_num = numbers[b_index]
            if abs(number - first_num) == abs(third_num - number):
                cur_count_of_arithmetic_sequence += 1
    max_count_of_arithmetic_sequence = max(max_count_of_arithmetic_sequence, cur_count_of_arithmetic_sequence)

print(max_count_of_arithmetic_sequence)