num = int(input())

def count_case(cur_num:int, memo:dict[int, int]={}) -> int:
    if cur_num in memo:
        return memo[cur_num]
    if cur_num < 0:
        return 0
    elif cur_num == 0:
        return 1
    memo[cur_num] = count_case(cur_num - 2) + count_case(cur_num - 3)
    return memo[cur_num] % 10007


print(count_case(num))