def sum_powered_number(number: int) -> int:
    #각자리 숫자의 제곱의 합 구하기
    if number < 10:
        return number ** 2

    return ((number % 10) ** 2) + sum_powered_number(number // 10)


number = int(input())
print(sum_powered_number(number))