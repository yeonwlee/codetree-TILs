def print_stars(number: int) -> None:
    if 1 > number:
        return
    
    print_stars(number - 1)
    print("*" * number)


num_of_rows = int(input())
print_stars(num_of_rows)