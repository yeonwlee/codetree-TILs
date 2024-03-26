import math


# def print_gcd(num1, num2) -> None:
#     print(math.gcd(num1, num2))


def print_gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):  # min(n, m)부터 1까지 역순으로 반복
        if num1 % i == 0 and num2 % i == 0:
            print(i)  
            break


num1, num2 = map(int, input().split())
print_gcd(num1, num2)