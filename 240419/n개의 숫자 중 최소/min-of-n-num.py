num_of_numbers = int(input())
numbers = list(map(int, input().split()))

min_value = min(numbers)
count = sum(1 for num in numbers if num == min_value) 
print(min_value, count)