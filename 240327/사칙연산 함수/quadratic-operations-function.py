def plus(num1: int, num2: int) -> None:
    print(f"{num1} + {num2} = {num1 + num2}")


def minus(num1: int, num2: int) -> None:
    print(f"{num1} - {num2} = {num1 - num2}")


def divide(num1: int, num2: int) -> None:
    print(f"{num1} / {num2} = {num1 // num2}")


def multiply(num1: int, num2: int) -> None:
    print(f"{num1} * {num2} = {num1 * num2}")


num1, operator, num2 = input().split()
num1, num2 = int(num1), int(num2)
valid_operaters = {"+", "-", "/", "*"}
if operator in valid_operaters:
    if operator == "+":
        plus(num1, num2)
    if operator == "-":
        minus(num1, num2)
    elif operator == "/": #조건상 num2가 0이 될 일은 없음
        divide(num1, num2)
    else:
        multiply(num1, num2)