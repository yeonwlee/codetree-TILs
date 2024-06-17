def print_even_or_odd(number: int) -> None:
    if number % 2:
        print('odd')
    else:
        print('even')


a, b = map(int, input().split())

print_even_or_odd(a)
print_even_or_odd(b)