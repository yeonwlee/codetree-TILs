## 폭탄 번호 별 거리 저장 후 풀이
# from collections import defaultdict
# from itertools import combinations

# num_of_bombs, explosion_distance = map(int, input().split())

# bombs = [
#     int(input())
#     for _ in range(num_of_bombs)
# ]

# bomb_position = defaultdict(set)
# # {폭탄번호: {인덱스},..}
# for index, bomb in enumerate(bombs):
#     bomb_position[bomb].add(index)

# # 폭탄의 번호는 0부터 시작. 폭발할 폭탄 중 번호가 가장 큰 번호를 출력. 없으면 -1
# max_bomb_num = -1
# for bomb_num, bomb_pos in bomb_position.items():
#     if len(bomb_pos) >= 2: # 같은 폭탄의 번호가 2개 이상이면
#         for bomb1, bomb2 in combinations(bomb_pos, 2): # 각 거리(인덱스 별) 거리 조합
#             if abs(bomb1 - bomb2) <= explosion_distance:
#                 max_bomb_num = max(max_bomb_num, bomb_num) # 폭발할 폭탄 중 번호가 가장 큰 번호 갱신

# print(max_bomb_num)


##### 풀이2
num_of_bombs, explosion_distance = map(int, input().split())

bombs = [
    int(input())
    for _ in range(num_of_bombs)
]

# 폭탄의 번호는 0부터 시작. 폭발할 폭탄 중 번호가 가장 큰 번호를 출력. 없으면 -1
max_bomb_num = -1
    
for start_bomb_index in range(num_of_bombs - explosion_distance + 1):
    for compare_bomb_index in range(start_bomb_index + 1, min(start_bomb_index + 1 + explosion_distance, num_of_bombs)):
        if bombs[start_bomb_index] == bombs[compare_bomb_index]:
            max_bomb_num = max(max_bomb_num, bombs[start_bomb_index]) # 폭발할 폭탄 중 번호가 가장 큰 번호 갱신

print(max_bomb_num)