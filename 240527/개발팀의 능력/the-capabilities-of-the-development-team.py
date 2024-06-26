# 2 / 2 / 1 팀
# 최대 능력 팀과 최소능력 팀간 능력차이가 최소이되, 모든 팀의 능력치를 다르게

# devs = list(map(int, input().split()))

# possibile_team_for_two = []
# all_capabilty = sum(devs)
# difference = float('inf')

# for first in range(len(devs) - 1):
#     for second in range(first + 1, len(devs)):
#         possibile_team_for_two.append({first, second})

# for first_team in possibile_team_for_two:
#     for second_team in possibile_team_for_two:
#         if not first_team & second_team:
#             first_team_sum = sum(devs[x] for x in first_team)
#             second_team_sum = sum(devs[x] for x in second_team) 
#             third_team_sum = all_capabilty - first_team_sum - second_team_sum
#             if first_team_sum == second_team_sum or second_team_sum == third_team_sum or first_team_sum == third_team_sum:
#                 continue
#             best = max([first_team_sum, second_team_sum, third_team_sum])
#             worst = min([first_team_sum, second_team_sum, third_team_sum])
#             difference = min(difference, best - worst)

# if difference == float('inf'):
#     print(-1)
# else:
#     print(difference)


# itertools 및 filter 활용

from itertools import combinations

devs = list(map(int, input().split()))

# combinations로 생성된 객체는 이터레이터로 사용시 데이터가 소진됨. -> 리스트화
possibile_team_for_two = list(combinations(range(len(devs)), 2))
all_capabilty = sum(devs)
difference = float('inf')

for first_team in possibile_team_for_two:
    for second_team in filter(lambda x: not (set(x) & set(first_team)), possibile_team_for_two):
        first_team_sum = sum(devs[x] for x in first_team)
        second_team_sum = sum(devs[x] for x in second_team) 
        third_team_sum = all_capabilty - first_team_sum - second_team_sum
        if first_team_sum == second_team_sum or second_team_sum == third_team_sum or first_team_sum == third_team_sum:
            continue
        best = max([first_team_sum, second_team_sum, third_team_sum])
        worst = min([first_team_sum, second_team_sum, third_team_sum])
        difference = min(difference, best - worst)

if difference == float('inf'):
    print(-1)
else:
    print(difference)