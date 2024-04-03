days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month1, day1, month2, day2 = map(int, input().split())
target_day = input()

day_difference = (sum(days_of_month[:month2]) + day2) - (sum(days_of_month[:month1]) + day1)
end_date_day = days_of_week[day_difference % 7]
is_more_target_day = days_of_week.index(target_day) <= days_of_week.index(end_date_day)
print(day_difference // 7 + 1 if is_more_target_day else day_difference // 7)