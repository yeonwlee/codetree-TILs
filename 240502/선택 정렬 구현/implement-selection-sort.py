#가장 작은 값을 찾아서 맨 좌측으로 이동시키거나
#가장 큰 값을 찾아서 맨 우측으로 이동시키거나

num_of_numbers = int(input())
numbers = list(map(int, input().split()))

for index in range(len(numbers)):
    min_value = float('inf')
    min_index = None
    for cur_comparing_index in range(index, len(numbers)):
        if min_value > numbers[cur_comparing_index]:
            min_value = numbers[cur_comparing_index]
            min_index = cur_comparing_index
    numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

print(" ".join(map(str, numbers)))