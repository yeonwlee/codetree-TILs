from collections import defaultdict
from functools import reduce 

num_of_person, num_of_cheese, num_of_eating_cheese_record, num_of_sick_record = map(int, input().split())

eating_cheese_record = [
    tuple(map(int, input().split()))
    for _ in range(num_of_eating_cheese_record)
]

sick_record = [
    tuple(map(int, input().split()))
    for _ in range(num_of_sick_record)
]

suspect_cheese = defaultdict(set)
max_num_of_sick_person = 0

# 치즈는 '하나만' 상했음
# 아픈 사람들이 아프기 시작한 시간 전(최소 -1)에 먹은 치즈가 상했을 수 있음
# 의심되는 치즈를 먹은 사람들의 최대 수 구하기

# 의심되는 치즈 찾기
for sick_info in sick_record:
    person, sick_time = sick_info # index 아님
    suspect_cheese[person].update(cheese for eater, cheese, eating_time in eating_cheese_record if eater == person and eating_time < sick_time)

# 아픈 사람들이 아프기 전에 공통적으로 먹었던 치즈 추려내기
common_suspect_cheeses = reduce(lambda x, y: x & y, suspect_cheese.values())

# 상했을 가능성이 있는 치즈들을 먹은 사람들을 구함.
# 한 사람이 여러 번 먹을 수 있음. 그래서 치즈를 먹은 정보를 단순히 세면 안 됨.
for maybe_rot_cheese in common_suspect_cheeses:
    max_num_of_sick_person = max(max_num_of_sick_person, len({eater for eater, cheese, _ in eating_cheese_record if cheese == maybe_rot_cheese}))

print(max_num_of_sick_person)