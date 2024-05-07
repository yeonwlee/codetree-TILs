num_of_rows, num_of_cols = map(int, input().split())

is_visited = [
    [0 for _ in range(num_of_cols)]
    for _ in range(num_of_rows)
]

cur_direction_index = 0
cur_row, cur_col = 0, 0
#아래, 오른쪽, 위, 왼쪽
direction_change = ["D", "R", "U", "L"]
moving = {"D":(1, 0), "R":(0, 1), "U":(-1, 0), "L":(0, -1)}
is_can_move = True
direction = direction_change[cur_direction_index]
is_visited[0][0] = 1
count = 2

def is_in_rect(row_index:int, col_index: int) -> bool:
    return 0 <= row_index < num_of_rows and 0 <= col_index < num_of_cols


def move_forward(row_range_info:tuple, col_range_info:tuple, direction:str) -> str: #direction
    global cur_row, cur_col, cur_direction_index
    global is_visited
    global count
    row_start, row_end, row_step = row_range_info
    col_start, col_end, col_step = col_range_info
    for row_index in range(row_start, row_end, row_step):
        for col_index in range(col_start, col_end, col_step):
            next_row, next_col = cur_row + moving[direction][0], cur_col + moving[direction][1]
            if is_in_rect(next_row, next_col) and not is_visited[next_row][next_col]:
                is_visited[next_row][next_col] = count
                count += 1
                cur_row, cur_col = next_row, next_col
            else:
                break
    cur_direction_index += 1
    return direction_change[(cur_direction_index + 4) % 4]



while count != (num_of_cols * num_of_rows) + 1:
    if direction == "D":
        direction = move_forward((cur_row, num_of_rows, 1), (cur_col, cur_col + 1, 1), direction)
    elif direction == "R":
        direction = move_forward((cur_row, cur_row + 1,1), (cur_col, num_of_cols, 1), direction)
    elif direction == "U":
        direction = move_forward((cur_row, 0, -1), (cur_col, cur_col + 1, 1), direction)
    elif direction == "L":
        direction = move_forward((cur_row, cur_row + 1, 1), (cur_col, 0, -1), direction)


for row in is_visited:
    for col in row:
        print(col, end=" ")
    print()