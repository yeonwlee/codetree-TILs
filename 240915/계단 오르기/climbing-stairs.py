num = int(input())

# top-down
# def count_case(cur_num:int, memo:dict[int, int]={}) -> int:
#     if cur_num in memo:
#         return memo[cur_num]
#     if cur_num < 0:
#         return 0
#     elif cur_num == 0:
#         return 1
#     memo[cur_num] = count_case(cur_num - 2) + count_case(cur_num - 3)
#     return memo[cur_num] % 10007
# print(count_case(num))


# bottom-up
dp = [0] * (num + 1)
dp[2] = 1
dp[3] = 1
for cur_num in range(4, num + 1):
    dp[cur_num] = dp[cur_num - 2] + dp[cur_num - 3] 

print(dp[num] % 10007)