# def is_yunnyun(year: int) -> str:
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return "false"
#         return "true"
#     return "false"


# year = int(input())
# print(is_yunnyun(year))


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #100으로 나누어 떨어지되 400으로 나누어 떨어지지 않는 해는 평년


year = int(input())
print("true" if is_leap_year(year) else "false")