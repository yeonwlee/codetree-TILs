num_of_numbers, base_number = map(int, input().split())
numbers = list(map(int, input().split()))

if numbers[0] > base_number:
    longest_streak = cur_streak = 1
else:
    longest_streak = cur_streak = 0

for index in range(1, num_of_numbers):
    if numbers[index] > base_number:
        cur_streak += 1
        longest_streak = max(cur_streak, longest_streak)
    else:
        cur_streak = 0

print(longest_streak)