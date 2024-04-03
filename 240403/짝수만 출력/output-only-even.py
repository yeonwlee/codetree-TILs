num1, num2 = map(int, input().split())

if num1 % 2 != 0:
    num1 += 1

while num1 <= num2:
    print(num1, end=" ")
    num1 += 2