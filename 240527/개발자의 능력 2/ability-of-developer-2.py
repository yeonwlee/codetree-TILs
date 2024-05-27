# 팀원들의 능력 총합이 가장 큰 팀과 가장 작은 팀의 차이 최소화 -> 되도록 평균치에 가깝게 
# 정렬해서 양 끝에서부터 주면 안 되나? -- 예외적인 경우가 있을까?
devs = list(map(int, input().split()))

devs.sort()
teams = []
for index in range(len(devs) - 1, len(devs) // 2 - 1, -1):
    teams.append(devs[index] + devs[len(devs) - 1 - index])

print(max(teams) - min(teams))