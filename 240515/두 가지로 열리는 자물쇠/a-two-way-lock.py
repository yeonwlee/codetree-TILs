def find_valid_value(cur_value:int) -> set[int]:
    valid_set = set([cur_value])
    for value in range(1, 3):
        valid_set.add((cur_value + value + max_number_of_range) % max_number_of_range)
        valid_set.add((cur_value - value + max_number_of_range) % max_number_of_range)
    return valid_set

def check_valid_combi(base_combi:tuple[int], cur_combi:tuple[int]) -> bool:
    return all(base_value in find_valid_value(cur_value) for base_value, cur_value in zip(base_combi, cur_combi))


max_number_of_range = int(input())
first_combi = tuple(map(int, input().split()))
second_combi = tuple(map(int, input().split()))

num_of_valid_combi = 0

for first in range(1, max_number_of_range + 1):
    for second in range(1, max_number_of_range + 1):
        for third in range(1, max_number_of_range + 1):
            cur_combi = (first, second, third)
            if (check_valid_combi(first_combi, cur_combi) 
                or check_valid_combi(second_combi, cur_combi)):
                    num_of_valid_combi += 1


print(num_of_valid_combi)