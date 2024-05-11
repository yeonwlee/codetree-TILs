def is_within_rect(row:int, col:int) -> bool:
    return 0 <= row < grid_width and 0 <= col < grid_width


grid_width, num_of_commands = map(int, input().split())

commands = input()
grid = [
    list(map(int, input().split()))
    for _ in range(grid_width)
]

# 가운데 위치에서 북쪽을 향한 상태로 움직이는 것을 시작
cur_direction_index = 0
cur_row = cur_col = grid_width // 2
sum_pos_value = grid[cur_row][cur_col] 
# 북 동 남 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for command in commands:
    if command == 'L':
        cur_direction_index = (cur_direction_index - 1 + 4) % 4
    elif command == 'R':
        cur_direction_index = (cur_direction_index + 1) % 4
    else: # 'F'인 경우. 앞으로 전진
        next_row, next_col = cur_row + direction[cur_direction_index][0], cur_col + direction[cur_direction_index][1]
        if is_within_rect(next_row, next_col):
            cur_row, cur_col = next_row, next_col
            sum_pos_value += grid[cur_row][cur_col]

print(sum_pos_value)