step = 1

def check_they_are_same_position() -> int:
    for index, (a, b) in enumerate(zip(a_position, b_position)):
        if index != 0 and a == b:
            return index
    return -1


def mark_position(cur_marking_target: list[int], command: tuple) -> None:
    direction, moving_seconds = command
    moving_seconds = int(moving_seconds)
    for _ in range(moving_seconds):
        if direction == "L":
            cur_marking_target.append(cur_marking_target[-1] - step)
        else:
            cur_marking_target.append(cur_marking_target[-1] + step)


a_num_of_commands, b_num_of_commands = map(int, input().split())

a_commands = [
    tuple(input().split())
    for _ in range(a_num_of_commands)
]

b_commands = [
    tuple(input().split())
    for _ in range(b_num_of_commands)
]

a_position = [0]
b_position = [0]
a_index = b_index = 0

max_length = max(len(a_commands), len(b_commands))
for _ in range(max_length):
    if a_index < len(a_commands):
        mark_position(a_position, a_commands[a_index])
        a_index += 1
    if b_index < len(b_commands):
        mark_position(b_position, b_commands[b_index])
        b_index += 1

    if (same_position:= check_they_are_same_position()) != -1:
        print(same_position)
        break

if same_position == -1:
    print(same_position)