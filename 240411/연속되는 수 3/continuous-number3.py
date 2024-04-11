num_of_numbers = int(input())
numbers = [
    int(input())
    for _ in range(num_of_numbers)
]

longest_value_count = 0
continued_same_sign_values = []

for index, number in enumerate(numbers):
    if index == 0:
        continued_same_sign_values.append(number)
    else:
        if ((numbers[index - 1] < 0 and number < 0) 
            or (numbers[index - 1] > 0 and number > 0)):
            continued_same_sign_values.append(number)
        else: #달라진 경우
            if longest_value_count < len(continued_same_sign_values):
                longest_value_count = len(continued_same_sign_values)
            continued_same_sign_values = []
            continued_same_sign_values.append(number)

if continued_same_sign_values:
    if longest_value_count < len(continued_same_sign_values):
        longest_value_count = len(continued_same_sign_values)

print(longest_value_count)