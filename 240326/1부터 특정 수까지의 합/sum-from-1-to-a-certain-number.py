num = int(input())


def division(num) -> int:
    return sum(cur_num for cur_num in range(1, num + 1)) // 10


print(division(num))