n: int = int(input())

def is_target_num(num):
    if num % 2 == 1: # 홀수면 무조건 false
        return False
    sum_each_position: int = 0
    while num > 0:
        sum_each_position += num % 10 
        num //= 10
    return num % 2 == 0 and sum_each_position % 5 == 0


if is_target_num(n):
    print("Yes")
else:
    print("No")