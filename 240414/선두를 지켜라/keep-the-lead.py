def update_running_info(cur_distance: list[int], data_for_update: tuple) -> None:
    speed, hours = data_for_update
    for _ in range(hours):
        cur_distance.append(cur_distance[-1] + speed)


a_num_of_speed_and_time_data, b_num_of_speed_and_time_data = map(int, input().split())

a_data = [
    tuple(map(int, input().split()))
    for _ in range(a_num_of_speed_and_time_data)
]

b_data = [
    tuple(map(int, input().split()))
    for _ in range(b_num_of_speed_and_time_data)
]


a_cur_distance = [0]
b_cur_distance = [0]
a_index = b_index = 0

max_length = max(len(a_data), len(b_data))

for _ in range(max_length):
    if a_index < len(a_data):
        update_running_info(a_cur_distance, a_data[a_index])
        a_index += 1
    if b_index < len(b_data):
        update_running_info(b_cur_distance, b_data[b_index])
        b_index += 1

cur_first_player = None
# 단, 두 사람이 공동으로 선두를 지키는 경우, 
#어느 한 쪽이 앞서가기 전까지는 선두가 바뀌지 않았다고 판단합니다
changed_first_player_count = 0

for a, b in zip(a_cur_distance, b_cur_distance):
    if cur_first_player is None:
        if a < b:
            cur_first_player = "b"
        elif b < a:
            cur_first_player = "a"
    else:    
        if cur_first_player == "a" and a < b:
            changed_first_player_count += 1
            cur_first_player = "b"
        elif cur_first_player == "b" and b < a:
            changed_first_player_count += 1
            cur_first_player = "a"
            
print(changed_first_player_count)