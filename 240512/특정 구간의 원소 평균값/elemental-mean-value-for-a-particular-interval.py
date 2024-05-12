num_of_numbers = int(input())
numbers = list(map(int, input().split()))
answer_count = 0

for start_index in range(len(numbers)):
    for end_index in range(start_index + 1, len(numbers)):
        cur_range_numbers = numbers[start_index:end_index]
        set_cur_range_numbers = set(cur_range_numbers) 
        if sum(cur_range_numbers) // len(cur_range_numbers) in set_cur_range_numbers:
            answer_count += 1

print(answer_count)