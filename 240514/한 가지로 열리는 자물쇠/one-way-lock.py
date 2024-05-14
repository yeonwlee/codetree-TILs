##### product를 사용한 풀이
# from itertools import product

# num_max_range = int(input())
# target_combination = tuple(map(int, input().split()))
# access_difference = 2 # 한 자리라도 2 이내로 차이가 나야함

# answer_count = 0
# for cur_combination in product([num for num in range(1, num_max_range + 1)], repeat=3):
#     if any(1 for cur_value, condition_value in zip(cur_combination, target_combination) if abs(condition_value - cur_value) <= 2):
#         answer_count += 1

# print(answer_count)

num_max_range = int(input())
target_combination = tuple(map(int, input().split()))
access_difference = 2 # 한 자리라도 2 이내로 차이가 나야함

answer_count = 0
for num1 in range(1, num_max_range + 1):
    for num2 in range(1, num_max_range + 1):
        for num3 in range(1, num_max_range + 1):
            if any(abs(cur_value - condition_value) <= 2 for cur_value, condition_value in zip([num1, num2, num3], target_combination)):
                answer_count += 1

print(answer_count)