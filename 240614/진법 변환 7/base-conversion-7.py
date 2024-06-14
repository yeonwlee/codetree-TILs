import math

def get_decimal_bin(decimal:float) -> int:
 
    return

number = float(input())
length_of_decimal = len(str(number).split('.')[-1])
decimal_answer = []
decimal = number % 1
while len(decimal_answer) != 4:
    decimal = math.trunc(decimal * pow(10, length_of_decimal)) / pow(10, length_of_decimal)
    num_pos, decimal = divmod(decimal * 2, 1)
    decimal_answer.append(str(int(num_pos)))

answer = bin(math.trunc(number))[2:] + '.' + ''.join(decimal_answer)
print(answer)