number, number_type_to_trans = map(int, input().split())


def change_decimal_number_type(source, number_type_to_trans) ->int:
    number: int = source
    result: list[int] = []
    while number > number_type_to_trans:
        number, remain = divmod(number, number_type_to_trans)
        result.append(remain)
    result.append(number)
    return result[::-1]


for number in change_decimal_number_type(number, number_type_to_trans):
    print(number, end="")