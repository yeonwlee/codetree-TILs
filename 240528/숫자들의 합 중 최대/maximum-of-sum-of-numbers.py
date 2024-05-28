# start_num 이상 end_num 이하
start_num, end_num = map(int, input().split())

print(max([sum(map(int, str(number))) for number in range(start_num, end_num + 1)]))