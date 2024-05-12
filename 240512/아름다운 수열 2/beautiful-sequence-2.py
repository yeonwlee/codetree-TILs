len_numbers1, len_numbers2 = map(int, input().split())

numbers1 = list(map(int,input().split()))
numbers2 = sorted(list(map(int,input().split())))
answer_count = 0

for start_index in range(len(numbers1) - len(numbers2) + 1):
    if sorted(numbers1[start_index:start_index+len(numbers2)]) == numbers2:
        answer_count += 1

print(answer_count)