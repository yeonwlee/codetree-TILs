numbers = [
    int(input()) for _ in range(28)
]

numbers.sort()
answers = []

count = 1
for num in numbers:
    if count != num:
        answers.append(count)
        count += 2
    else:
        count += 1

print(answers[0])
print(answers[1])