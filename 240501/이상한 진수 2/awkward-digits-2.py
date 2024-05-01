#0 이상의 정수 N을 2진법으로 나타낸 뒤, 그 숫자들 중 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때, 
#가능한 숫자 N 중 최댓값을 찾는 프로그램을 작성해보세요.

# 가장 높은 자리의 수 중 0 -> 1로 변경한 후 해당 수를 10진수로 다시 변경하면 되지 않을지
# source = list(input()) # 2진수

# is_changed = False
# for index, position_value in enumerate(source):
#     if position_value == '0':
#         source[index] = '1'
#         is_changed = True
#         break


# if not is_changed: #아무것도 변경되지 않았다는 것은 모든 자리가 1이었음. 제일 낮은 자리수를 0으로 변경
#     source[-1] = '0'


# print(int(''.join(source), 2))


####완전탐색 연습하기


source = list(map(int, list(input()))) # 2진수
maximum_value = float('-inf')

for index in range(len(source)):
    source[index] ^= 1  # XOR 연산을 사용해 숫자를 반전
    current_value = int(''.join(map(str, source)), 2)
    maximum_value = max(maximum_value, current_value)
    source[index] ^= 1  # 원래 상태로 복구

print(maximum_value)