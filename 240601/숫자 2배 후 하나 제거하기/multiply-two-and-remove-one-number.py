num_of_numbers = int(input())
numbers = list(map(int, input().split()))

min_answer = float('inf')
for index, number in enumerate(numbers):
    numbers[index] = number * 2 # 하나의 숫자를 선택해 2배

    # 하나의 숫자를 선택해 제거
    for d_index, _ in enumerate(numbers):
        skipped_numbers = [numbers[none_skip_index] for none_skip_index in range(len(numbers)) if d_index != none_skip_index] 
        # 제거 한 후, 인접한 숫자 간의 차의 합
        sum_value = sum(abs(skipped_numbers[cur_index] - skipped_numbers[cur_index + 1]) for cur_index in range(len(skipped_numbers) - 1))
        min_answer = min(min_answer, sum_value)

    numbers[index] = numbers[index] // 2 # 원복
   
print(min_answer)