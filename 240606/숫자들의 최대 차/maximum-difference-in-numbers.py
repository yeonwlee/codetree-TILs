##################### 풀이1:
# import sys

# input = sys.stdin.readline

# num_of_numbers, max_difference = map(int, input().rstrip().split())
# numbers = [
#     int(input())
#     for _ in range(num_of_numbers)
# ]

# max_valid_choice_count = 0
# # 최소차이: 0 최대차이: max_difference
# for min_num in range(1, 10001): # 조건 범위
#     # min_num을 최소로 가정, numbers에 있는 최소 ~ 최소 + max_difference 범위의 숫자의 갯수를 셈
#     max_valid_choice_count = max(max_valid_choice_count, len(list(filter(lambda x: min_num <= x <= min_num + max_difference, numbers))))

# print(max_valid_choice_count)


##################### 풀이2: 투 포인터 활용하기
import sys

input = sys.stdin.readline

num_of_numbers, max_difference = map(int, input().rstrip().split())
numbers = [
    int(input())
    for _ in range(num_of_numbers)
]

# 정렬
numbers.sort()

max_valid_choice_count: int = 0
left: int = 0
for right in range(len(numbers)): 
    while numbers[right] - numbers[left] > max_difference:
        left += 1
    max_valid_choice_count = max(max_valid_choice_count, right - left + 1)


print(max_valid_choice_count)