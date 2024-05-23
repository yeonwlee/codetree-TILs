num_of_devs = int(input())

dev_working_time = [
    tuple(map(int, input().split()))
    for _ in range(num_of_devs)
]

max_sum_working_time = 0

for index in range(len(dev_working_time)):
    check_working_time = [0] * 1000
    remain_devs = dev_working_time[:index] + dev_working_time[index+1:]
    for remain in remain_devs:
        start, end = remain
        for cur_working_time in range(start, end): # 마지막 시간이 포함되지 않게
            check_working_time[cur_working_time] += 1
    max_sum_working_time = max(max_sum_working_time, sum(1 if working_time >= 1 else 0 for working_time in check_working_time))

print(max_sum_working_time)