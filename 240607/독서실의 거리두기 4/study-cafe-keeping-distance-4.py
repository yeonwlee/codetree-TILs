def get_nearest_distance()-> int :
    min_distance: int = float('inf')
    left: int = -1 
    for right in range(num_of_seat): # '좌석에 앉은 사람' 간의 최소 거리임. 
        if seat_info[right] == '1':
            if left != -1:
                min_distance  = min(min_distance, right - left)
            left = right

    return min_distance 


# 두 명을 더 집어넣었을 때 가장 가까운 두 사람 간의 거리를 최대로 하고 싶다
num_of_seat = int(input())
seat_info = list(input())
empty_seat_info = [index for index, value in enumerate(seat_info) if value == '0']

max_distance = 0
for first_index, first in enumerate(empty_seat_info):
    seat_info[first] = '1'
    for second in empty_seat_info[first_index + 1:]:
        seat_info[second] = '1'
        max_distance = max(max_distance, get_nearest_distance())
        seat_info[second] = '0'
    seat_info[first] = '0'

print(max_distance)