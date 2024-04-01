n = int(input())
numbers = list(map(int, input().split()))

cur_numbers = [numbers[0]]
mid_numbers = [numbers[0]]

for index in range(1, len(numbers),2):
    cur_numbers.append(numbers[index])
    cur_numbers.append(numbers[index + 1])
    cur_numbers = sorted(cur_numbers)
    mid_numbers.append(cur_numbers[len(cur_numbers) // 2])

for mid in mid_numbers:
    print(mid,end=" ")