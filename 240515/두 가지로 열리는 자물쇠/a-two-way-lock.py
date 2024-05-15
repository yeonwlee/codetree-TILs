def find_valid_value(cur_value:int) -> set[int]:
    valid_set = set([cur_value])
    for value in range(-2, 3):
        valid_set.add((cur_value + value - 1) % max_number_of_range + 1)
    return valid_set

def check_valid_combi(valid_nums:list[set[int]], cur_combi:tuple[int]) -> bool:
    return all(cur_value in valid_num_set for valid_num_set, cur_value in zip(valid_nums, cur_combi))


max_number_of_range = int(input())
first_combi = tuple(map(int, input().split()))
second_combi = tuple(map(int, input().split()))

valid_num_at_first_combi = [find_valid_value(num) for num in first_combi]
valid_num_at_second_combi = [find_valid_value(num) for num in second_combi]

num_of_valid_combi = 0

for first in range(1, max_number_of_range + 1):
    for second in range(1, max_number_of_range + 1):
        for third in range(1, max_number_of_range + 1):
            cur_combi = (first, second, third)
            if check_valid_combi(valid_num_at_first_combi, cur_combi) or check_valid_combi(valid_num_at_second_combi, cur_combi):
                num_of_valid_combi += 1



print(num_of_valid_combi)