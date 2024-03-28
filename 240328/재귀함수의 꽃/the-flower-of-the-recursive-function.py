def print_numbers(number: int) -> None:
    if 1 > number: 
        return

    print(number, end=" ")
    print_numbers(number - 1)
    print(number, end=" ")


number = int(input())
print_numbers(number)