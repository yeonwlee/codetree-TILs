from itertools import permutations


def is_pretty_number(cur_pretty_index:int, num_for_checking:int) -> bool:
    for pretty_nums in pretties:
        if pretty_nums[cur_pretty_index] == num_for_checking:
            return True
    return False


len_numbers1, len_numbers2 = map(int, input().split())

numbers1 = list(map(int,input().split()))
numbers2 = list(map(int,input().split()))
pretties = list(permutations(numbers2, len(numbers2)))
answer_count = 0

for start_index in range(len(numbers1) - len(numbers2) + 1):
    pretty_index = 0
    for cur_range_index in range(start_index, start_index + len(numbers2)):
        if is_pretty_number(pretty_index, numbers1[cur_range_index]):
            pretty_index += 1
    if pretty_index == len(numbers2):
        answer_count += 1

print(answer_count)