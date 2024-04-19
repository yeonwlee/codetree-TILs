num_of_numbers = int(input())
numbers = list(map(int, input().split()))

# min_value = min(numbers)
# count = sum(1 for num in numbers if num == min_value) 
# print(min_value, count)


min_value = float('inf')
count = 0

for num in numbers:
    if num < min_value:
        min_value = num
        count = 1
    elif num == min_value:
        count += 1

print(min_value, count)