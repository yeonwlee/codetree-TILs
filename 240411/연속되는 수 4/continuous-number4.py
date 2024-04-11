num_of_numbers = int(input())
prev_number = int(input())
longest_streak = current_streak = 1

for _ in range(1, num_of_numbers):
    current_number = int(input())
    if prev_number < current_number:
        current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    else:
        current_streak = 1
    prev_number = current_number

print(longest_streak)