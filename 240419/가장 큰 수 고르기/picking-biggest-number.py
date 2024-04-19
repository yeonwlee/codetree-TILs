numbers = list(map(int, input().split()))

# print(max(numbers))

max_num = float('-inf') #문제 조건상으로는 0으로 그냥 초기화해줘도 됨
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)