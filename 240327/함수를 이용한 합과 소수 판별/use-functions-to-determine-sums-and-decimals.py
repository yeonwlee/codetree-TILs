import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for num_for_division in range(2, int(math.sqrt(number)) + 1):
        if number % num_for_division == 0:
            return False
    return True


def sum_every_num_position(number: int) -> int:
    return sum(int(cur_num) for cur_num in str(number)) 


a, b = map(int, input().split())
print(sum(1 for num in range(a, b + 1) if is_prime(num) and sum_every_num_position(num) % 2 == 0))