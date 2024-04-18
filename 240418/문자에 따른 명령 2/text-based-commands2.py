commands = input()

def get_next_direction(cur_direction: int, next_direction: int) -> int:
    return (cur_direction + next_direction + 4) % 4


#북, 동, 남, 서 - 시계방향
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cur_x, cur_y = 0, 0
cur_direction_index = 0
for command in commands:
    if command in {"L", "R"}:
        next_direction = -1 if command == "L" else 1
        cur_direction_index = get_next_direction(cur_direction_index, next_direction)
    else:
        cur_x += dx[cur_direction_index]
        cur_y += dy[cur_direction_index]

print(cur_x, cur_y)