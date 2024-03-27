def calculate(num1: int, num2: int)-> tuple[int]:
    if num1 > num2:
        num1 *= 2
        num2 += 10
    else:
        num1 += 10
        num2 *= 2
    return num1, num2


a, b = map(int, input().split())
a, b = calculate(a, b)
print(a, b)