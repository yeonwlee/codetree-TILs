#가장 작은 값을 찾아서 맨 좌측으로 이동시키거나
#가장 큰 값을 찾아서 맨 우측으로 이동시키거나

num_of_numbers = int(input())
numbers = list(map(int, input().split()))

for index in range(len(numbers) - 1): #마지막 요소는 확인할 필요가 없음
    min_index = index
    for cur_comparing_index in range(index + 1, len(numbers)):
        if numbers[min_index] > numbers[cur_comparing_index]:
            min_index = cur_comparing_index
    numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

print(" ".join(map(str, numbers)))