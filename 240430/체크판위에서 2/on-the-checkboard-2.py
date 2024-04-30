def can_move_to_last_position(cur_row, cur_col) -> bool:
    if cur_row < height - 1 and cur_col < width - 1:
        if rect_info[cur_row][cur_col] != rect_info[height - 1][width - 1]:
            return True
    return False

def find_paths(cur_row, cur_col, cur_moving_count) -> int:
    global result
    if cur_moving_count == 2:
        if can_move_to_last_position(cur_row, cur_col):
            return 1
        return 0
    for row_next_step_index in range(cur_row + 1, height - 1):
        for col_next_step_index in range(cur_col + 1, width - 1):
            if rect_info[cur_row][cur_col] != rect_info[row_next_step_index][col_next_step_index]: #색이 다르면
                result += find_paths(row_next_step_index, col_next_step_index, cur_moving_count + 1)
    return result


height, width= map(int, input().split())

rect_info = [
    input().split()
    for _ in range(height)
]

cur_row, cur_col = 0, 0
result = 0

print(find_paths(cur_row, cur_col, 0))