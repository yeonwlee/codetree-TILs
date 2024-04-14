from itertools import zip_longest

step = 1

def mark_position(position: list[int], command: tuple) -> None:
    time, direction = command
    time = int(time)
    cur_position = position[-1]
    for _ in range(time):
        if direction == "L":
            position.append(cur_position - step)
            cur_position -= step
        else:
            position.append(cur_position + step)
            cur_position += step


#바로 직전에는 다른 위치에 있다가 그 다음번에 같은 위치에 있게 되는 경우 세기
def count_target_state(a_position: list[int], b_position: list[int]) -> int:
    fill_value: int = None
    count = 0
    if len(a_robot_position) < len(b_robot_position):
        fill_value = a_position[-1]
    else:
        fill_value = b_position[-1]
    is_same_position = True
    for a, b in zip_longest(a_position, b_position, fillvalue=fill_value):
        if a == b and is_same_position == False:
            count += 1
            is_same_position = True
        elif a != b:
            is_same_position = False
    return count


a_robot_moving_count, b_robot_moving_count = map(int, input().split())

a_robot_commands = [
    tuple(input().split())
    for _ in range(a_robot_moving_count)
]

b_robot_commands = [
    tuple(input().split())
    for _ in range(b_robot_moving_count)
] 

a_robot_position = [0]
b_robot_position = [0]
a_index = b_index = 0

max_length = max(len(a_robot_commands), len(b_robot_commands))
for _ in range(max_length):
    if a_index < len(a_robot_commands):
        mark_position(a_robot_position, a_robot_commands[a_index])
        a_index += 1
    if b_index < len(b_robot_commands):
        mark_position(b_robot_position, b_robot_commands[b_index])
        b_index += 1


print(count_target_state(a_robot_position, b_robot_position))