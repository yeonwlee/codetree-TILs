numbers = [
    int(input()) for _ in range(28)
]

numbers.sort()
answers = []

num1 = numbers[0]
for num2 in numbers[1:]:
    if num2 - num1 != 1:
        answers.append(num2 - 1)
    num1 = num2

print(answers[0])
print(answers[1])