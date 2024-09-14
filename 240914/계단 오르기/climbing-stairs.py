num = int(input())

def count_case(cur_num:int) -> int:
    if cur_num < 0:
        return 0
    elif cur_num == num:
        return 1

    return count_case(cur_num - 2) + count_case(cur_num - 3)


print(count_case(num))