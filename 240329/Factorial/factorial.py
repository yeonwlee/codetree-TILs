def factorial(number: int) -> int:
    if number <= 1: #조건상 양의 정수만 들어옴
        return 1

    return number * factorial(number - 1)


number = int(input())
print(factorial(number))