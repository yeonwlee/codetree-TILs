date_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
season = {(3, 4, 5): "Spring", (6, 7, 8): "Summer", (9, 10, 11): "Fall", (12, 1, 2): "Winter"}


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or (year % 100 and year % 400 == 0)) 


def is_valid_date(month: int, date: int) -> bool:
    return date <= date_in_month[month] #주어진 조건상 이것으로 충분


year, month, date = map(int, input().split())


if is_leap_year(year):
    date_in_month[2] = 29

if is_valid_date(month, date):
    print([season[target_month] for target_month in season.keys() if month in target_month][0])
else:
    print(-1)