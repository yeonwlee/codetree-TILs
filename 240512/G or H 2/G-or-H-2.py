from collections import Counter


def check_values(left_index:int, right_index:int) -> int:
    cur_target_range = pos_info[left_index:right_index + 1]
    counter = Counter(cur_target_range)
    del counter[None] # None인 경우 삭제
    if len(counter) == 1 or counter['G'] == counter['H']:
        for index in range(len(cur_target_range)):
            if cur_target_range[index] is not None:
                left_index = index
                break
        for index in range(len(cur_target_range) - 1, 0 , -1):
            if cur_target_range[index] is not None:
                right_index = index
                break
        return right_index - left_index
    return None


num_of_person = int(input())
pos_info = [None] * 101

if num_of_person == 1:
    print(0)
else:
    min_position = 101
    max_position = -1
    for _ in range(num_of_person):
        position, info = input().split()
        position = int(position)
        max_position = max(position, max_position)
        min_position = min(position, min_position)
        pos_info[position] = info

    left_index = min_position
    right_index = max_position
    while left_index < right_index - 1:
        if result:=check_values(left_index, right_index):
            break
        if result:=check_values(left_index + 1, right_index):
            break
        if reuslt:=check_values(left_index, right_index - 1):
            break
        left_index += 1
        right_index -= 1

    print(result)