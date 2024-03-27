def print_power(num1: int, num2: int) -> None:
    print(num1 ** num2)


a, b = map(int, input().split())
print_power(a, b)