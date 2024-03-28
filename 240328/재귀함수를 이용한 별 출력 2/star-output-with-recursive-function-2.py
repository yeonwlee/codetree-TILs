def print_stars(number: int) -> None:
    if 1 > number:
        return

    print("* " * number)
    print_stars(number - 1)
    print("* " * number) 


number = int(input())
print_stars(number)