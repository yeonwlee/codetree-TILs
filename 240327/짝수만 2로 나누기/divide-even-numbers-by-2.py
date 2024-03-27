n = int(input())

number_arr = map(int, input().split())
for cur_num in number_arr:
    if cur_num % 2 == 0:
        print(cur_num // 2, end=" ")
    else:
        print(cur_num, end=" ")