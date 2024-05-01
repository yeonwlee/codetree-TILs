#0 이상의 정수 N을 2진법으로 나타낸 뒤, 그 숫자들 중 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때, 
#가능한 숫자 N 중 최댓값을 찾는 프로그램을 작성해보세요.

# 가장 높은 자리의 수 중 0 -> 1로 변경한 후 해당 수를 10진수로 다시 변경하면 되지 않을지

source = list(input()) # 2진수

for index, position_value in enumerate(source):
    if position_value == '0':
        source[index] = '1'
        break

print(int(''.join(source), 2))