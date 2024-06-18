import sys
from collections import Counter
from collections import defaultdict

input = sys.stdin.readline

num_of_bomb, explosion_distance = map(int, input().rstrip().split())
bombs = [
    int(input().rstrip())
    for _ in range(num_of_bomb)
]

# 가장 많이 터진 폭탄의 정수 출력
# 단, 가장 많이 터진 폭탄이 여러개인 경우, 가장 큰 번호를 출력합니다. 아무 폭탄도 터지지 않을 경우 0을 출력합니다.


# 이미 터진 폭탄을 체크해두면?
exploded_bomb_pos = [0 for _ in range(num_of_bomb)]
explosion_count = defaultdict(int)

for start_index in range(num_of_bomb):
    bomb_counter_in_range = Counter(bombs[start_index:start_index + explosion_distance])
    explosion_bomb_id = {bomb_id for bomb_id, count in bomb_counter_in_range.items() if count >= 2}
    if explosion_bomb_id:
        for cur_pos in range(start_index, start_index + explosion_distance):
            if exploded_bomb_pos[cur_pos] != 1 and bombs[cur_pos] in explosion_bomb_id:
                exploded_bomb_pos[cur_pos] = 1
                explosion_count[bombs[cur_pos]] += 1


if not explosion_count: # 터지는 폭탄에 대한 정보가 아무것도 없음
    print(0)
else:
    explosion_count = Counter(explosion_count)
    sorted_answer = sorted(explosion_count.most_common(), key=lambda x: (x[1], -x[0]))
    print(sorted_answer[0][0])