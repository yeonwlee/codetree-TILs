a_position = [0]
b_position = [0]
step = 1

def check_they_are_same_position() -> int:
    for index, (a, b) in enumerate(zip(a_position, b_position)):
        if index != 0 and a == b:
            return index
    return -1
    
def mark_position(command: tuple, mark_flag: str) -> None:
    global a_position
    global b_position

    cur_marking_target = None
    if mark_flag == "a":
        cur_marking_target = a_position
    else:
        cur_marking_target = b_position

    direction, moving_seconds = command
    moving_seconds = int(moving_seconds)

    while moving_seconds:
        if direction == "L":
            cur_marking_target.append(cur_marking_target[-1] - step)
        else:
            cur_marking_target.append(cur_marking_target[-1] + step)
        moving_seconds -= 1    

a_num_of_commands, b_num_of_commands = map(int, input().split())

a_commands = [
    tuple(input().split())
    for _ in range(a_num_of_commands)
]

b_commands = [
    tuple(input().split())
    for _ in range(b_num_of_commands)
]

a_index = b_index = 0

# while a_index < len(a_commands) and b_index < len(b_commands):
#     mark_position(a_commands[a_index], "a")
#     a_index += 1
#     mark_position(b_commands[b_index], "b")
#     b_index += 1

#     if (same_position:= check_they_are_same_position()) is not None:
#         print(same_position)
#         break

while a_index < len(a_commands):
    mark_position(a_commands[a_index], "a")
    a_index += 1

while b_index < len(b_commands):
    mark_position(b_commands[b_index], "b")
    b_index += 1

print(check_they_are_same_position())