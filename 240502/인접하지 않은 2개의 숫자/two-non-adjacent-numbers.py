num_of_numbers = int(input())
numbers = list(map(int, input().split()))

max_sum = float('-inf')

for first_num_index in range(len(numbers) - 2): # 인접하지 않은 수끼리 더해야하므로, 뒤에서 3번째 인덱스까지만 돌면 됨
    for second_num in numbers[first_num_index + 1:]:
        max_sum = max(max_sum, numbers[first_num_index] + second_num)

print(max_sum)