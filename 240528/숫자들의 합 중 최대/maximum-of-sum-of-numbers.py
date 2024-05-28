# start_num 이상 end_num 이하
start_num, end_num = map(int, input().split())

# 범위내의 숫자의 각 자리수를 합한 것 중 가장 큰 값 출력
print(max([sum(map(int, str(number))) for number in range(start_num, end_num + 1)]))