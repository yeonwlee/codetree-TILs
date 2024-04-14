num1 = int(input())
num2 = int(input())

result = num1 * num2

while num2 >= 1:
    num2, num2_remain = divmod(num2, 10)
    print(num1 * num2_remain)

print(result)