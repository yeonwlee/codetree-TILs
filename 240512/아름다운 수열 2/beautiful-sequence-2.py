len_numbers1, len_numbers2 = map(int, input().split())

numbers1 = list(map(int,input().split()))
numbers2 = list(map(int,input().split()))
answer_count = 0

for start_index in range(len(numbers1) - len(numbers2) + 1):
    arr_for_checking_pretty_num = numbers2[:]
    for cur_range_index in range(start_index, start_index + len(numbers2)):
        if numbers1[cur_range_index] in arr_for_checking_pretty_num:
            arr_for_checking_pretty_num.remove(numbers1[cur_range_index])
    if not arr_for_checking_pretty_num:
        answer_count += 1

print(answer_count)