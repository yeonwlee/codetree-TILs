num_of_numbers = int(input())
numbers = list(map(int, input().split()))

while True:
    is_sorted = True
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index] 
            is_sorted = False
    if is_sorted:
        break

print(" ".join(map(str, numbers)))