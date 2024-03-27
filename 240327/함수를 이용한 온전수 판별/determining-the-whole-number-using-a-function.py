# def is_target_value(number: int) -> bool:
#     return number % 2 != 0 and str(number)[-1] != "5" and (number % 3 != 0 or number % 9 == 0)


# a, b = map(int, input().split())
# print(sum(1 for cur_num in range(a, b + 1) if is_target_value(cur_num)))


def is_target_value(number: int) -> bool:
    return number % 2 != 0 and number % 10 != 5 and not (number % 3 == 0 and number % 9 != 0)


a, b = map(int, input().split())
print(sum(1 for cur_num in range(a, b + 1) if is_target_value(cur_num)))