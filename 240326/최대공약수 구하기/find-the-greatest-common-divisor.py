import math


def print_gcd(num1, num2) -> None:
    print(math.gcd(num1, num2))


num1, num2 = map(int, input().split())
print_gcd(num1, num2)