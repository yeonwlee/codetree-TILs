num_of_numbers, num_of_picked = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = float('-inf')
for start_index in range(num_of_numbers - num_of_picked + 1):
    max_sum = max(max_sum, sum(numbers[start_index: start_index + num_of_picked]))

print(max_sum)