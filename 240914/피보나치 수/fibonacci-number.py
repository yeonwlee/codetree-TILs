num = int(input())
dp = [-1] * (num + 1)
dp[1], dp[2] = 1, 1

for cur_num in range(3, num + 1):
    dp[cur_num] = dp[cur_num - 1] + dp[cur_num - 2]

print(dp[num])