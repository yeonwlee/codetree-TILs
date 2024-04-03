days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

month1, day1, month2, day2 = map(int, input().split())
day_difference = (sum(days_in_month[:month2]) + day2) - (sum(days_in_month[:month1]) + day1)
print(days_of_week[day_difference % 7])