from collections import Counter

num_of_dev = int(input()) # 개발자의 수

dev_working = [
    tuple(map(int, input().split()))
    for _ in range(num_of_dev)
] # 시작 시간, 끝시간, 필요한 컴퓨터의 수

# Counter 객체로 필요한 만큼만 메모리 사용
time = Counter()

for start, end, required_computer in dev_working:
    for working_time in range(start, end + 1):
        time[working_time] += required_computer

# 최대 필요한 컴퓨터의 수
print(max(time.values()))