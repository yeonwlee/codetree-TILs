num = int(input())
dp = [0] * (num + 1)
dp[1] = 1

for cur_num in range(2, num + 1):
    dp[cur_num] = dp[cur_num - 1] + dp[cur_num - 2]

print(dp[num])