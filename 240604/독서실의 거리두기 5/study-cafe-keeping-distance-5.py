# ## 풀이1: 매번 확인하는 완전탐색
# import sys

# input = sys.stdin.readline

# num_of_seat = int(input().rstrip())
# seat_info = list(input().rstrip())

# max_distance_of_nearest: int = 0

# for index, seat in enumerate(seat_info):
#     if seat == '1': # 이미 앉아 있는 자리면 건너뜀
#         continue
#     seat_info[index] = '1'
#     distances = set()
#     for first in range(len(seat_info) - 1):
#         if seat_info[first] == '1':
#             for second in range(first + 1, len(seat_info)):
#                 if seat_info[second] == '1':
#                     distances.add(second - first)
#                     break
#     max_distance_of_nearest = max(max_distance_of_nearest, min(distances))

#     seat_info[index] = '0' # 원복

# print(max_distance_of_nearest)

## 풀이2: 시간복잡도 줄이기
import sys

input = sys.stdin.readline

num_of_seat = int(input().rstrip())
seat_info = list(input().rstrip())

max_distance_of_nearest: int = 0

# 문제 조건상, 아무도 안 앉아있는 경우는 없음.
already_occupied_seat_indexes = [index for index, seat in enumerate(seat_info) if seat == '1']

for index, seat in enumerate(seat_info):
    if seat == '0':
        left_distance = float('inf') if index < already_occupied_seat_indexes[0] else index - max([occupied for occupied in already_occupied_seat_indexes if occupied < index])
        right_distance = float('inf') if index > already_occupied_seat_indexes[-1] else min([occupied for occupied in already_occupied_seat_indexes if occupied > index]) - index
        max_distance_of_nearest = max(max_distance_of_nearest, min(left_distance, right_distance))

print(max_distance_of_nearest)