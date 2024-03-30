num_of_numbers, nth = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[nth - 1])