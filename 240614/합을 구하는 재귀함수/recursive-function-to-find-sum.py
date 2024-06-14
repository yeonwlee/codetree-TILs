number = int(input())

def get_sum_value(number:int) -> int:
    if number > 100:
        return 0
    return number + get_sum_value(number + 2)


print(get_sum_value(number))