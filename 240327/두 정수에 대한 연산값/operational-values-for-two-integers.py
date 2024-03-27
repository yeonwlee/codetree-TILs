def calculate(a: int, b: int) -> tuple[int]:
    #큰 수에는 25 작은 수에는 2 곱하기
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b    


a, b = map(int, input().split())
a, b = calculate(a, b)
print(a, b)