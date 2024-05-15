# def is_within_range(value, target):
#     return abs(value - target) <= 2 or abs(value - target) >= max_number_of_range - 2


# def is_valid_combi(combi, first_combi, second_combi):
#     return (all(is_within_range(combi[i], first_combi[i]) for i in range(3)) 
#             or all(is_within_range(combi[i], second_combi[i]) for i in range(3)))


# max_number_of_range = int(input())
# first_combi = tuple(map(int, input().split()))
# second_combi = tuple(map(int, input().split()))

# num_of_valid_combi = 0

# for first in range(1, max_number_of_range + 1):
#     for second in range(1, max_number_of_range + 1):
#         for third in range(1, max_number_of_range + 1):
#             cur_combi = (first, second, third)
#             if is_valid_combi(cur_combi, first_combi, second_combi):
#                 num_of_valid_combi += 1



# print(num_of_valid_combi)


### 시간 줄여보기(답안)
n = int(input())
a, b, c = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))

# 모든 조합을 다 만들어 봅니다.
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # 모든 자리가 주어진 첫 조합과의 거리가 2 이내인지 확인합니다.
            if (abs(a - i) <= 2 or abs(a - i) >= n - 2) and (abs(b - j) <= 2 or abs(b - j) >= n - 2) and \
               (abs(c - k) <= 2 or abs(c - k) >= n - 2):
                cnt += 1
			
			# 모든 자리가 주어진 두 번째 조합과의 거리가 2 이내인지 확인합니다.
            elif (abs(a2 - i) <= 2 or abs(a2 - i) >= n - 2) and (abs(b2 - j) <= 2 or abs(b2 - j) >= n - 2) and \
               (abs(c2 - k) <= 2 or abs(c2 - k) >= n - 2):
                cnt += 1

print(cnt)