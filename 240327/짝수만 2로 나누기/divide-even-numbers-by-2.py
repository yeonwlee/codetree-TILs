n = int(input())

number_arr = map(int, input().split())
for cur_num in number_arr:
    print(cur_num // 2 if cur_num % 2 == 0 else cur_num, end=" ")