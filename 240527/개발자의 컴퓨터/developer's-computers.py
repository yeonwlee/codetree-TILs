num_of_dev = int(input())

dev_working = [
    tuple(map(int, input().split()))
    for _ in range(num_of_dev)
]

time = [0] * 1001

for start, end, require_com in dev_working:
    for working_time in range(start, end + 1):
        time[working_time] += require_com

print(max(time))