hour1, minute1, hour2, minute2 = map(int, input().split())

print((hour2 * 60 + minute2) - (hour1 * 60 + minute1))