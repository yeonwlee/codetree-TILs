a_base, b_base = map(int, input().split())
number = input()

number_decimal = int(number, a_base)
result: list[int] = []

while number_decimal >= b_base:
    number_decimal, remain = divmod(number_decimal, b_base)
    result.append(remain)
result.append(number_decimal)

for num in reversed(result):
    print(num, end="")