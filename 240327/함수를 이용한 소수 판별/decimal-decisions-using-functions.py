import math


def is_prime(source_number: int) -> bool:
    if source_number <= 1:
        return False
    for num in range(2, int(math.sqrt(source_number)) + 1):
        if source_number % num == 0:
            return False
    return True


a, b = map(int, input().split())
print(sum(cur_num for cur_num in range(a, b + 1) if is_prime(cur_num)))