num1, num2 = map(int, input().split())

count_of_pelindromes = 0

for cur_num in range(num1, num2 + 1):
    str_num = str(cur_num)
    if str_num == str_num[::-1]:
        count_of_pelindromes += 1

print(count_of_pelindromes)