a, b = map(int, input().split())
odd_numbers_in_between = list(number for number in range(a, b + 1) if number % 2 == 1)
for odd_number in odd_numbers_in_between:
    print(odd_number, end=" ")