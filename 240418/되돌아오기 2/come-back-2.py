def change_direction(cur_direction_index: int, next_direction: int) -> int:
    return (cur_direction_index + next_direction + 4) % 4


commands = input()

#북, 동, 남, 서
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cur_x, cur_y = 0, 0
cur_direction_index = 0 #북쪽
time = 0

for command in commands:
    time += 1
    if command in {"L", "R"}:
        next_direction = -1 if command == "L" else 1 
        cur_direction_index = change_direction(cur_direction_index, next_direction)
    else:
        cur_x, cur_y = cur_x + dxs[cur_direction_index], cur_y + dys[cur_direction_index]
        if cur_x == 0 and cur_y == 0:
            print(time)
            break