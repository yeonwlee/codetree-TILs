def is_leap_year(year:int) -> int:
    if year % 4 == 0:
        if year % 100 or year % 400 == 0:
            return 1
    return 0

year = int(input())

print(is_leap_year(year))