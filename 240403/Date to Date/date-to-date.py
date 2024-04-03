month1, date1, month2, date2 = map(int, input().split())

date_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print((sum(date_in_month[:month2 - 1]) + date2) - (sum(date_in_month[:month1 - 1]) + date1))