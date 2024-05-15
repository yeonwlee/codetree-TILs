def is_within_range(value, target):
    return abs(value - target) <= 2 or abs(value - target) >= max_number_of_range - 2


def is_valid_combi(combi, first_combi, second_combi):
    return (all(is_within_range(combi[i], first_combi[i]) for i in range(3)) 
            or all(is_within_range(combi[i], second_combi[i]) for i in range(3)))


max_number_of_range = int(input())
first_combi = tuple(map(int, input().split()))
second_combi = tuple(map(int, input().split()))

num_of_valid_combi = 0

for first in range(1, max_number_of_range + 1):
    for second in range(1, max_number_of_range + 1):
        for third in range(1, max_number_of_range + 1):
            cur_combi = (first, second, third)
            if is_valid_combi(cur_combi, first_combi, second_combi):
                num_of_valid_combi += 1



print(num_of_valid_combi)