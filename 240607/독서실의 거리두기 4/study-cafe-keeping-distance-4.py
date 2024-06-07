def get_nearest_distance()-> int :
    min_connective_empty_seat: int = float('inf')
    left: int = 0
    for right in range(num_of_seat):
        if any(True if seat == '1' else False for seat in seat_info[left:right + 1]):
            left += 1
        else:
            min_connective_empty_seat = min(min_connective_empty_seat, right - left + 1) # 연속된 빈 좌석의 수

    return min_connective_empty_seat + 1 # 1001 을 예로 들면, 1과 1 사이의 거리는 3임(연속된 빈좌석 수 + 1).


# 두 명을 더 집어넣었을 때 가장 가까운 두 사람 간의 거리를 최대로 하고 싶다
num_of_seat = int(input())
seat_info = list(input())
empty_seat_info = {index for index, value in enumerate(seat_info) if value == '0'}

max_distance = 0
for first in empty_seat_info:
    seat_info[first] = '1'
    for second in empty_seat_info:
        if first == second:
            continue
        seat_info[second] = '1'
        max_distance = max(max_distance, get_nearest_distance())
        seat_info[second] = '0'
    seat_info[first] = '0'

print(max_distance)