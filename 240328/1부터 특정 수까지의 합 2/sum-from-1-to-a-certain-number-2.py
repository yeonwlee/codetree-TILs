def sum_numbers(number: int) -> int:
    if number == 1:
        return number
    return number + sum_numbers(number - 1)


number = int(input())
print(sum_numbers(number))