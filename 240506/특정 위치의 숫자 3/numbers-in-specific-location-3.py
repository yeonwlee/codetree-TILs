num_of_elements = int(input())
numbers = list(map(int, input().split()))
answer = 0

for index in range(8):
    if index in {2, 4, 7}:
        answer += numbers[index]
    elif index == 6:
        answer -= numbers[index]

print(answer)