def has_same_sign(a, b):
    return a * b > 0

num_of_numbers = int(input())
numbers = [int(input()) for _ in range(num_of_numbers)]

longest_streak = current_streak = (1 if numbers else 0)

for i in range(1, num_of_numbers):
    if has_same_sign(numbers[i], numbers[i-1]):
        current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    else:
        current_streak = 1

print(longest_streak)