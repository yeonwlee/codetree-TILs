num_of_numbers = int(input())
numbers = [
    int(input())
    for _ in range(num_of_numbers)
]

cur_longest_length = 0
same_values = []
for index, number in enumerate(numbers):
    if index == 0:
        same_values.append(number)
    else:
        if numbers[index] != numbers[index - 1]:
            if cur_longest_length < len(same_values):
                cur_longest_length = len(same_values)
            same_values = []
            same_values.append(number)
        else:
            same_values.append(number)

if same_values and cur_longest_length < len(same_values):
    cur_longest_length = len(same_values)

print(cur_longest_length)