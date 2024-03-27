date_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or (year % 100 and year % 400 == 0)) 


def is_valid_date(month: int, date: int) -> bool:
    return date <= date_in_month[month] #주어진 조건상 이것으로 충분


def get_season(month: int) -> str:
    if month in {3, 4, 5}:
        return "Spring"
    elif month in {6, 7, 8}:
        return "Summer"
    elif month in {9, 10, 11}:
        return "Fall"
    else:
        return "Winter"


year, month, date = map(int, input().split())

if is_leap_year(year):
    date_in_month[2] = 29

if is_valid_date(month, date):
    print(get_season(month))
else:
    print(-1)