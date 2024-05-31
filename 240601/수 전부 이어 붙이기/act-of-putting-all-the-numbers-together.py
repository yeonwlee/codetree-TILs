num_of_numbers = int(input())

str_numbers = ''.join(input().split())

for index, char in enumerate(str_numbers, start=1):
    print(char, end='')
    if index % 5 == 0:
        print()