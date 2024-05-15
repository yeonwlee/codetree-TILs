def get_difference(team1:int) -> int:
    team2 = sum_whole_capability - team1 
    return abs(team2 - team1)


# 6명을 3명씩 2팀으로 배정. 능력 총합 차이 최소화
devs = list(map(int, input().split()))
sum_whole_capability = sum(devs)
min_difference = float('inf')

for first_dev_index in range(len(devs) - 2):
    for second_dev_index in range(first_dev_index + 1, len(devs) - 1):
        for third_dev_index in range(second_dev_index + 1, len(devs)):
            min_difference = min(min_difference, 
                                get_difference(sum([devs[first_dev_index], devs[second_dev_index], devs[third_dev_index]]))
                            )

print(min_difference)