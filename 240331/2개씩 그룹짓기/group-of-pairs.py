#겹치지 않게 그룹을 이루도록 하기
#각 그룹에 있는 원소의 합의 최대값이 제일 작아지도록

## 그렇다는 건, 각 그룹간의 합 차이를 작게 만들어야하는 것 같다
# 정렬을 해서 가장 앞, 뒤의 값으로 그룹을 만들되,
# 바로 이전에 만든 그룹과 동일해지는 경우에 대한 추가 처리를 해주기

from collections import deque

num_of_groups = int(input())
numbers = list(map(int, input().split()))
groups: list[int] = [[0, 0]] # 인덱스 오류를 막기 위한 초기화

numbers = deque(sorted(numbers))

for _ in range(len(numbers) // 2): # 조어진 조건 상, 홀수일 일은 없음
    cur_small_value_index: int = 0
    while groups[-1] == [numbers[cur_small_value_index], numbers[-1]]:
        cur_small_value_index += 1
    groups.append([numbers.popleft(), numbers.pop()])

print(max(sum(group) for group in groups))