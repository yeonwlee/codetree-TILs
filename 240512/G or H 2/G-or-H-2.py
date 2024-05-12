from collections import Counter


def check_values(left_index:int, right_index:int) -> int:
    cur_target_range = pos_info[left_index:right_index + 1]
    counter = Counter(cur_target_range)
    if None in counter:
        del counter[None] # None인 경우 삭제
    if len(counter) == 1 or counter['G'] == counter['H']:
        non_none_indices = [i for i, x in enumerate(cur_target_range) if x is not None]
        if non_none_indices:
            return non_none_indices[-1] - non_none_indices[0] # 실제 길이 반환
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
        pos_info[position] = info

    max_result = 0
    for start_pos in range(len(pos_info)):
        for end_pos in range(len(pos_info) - 1, start_pos - 1, -1):
            if result:=check_values(start_pos, end_pos):
                max_result = max(result, max_result)

    print(max_result)