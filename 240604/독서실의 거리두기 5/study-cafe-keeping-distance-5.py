import sys

input = sys.stdin.readline

num_of_seat = int(input().rstrip())
seat_info = list(input().rstrip())

max_distance_of_nearest: int = 0

for index, seat in enumerate(seat_info):
    if seat == '1': # 이미 앉아 있는 자리면 건너뜀
        continue
    seat_info[index] = '1'
    distances = set()
    for first in range(len(seat_info) - 1):
        if seat_info[first] == '1':
            for second in range(first + 1, len(seat_info)):
                if seat_info[second] == '1':
                    distances.add(second - first)
                    break
    max_distance_of_nearest = max(max_distance_of_nearest, min(distances))

    seat_info[index] = '0' # 원복

print(max_distance_of_nearest)