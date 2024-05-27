# 팀원들의 능력 총합이 가장 큰 팀과 가장 작은 팀의 차이 최소화 -> 되도록 평균치에 가깝게 
# 정렬해서 양 끝에서부터 주면 안 되나? -- 예외적인 경우가 있을까?
# 풀이1
# devs = list(map(int, input().split()))

# devs.sort()
# teams = []

# for index in range(len(devs) // 2):
#     teams.append(devs[index] + devs[len(devs) - 1 - index])

# print(max(teams) - min(teams))


## 풀이2: 조합 활용
from itertools import combinations

devs = list(map(int, input().split()))

dev_combi = list(map(set, combinations(range(6), 2)))
difference = float('inf')

for combi in dev_combi:
    for combi2 in dev_combi:
        if combi & combi2:
            continue
        for combi3 in dev_combi:
            if combi & combi3 or combi2 & combi3:
                continue
            sums = [sum(devs[x] for x in combi), sum(devs[x] for x in combi2), sum(devs[x] for x in combi3)]  
            best = max(sums)
            worst = min(sums)
            difference = min(difference, best - worst)


print(difference)