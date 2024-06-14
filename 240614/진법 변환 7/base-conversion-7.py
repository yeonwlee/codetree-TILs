import math

# # 풀이 1: 다소 장황
# number = float(input())
# length_of_decimal = len(str(number).split('.')[-1])
# decimal_answer = []
# decimal = number % 1
# while len(decimal_answer) != 4:
#     decimal = math.trunc(decimal * pow(10, length_of_decimal)) / pow(10, length_of_decimal)
#     num_pos, decimal = divmod(decimal * 2, 1)
#     decimal_answer.append(str(int(num_pos)))

# answer = bin(math.trunc(number))[2:] + '.' + ''.join(decimal_answer)
# print(answer)

# 풀이2: 뺄셈을 활용해보자
number = float(input())
num_pos = math.trunc(number)
answer = bin(num_pos)[2:] # 전체를 모을 문자열

decimal_answer = [] # 소수부
while len(decimal_answer) != 4:
    decimal = number - num_pos
    number = decimal * 2    
    num_pos = math.trunc(number)
    decimal_answer.append(str(num_pos))

print(answer + '.' + ''.join(decimal_answer))