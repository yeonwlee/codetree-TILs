max_num = int(input())

def print_numbers(number:int) -> None:
    if number < 1:
        return
    print_numbers(number - 2)
    print(number, end=' ')


print_numbers(max_num)