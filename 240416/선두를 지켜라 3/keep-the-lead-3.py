def mark_cur_position(position: list[int], moving_info: tuple[int]) -> None:
    speed, hour = map(int, moving_info)
    cur_position = position[-1]
    for _ in range(hour):
        position.append(cur_position + speed)
        cur_position += speed


a_num_of_moving_info, b_num_of_moving_info = map(int, input().split())

a_position = [0]
b_position = [0]

for _ in range(a_num_of_moving_info):
    mark_cur_position(a_position, tuple(input().split()))

for _ in range(b_num_of_moving_info):
    mark_cur_position(b_position, tuple(input().split()))
    

cur_first_player = None
changed_first_player_count = 0

for index in range(1, len(a_position)): #a_position과 b_position의 길이는 같음. 총 이동한 시간 동일
    if a_position[index] > b_position[index]:
        next_first_player = "A"
    elif a_position[index] < b_position[index]:
        next_first_player = "B"
    else: 
        next_first_player = "AB"
    
    if cur_first_player != next_first_player:
        changed_first_player_count += 1
        cur_first_player = next_first_player

print(changed_first_player_count)