from itertools import zip_longest


def sum_each_position(num1:str, num2:str, num3:str) -> int:
    rev_num1, rev_num2, rev_num3 = map(reversed, [num1, num2, num3])
    for cur_pos in zip_longest(rev_num1, rev_num2, rev_num3, fillvalue='0'): # 하나의 자릿수가 짧아도 다른 수끼리는 자리수를 합할 수 있도록 zip_longest사용
        if sum(map(int, cur_pos)) >= 10:
            return -1 # 숫자의 범위가 모두 양수이기 때문에, 합해서 -1이 나올 일이 없음
    return sum(map(int, [num1, num2, num3]))


# 조건상, 입력으로 주어지는 숫자가 모두 다름. 
# 서로 다른 3개의 숫자를 고른다고 했을 때, 다른 인덱스에 있는 숫자를 고르기만 하면 됨

# 유의할 점: 각 인덱스의 최대 자릿수가 다를 수 있음

num_of_numbers = int(input())

# 추후 zip으로 편리하게 풀기 위해 str로 받음
numbers = [
    input()
    for _ in range(num_of_numbers)
]

max_value = float('-inf')
for first_num_index in range(num_of_numbers - 2):
    for second_num_index in range(first_num_index + 1, num_of_numbers - 1):
        for third_num_index in range(second_num_index + 1, num_of_numbers):
            max_value = max(max_value, 
                            sum_each_position(numbers[first_num_index], numbers[second_num_index], numbers[third_num_index]))


print(max_value)