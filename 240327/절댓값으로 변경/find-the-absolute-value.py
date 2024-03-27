n = int(input())

number_arr = map(int, input().split())
for cur_num in number_arr:
    print(abs(cur_num), end=" ")