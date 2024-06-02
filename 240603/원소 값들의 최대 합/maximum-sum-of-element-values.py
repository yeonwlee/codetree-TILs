import sys

input = sys.stdin.readline

range_of_num, num_of_moving = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum_tracing_values = 0

for start_index in range(range_of_num):
    next_index = start_index
    sum_values = 0
    for _ in range(num_of_moving):
        sum_values += numbers[next_index]
        next_index = numbers[next_index] - 1
    max_sum_tracing_values = max(max_sum_tracing_values, sum_values)
    
print(max_sum_tracing_values)