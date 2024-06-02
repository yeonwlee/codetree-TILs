import sys


def get_min_distance_the_others(new_user_seat:int) -> int:
    left_seats = seat_info[new_user_seat::-1] # 거꾸로 함. find로 제일 가까운 점유된 좌석을 찾기 위함
    right_seats = seat_info[new_user_seat+1:]
    left_one_distance = 0
    right_one_distance = 0
    if (left_one_distance:= str(left_seats).find('1')) != -1: # 왼쪽
        left_one_distance += 1 # 거리
    else:
        left_one_distance = len(left_seats)
    if (right_one_distance:= str(right_seats).find('1')) != -1: # 오른쪽
        right_one_distance += 1 # 거리
    else:
        right_one_distance = len(right_seats)
    return min(left_one_distance, right_one_distance)

input = sys.stdin.readline

num_of_seat: int = int(input().rstrip()) # 모든 좌석의 개수
seat_info: str = input().rstrip() # 공석여부

max_distance = float('-inf')
for new_user_seat in range(num_of_seat):
    max_distance = max(max_distance, get_min_distance_the_others(new_user_seat))

print(max_distance)