n = int(input())

number_arr = map(int, input().split())
abs_number_arr = [abs(cur_num) for cur_num in number_arr]
for abs_number in abs_number_arr:
    print(abs_number, end=" ")