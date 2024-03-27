date_month_has = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def has_it_a_date(month: int, date: int) -> bool:
    if month in date_month_has:
        if 1 <= date <= date_month_has[month]:
            return True
    return False


month, date = map(int, input().split())
print("Yes" if has_it_a_date(month, date) else "No")