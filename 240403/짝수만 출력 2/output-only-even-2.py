end_num, start_num = map(int, input().split())

while end_num >= start_num:
    print(end_num, end=" ")
    end_num -= 2