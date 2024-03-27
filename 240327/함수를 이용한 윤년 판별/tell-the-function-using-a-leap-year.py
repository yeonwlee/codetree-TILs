def is_yunnyun(year: int) -> str:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return "false"
        return "true"
    return "false"


year = int(input())
print(is_yunnyun(year))